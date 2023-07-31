#! /usr/bin/env python3
##################################################################
# fixtool
# Copyright (C) 2017-2018, David Arnold.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
##################################################################

"""Background agent that manages the fixtool sessions."""

import argparse
import asyncio
import base64
import json
import logging
import os
import signal
import socket
import struct
import sys
import tempfile
import time

import simplefix

# pylint: disable=unused-wildcard-import
from fixtool.message import *
from fixtool.proxy import FixToolProxy
from fixtool.version import VERSION

# Log level names, from argv.
LOGLEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}


class Client:
    """Simulated FIX client."""

    def __init__(self, name: str):
        """Constructor."""
        self._name = name
        self._comp_id = b''
        self._auto_heartbeat = True
        self._auto_sequence = True
        self._raw = False
        self._next_send_sequence = 0
        self._last_seen_sequence = 0
        self._host = None
        self._port = None
        self._is_connected = False

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setblocking(True)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self._parser = simplefix.FixParser()
        self._queue = []
        return

    def destroy(self):
        """Destroy the client instance."""
        if self._is_connected:
            self.disconnect()

        return

    def connect(self, host: str, port: int):
        """Attempt connection to a FIX server.

        :param host: Server's host name or IP address.
        :param port: Server's TCP port number."""
        self._host = host
        self._port = port
        self._socket.connect((self._host, self._port))
        self._is_connected = True

        asyncio.get_event_loop().add_reader(self._socket, self.readable)
        return

    def is_connected(self):
        """Returns True if this client is connected to a server."""
        return self._is_connected

    def disconnect(self):
        """Close the active server connection for this client."""
        asyncio.get_event_loop().remove_reader(self._socket)
        self._socket.close()
        self._is_connected = False
        return

    def readable(self):
        """Handle received data on the client's server connection.

        This method actually parses the message content, so it must
        be well-formed FIX, so that it can detect the end of the
        message.  This is perhaps not ideal, but ..."""
        buf = self._socket.recv(65536)
        if not buf:
            self.disconnect()
            return

        self._parser.append_buffer(buf)
        message = self._parser.get_message()
        while message is not None:
            self._queue.append(message.encode())
            message = self._parser.get_message()
        return

    def receive_queue_length(self) -> int:
        """Return the number of messages on the received message queue."""
        return len(self._queue)

    def get_message(self):
        """Return the first message from the received message queue."""
        if self.receive_queue_length() < 1:
            return None
        return self._queue.pop(0)

    def send_message(self, message: bytes):
        """Send a message to the connected server session.

        :param message: Byte array of formatted FIX message to send.

        The message has been received via the control protocol, where
        it was wrapped/unwrapped in BASE64, and we assume it is good.
        We send it as-is."""
        self._socket.sendall(message)
        return


class Server:
    def __init__(self):
        """Constructor."""
        self._auto_heartbeat = True
        self._auto_sequence = True
        self._raw = False
        self._next_send_sequence = 0
        self._last_seen_sequence = 0
        self._pending_sessions = []
        self._accepted_sessions = {}

        self._socket = None
        return

    def destroy(self):
        """Destroy the server instance."""
        if self._socket is not None:
            self.unlisten()

        for session in self._pending_sessions:
            session.destroy()
        self._pending_sessions = []

        for session in self._accepted_sessions.values():
            session.destroy()
        self._accepted_sessions = {}
        return

    def is_raw(self):
        """Is this server configured in 'raw' mode?"""
        return self._raw

    def listen(self, port):
        """Listen for client connections.

        :param port: TCP port number to listen on."""
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setblocking(False)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(('', port))
        self._socket.listen(5)
        actual_port = self._socket.getsockname()[1]

        asyncio.get_event_loop().add_reader(self._socket, self.acceptable)
        return actual_port

    def unlisten(self):
        """Stop listening for client connections."""
        asyncio.get_event_loop().remove_reader(self._socket)
        self._socket.close()
        self._socket = None
        return

    def acceptable(self):
        """Handle readable event on listening socket."""
        sock, _ = self._socket.accept()
        session = ServerSession(self, sock)
        self._pending_sessions.append(session)
        return

    def pending_client_count(self):
        """Return number of pending client sessions."""
        return len(self._pending_sessions)

    def accept_client_session(self, name: str):
        """Accept a pending client session.

        :param name: Name for client session."""

        if self.pending_client_count() < 1:
            return None

        client = self._pending_sessions.pop(0)
        client.set_name(name)
        self._accepted_sessions[name] = client
        return client


class ServerSession:
    """Server state of an active client connection."""

    def __init__(self, server: Server, sock: socket.SocketType):
        """Constructor.

        :param server: Server instance that owns this session.
        :param sock: ephemeral sock for this session."""
        self._server = server
        self._socket = sock
        self._name = None
        self._parser = simplefix.FixParser()
        self._is_connected = True
        self._queue = []

        asyncio.get_event_loop().add_reader(sock, self.readable)
        return

    def destroy(self):
        """Destroy the active session to a client."""
        if self._is_connected:
            self.disconnect()
        self._queue = []
        return

    def set_name(self, name: str):
        """Set the user-visible name of this session.

        :param name: User-visible name for this session, as used
        in logging, etc."""
        self._name = name
        return

    def readable(self):
        """Handle readable event on session's socket."""
        buf = self._socket.recv(65536)
        if not buf:
            self._is_connected = False
            return

        self._parser.append_buffer(buf)
        msg = self._parser.get_message()
        while msg is not None:
            self._queue.append(msg.encode())
            msg = self._parser.get_message()
        return

    def is_connected(self) -> bool:
        """Return True if session is connected."""
        return self._is_connected

    def disconnect(self):
        """Close this session."""
        asyncio.get_event_loop().remove_reader(self._socket)
        self._socket.close()
        self._socket = None
        self._is_connected = False
        return

    def receive_queue_length(self) -> int:
        """Return the number of messages on the received message queue."""
        return len(self._queue)

    def get_message(self):
        """Return the first message from the received message queue."""
        if self.receive_queue_length() < 1:
            return None
        return self._queue.pop(0)

    def send_message(self, message: bytes):
        """Send a message to the connected client.

        :param message: Byte array of formatted FIX message to send."""
        self._socket.sendall(message)
        return


class ControlSession:
    """Control client session."""

    def __init__(self, sock: socket.SocketType):
        """Constructor.

        :param sock: Accepted socket."""
        self._socket = sock
        self._buffer = b''
        return

    def append_bytes(self, buffer: bytes):
        """Receive a buffer of bytes from this control client.

        :param buffer: Array of bytes from client."""
        self._buffer += buffer
        if len(self._buffer) <= 4:
            # No payload yet
            return None

        payload_length = struct.unpack(b'>L', self._buffer[:4])[0]
        if len(buffer) < 4 + payload_length:
            # Not received full message yet
            return None
        self._buffer = self._buffer[4:]

        # FIXME: deal with the case where there's multiple control
        # FIXME: messages in the buffer.

        payload = self._buffer[:payload_length]
        self._buffer = self._buffer[payload_length:]
        return payload

    def send(self, payload: bytes):
        """Send a buffer to the control client.

        :param payload: Array of bytes to send to client."""

        payload_length = len(payload)
        header = struct.pack(">L", payload_length)
        self._socket.sendall(header + payload)
        return

    def close(self):
        """Close this connection."""
        self._socket.close()
        return


class FixToolAgent(object):
    """Main class for the simulation agent."""

    def __init__(self, port=0):
        """Constructor.

        :param port: TCP port number for accepting control sessions."""
        self._socket = None
        self._loop = None

        self._control_sessions = {}
        self._clients = {}
        self._servers = {}
        self._server_sessions = {}

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setblocking(False)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(('0.0.0.0', port))
        self._socket.listen(5)

        self._loop = asyncio.get_event_loop()
        self._loop.add_reader(self._socket, self.accept)
        self._loop.add_signal_handler(signal.SIGINT, self.handle_sigint)

        name = self._socket.getsockname()
        self._port = name[1]
        return

    def port(self):
        """Get the active control sessions port number."""
        return self._port

    def run(self):
        """Enter mainloop."""
        self._loop.run_forever()
        return

    def stop(self):
        """Exit mainloop."""
        if self._loop.is_running():
            self._loop.stop()
            logging.debug("event loop stopped.")
        return

    def reset(self):
        """Clean up all simulated entities."""

        logging.info("agent reseting ...")
        # Server listening sockets.
        for server in self._servers.values():
            server.destroy()
        self._servers = {}

        # Client sessions.
        for client in self._clients.values():
            client.destroy()
        self._clients = {}

        # Server sessions are cleaned up by server.destroy()
        self._server_sessions = {}

        logging.info("agent reset complete.")
        return

    def shutdown(self):
        """Clean up for exit."""

        logging.info("agent shutting down ...")
        self.stop()
        self.reset()

        # Control sessions.
        for sock, session in self._control_sessions.items():
            self._loop.remove_reader(sock)
            session.close()
        self._control_sessions = {}

        # Control session listening socket.
        self._loop.remove_reader(self._socket)
        self._socket.close()
        self._socket = None
        self._port = None

        # Event loop.
        self._loop.remove_signal_handler(signal.SIGINT)
        self._loop.close()
        self._loop = None

        logging.info("agent shutdown complete.")
        return

    def handle_sigint(self, *args):
        """Handle SIGINT."""
        # pylint: disable=unused-argument
        logging.info("Exiting on C-c.")
        self.stop()
        return

    def accept(self):
        """Accept a new control client connection."""
        sock, addr = self._socket.accept()
        self._loop.add_reader(sock, self.readable, sock)
        self._control_sessions[sock] = ControlSession(sock)

        logging.info("Accepted control session from %s", addr[0])
        return

    def readable(self, sock):
        """Handle readable event on a control client socket."""
        logging.log(logging.DEBUG, "Control session readable")
        control_session = self._control_sessions[sock]
        buf = sock.recv(65536)
        if not buf:
            self._loop.remove_reader(sock)
            del self._control_sessions[sock]
            control_session.close()
            logging.log(logging.INFO, "Disconnected control session.")
            return

        payload = control_session.append_bytes(buf)
        while payload is not None:
            message = json.loads(payload.decode())
            self.handle_request(control_session, message)
            payload = None  # FIXME: deal with multiple messages

        return

    def handle_request(self, client, message):
        """Process a received message."""

        message_type = message["type"]
        logging.debug("Dispatching [%s]", message_type)

        if message_type == "client_create":
            self.handle_client_create(client, message)

        elif message_type == "client_destroy":
            self.handle_client_destroy(client, message)

        elif message_type == "client_connect":
            self.handle_client_connect(client, message)

        elif message_type == "client_is_connected_request":
            self.handle_client_is_connected_request(client, message)

        elif message_type == "client_send":
            self.handle_client_send(client, message)

        elif message_type == "client_receive_count_request":
            self.handle_client_receive_count_request(client, message)

        elif message_type == "client_get":
            self.handle_client_get(client, message)

        elif message_type == "server_create":
            self.handle_server_create(client, message)

        elif message_type == "server_destroy":
            self.handle_server_destroy(client, message)

        elif message_type == "server_listen":
            self.handle_server_listen(client, message)

        elif message_type == "server_unlisten":
            self.handle_server_unlisten(client, message)

        elif message_type == "server_pending_accept_request":
            self.handle_server_pending_accept_request(client, message)

        elif message_type == "server_accept":
            self.handle_server_accept(client, message)

        elif message_type == "server_is_connected_request":
            self.handle_server_is_connected_request(client, message)

        elif message_type == "server_disconnect":
            self.handle_server_disconnect(client, message)

        elif message_type == "session_send":
            self.handle_session_send(client, message)

        elif message_type == "session_receive_count_request":
            self.handle_session_receive_count_request(client, message)

        elif message_type == "session_get":
            self.handle_session_get(client, message)

        elif message_type == "shutdown":
            self.handle_shutdown(client, message)

        elif message_type == "reset":
            self.handle_reset(client, message)

        else:
            logging.critical("Unknown message type: %s" % message_type)
        return

    def handle_shutdown(self, control: ControlSession, message: dict):
        """Handle a 'shutdown' request message.

        :param control: Control session.
        :param message: Control message."""
        # pylint: disable=unused-argument
        logging.info("agent shutdown() requested")
        self.stop()
        return

    def handle_reset(self, control: ControlSession, message: dict):
        """Handle a 'reset' request message.

        :param control: Control session.
        :param message: Control message."""
        logging.info("agent reset() requested.")
        self.reset()
        return

    def handle_client_create(self, control: ControlSession, message: dict):
        """Handler a 'client_create' request message.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        logging.info("client_create(%s)", name)
        if name in self._clients:
            response = ClientCreatedMessage(name, False,
                                            "Client %s already exists" % name)
            control.send(response.to_json().encode())
            return

        self._clients[name] = Client(name)

        response = ClientCreatedMessage(name, True, '')
        control.send(response.to_json().encode())
        return

    def handle_client_destroy(self, control: ControlSession, message: dict):
        """Handle a 'client_destroy' message.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        client = self._clients.get(name)
        if client is None:
            response = ClientDestroyedMessage(name, False,
                                              "No such client '$s'" % name)
            control.send(response.to_json().encode())
            return

        client.destroy()
        del self._clients[name]

        response = ClientDestroyedMessage(name, True, '')
        control.send(response.to_json().encode())
        return

    def handle_client_connect(self, control: ControlSession, message: dict):
        """Handle a 'client_connect' message.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        client = self._clients.get(name)
        if client is None:
            response = ClientConnectedMessage(name, False,
                                              "No such client '$s'" % name)
            control.send(response.to_json().encode())
            return

        client.connect(message.get("host"), message.get("port"))

        response = ClientConnectedMessage(name, True, '')
        control.send(response.to_json().encode())
        return

    def handle_client_is_connected_request(self, control: ControlSession,
                                           message: dict):
        """Handle a 'client_is_connected' request.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        client = self._clients.get(name)
        if client is None:
            response = ClientIsConnectedResponse(name, False,
                                                 "No such client %s" % name,
                                                 False)
            control.send(response.to_json().encode())
            return

        is_connected = client.is_connected()

        response = ClientIsConnectedResponse(name, True, '', is_connected)
        control.send(response.to_json().encode())
        return

    def handle_client_send(self, control: ControlSession, message: dict):
        """Handle a 'client_send' request.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        client = self._clients.get(name)
        if client is None:
            response = ClientSentMessage(name, False,
                                         "No such client: %s" % name)
            control.send(response.to_json().encode())
            return

        payload = message.get("payload")
        buffer = base64.b64decode(payload)
        client.send_message(buffer)

        response = ClientSentMessage(name, True, '')
        control.send(response.to_json().encode())
        return

    def handle_client_receive_count_request(self,
                                            control: ControlSession,
                                            message: dict):
        """Process a 'client_get' message.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        client = self._clients.get(name)
        if client is None:
            logging.warning("No sucj client: %s" % name)
            response = ClientReceiveCountResponse(name, False,
                                                  "No such client: %s" % name,
                                                  0)
            control.send(response.to_json().encode())
            return

        count = client.receive_queue_length()
        logging.info("client_receive_count_request(%s): "
                     "%d" % (name, count))
        response = ClientReceiveCountResponse(name, True, '', count)
        control.send(response.to_json().encode())
        return

    def handle_client_get(self, control: ControlSession, message: dict):
        """Process a 'client_get' message.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        client = self._clients.get(name)
        if client is None:
            response = ClientGotMessage(name, False,
                                        "No such client: %s" % name,
                                        None)
            control.send(response.to_json().encode())
            return

        fix_message = client.get_message()
        buffer = base64.b64encode(fix_message).decode("ascii")
        response = ClientGotMessage(name, True, '', buffer)
        control.send(response.to_json().encode())
        return

    def handle_server_create(self, client: ControlSession, message: dict):
        """Process a server_create message.

        :param client: Reference to the sending client.
        :param message: """
        name = message.get("name")
        if name in self._servers:
            response = ServerCreatedMessage(name, False,
                                            "Server '%s' already exists" % name)
            client.send(response.to_json().encode())
            return

        # Create server.
        server = Server()

        # Register in table.
        self._servers[name] = server

        # Send reply.
        response = ServerCreatedMessage(name, True, '')
        client.send(response.to_json().encode())
        return

    def handle_server_destroy(self, control: ControlSession, message: dict):
        """Handle a 'server_destroy' request.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        server = self._servers.get(name)
        if server is None:
            response = ServerDestroyedMessage(name, False,
                                              "No such server '$s'" % name)
            control.send(response.to_json().encode())
            return

        server.destroy()
        del self._servers[name]

        response = ServerDestroyedMessage(name, True, '')
        control.send(response.to_json().encode())
        return

    def handle_server_listen(self, control: ControlSession, message: dict):
        """Handle a 'server_listen' message.

        :param control: Control session.
        :param message: Control message."""
        name = message["name"]
        server = self._servers.get(name)
        if server is None:
            logging.warning("server_listen(%s): no such server." % name)
            response = ServerListenedMessage(name, False,
                                             "No such server '%s'" % name)
            control.send(response.to_json().encode())
            return

        port = message.get("port")
        if port is None or port < 0 or port > 65535:
            logging.warning("server_listen(%s, %s): bad port."
                            % (name, str(port)))
            response = ServerListenedMessage(name, False,
                                             "Bad or missing port")
            control.send(response.to_json().encode())
            return

        actual_port = server.listen(port)

        response = ServerListenedMessage(name, True, '', actual_port)
        control.send(response.to_json().encode())
        return

    def handle_server_unlisten(self, control: ControlSession, message: dict):
        """Handle a 'server_unlisten' request.

        :param control: Control session.
        :param message: Control message."""
        name = message["name"]
        server = self._servers.get(name)
        if server is None:
            response = ServerUnlistenedMessage(name, False,
                                               "No such server '%s'" % name)
            control.send(response.to_json().encode())
            return

        server.unlisten()

        response = ServerUnlistenedMessage(name, True, '')
        control.send(response.to_json().encode())
        return

    def handle_server_pending_accept_request(self,
                                             control: ControlSession,
                                             message: dict):
        """Handle a 'server_pending_accept' request.

        :param control: Control session.
        :param message: Control message."""
        name = message["name"]
        server = self._servers.get(name)
        if server is None:
            response = ServerPendingAcceptCountResponse(
                name, False, "No such server '%s'" % name, 0)
            control.send(response.to_json().encode())
            return

        count = server.pending_client_count()
        response = ServerPendingAcceptCountResponse(name, True, '', count)
        control.send(response.to_json().encode())
        return

    def handle_server_accept(self, control: ControlSession, message: dict):
        """Handle a 'server_accept' request.

        :param control: Control session.
        :param message: Control message."""

        logging.debug("STARTING handle_server_accept")

        name = message["name"]
        server = self._servers.get(name)
        if server is None:
            response = ServerAcceptedMessage(
                name, False, "No such server '%s'" % name, '')
            control.send(response.to_json().encode())
            return

        logging.debug("GOT server [%s]" % name)
        session_name = message.get("session_name")
        session = server.accept_client_session(session_name)
        self._server_sessions[session_name] = session
        response = ServerAcceptedMessage(name, True, '', session_name)
        control.send(response.to_json().encode())
        logging.debug("SENT response")
        return

    def handle_server_is_connected_request(self, control: ControlSession,
                                           message: dict):
        """Handle 'server_is_connected' request.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        server_session = self._server_sessions.get(name)
        if server_session is None:
            response = ServerIsConnectedResponse(name, False,
                                                 "No such session %s" % name,
                                                 False)
            control.send(response.to_json().encode())
            return

        is_connected = server_session.is_connected()

        response = ServerIsConnectedResponse(name, True, '', is_connected)
        control.send(response.to_json().encode())
        return

    def handle_server_disconnect(self, control: ControlSession, message: dict):
        """Handle 'server_disconnect' request.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        server_session = self._server_sessions.get(name)
        if server_session is None:
            response = ServerDisconnectedMessage(name, False,
                                                 "No such session %s" % name)
            control.send(response.to_json().encode())
            return

        server_session.disconnect()

        response = ServerDisconnectedMessage(name, True, '')
        control.send(response.to_json().encode())
        logging.debug("Server session [%s] disconnected." % name)
        return

    def handle_session_send(self, control: ControlSession, message: dict):
        """Handle 'session_send' request.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        server_session = self._server_sessions.get(name)
        if server_session is None:
            response = SessionSentMessage(name, False,
                                          "No such session %s" % name)
            control.send(response.to_json().encode())
            return

        buffer = base64.b64decode(message.get("payload"))
        server_session.send_message(buffer)

        response = SessionSentMessage(name, True, '')
        control.send(response.to_json().encode())
        return

    def handle_session_receive_count_request(self,
                                             control: ControlSession,
                                             message: dict):
        """Handle 'session_receive_count_request' message.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        server_session = self._server_sessions.get(name)
        if server_session is None:
            logging.warning("session_receive_count_request(%s): "
                            "error: unknown session" % name)
            response = SessionReceiveCountResponse(name, False,
                                                   "No such session: "
                                                   "%s" % name, 0)
            control.send(response.to_json().encode())
            return

        count = server_session.receive_queue_length()
        logging.debug("session_receive_count_request(%s): "
                      "%d" % (name, count))
        response = SessionReceiveCountResponse(name, True, '', count)
        control.send(response.to_json().encode())
        return

    def handle_session_get(self, control: ControlSession, message: dict):
        """Handle 'session_get' request.

        :param control: Control session.
        :param message: Control message."""
        name = message.get("name")
        server_session = self._server_sessions.get(name)
        if server_session is None:
            response = SessionGotMessage(name, False,
                                         "No such session %s" % name,
                                         b'')
            control.send(response.to_json().encode())
            return

        fix_message = server_session.get_message()
        payload = base64.b64encode(fix_message).decode("ascii")
        response = SessionGotMessage(name, True, '', payload)
        control.send(response.to_json().encode())
        return


def main():
    """Main function for agent."""

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version",
                        action="version",
                        version=VERSION)
    parser.add_argument("-l", "--loglevel",
                        default="WARNING",
                        choices=LOGLEVELS.keys(),
                        help="Suppress messages with priority below this")
    parser.add_argument("-f", "--foreground",
                        action="store_true",
                        help="Don't daemonise; run in the foreground")
    parser.add_argument("-p", "--port", type=int,
                        default=0,
                        help="TCP port number for control sessions")
    parser.add_argument("action", type=str,
                        choices=("start", "stop", "reset"),
                        help="Action to perform")
    args = parser.parse_args()

    # Logging.
    tmpdir = "/tmp" if sys.platform == "darwin" else tempfile.gettempdir()
    now = time.strftime("%Y%m%d-%H%M%S")
    logfile = os.path.join(tmpdir, "fixtool-" + now + ".log")
    level = LOGLEVELS.get(args.loglevel.lower(), logging.DEBUG)
    logging.basicConfig(filename=logfile,
                        level=level,
                        format="%(asctime)s.%(msecs)03d %(name)s "
                               "%(levelname)s  %(message)s",
                        datefmt="%Y/%m/%d-%H:%M:%S")
    logging.log(logging.INFO, "Starting")

    # Dispatch.
    if args.action == "start":
        if not args.foreground:
            pid = os.fork()
            if pid != 0:
                # Exit parent process without cleaning up, so child
                # retains control of shared resources.
                os._exit(0)

        try:
            agent = FixToolAgent(args.port)
        except OSError:
            print("ERROR creating agent on port " + str(args.port))
            sys.exit(1)

        print("OK " + str(agent.port()))
        sys.stdout.flush()

        try:
            agent.run()
        finally:
            agent.shutdown()

        logging.info("Exiting")
        sys.exit(0)

    elif args.action == "stop":
        if not args.port:
            print("ERROR need port number for 'stop' action.")
            sys.exit(1)

        try:
            proxy = FixToolProxy('localhost', args.port)
            proxy.shutdown()
            sys.exit(0)

        except ConnectionRefusedError:
            print("ERROR no agent running on port " + str(args.port))

        sys.exit(1)

    elif args.action == "reset":
        if not args.port:
            print("ERROR need port number for 'reset' action.")
            sys.exit(1)

        try:
            proxy = FixToolProxy('localhost', args.port)
            proxy.reset()
            sys.exit(0)

        except ConnectionRefusedError:
            print("ERROR no agent running on port " + str(args.port))

        sys.exit(1)

    return


if __name__ == "__main__":
    main()


##################################################################
