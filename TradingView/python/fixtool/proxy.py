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

"""Python API to fixtool simulator agent."""

import base64
import json
import logging
import socket
import struct

from fixtool.message import *


class Client(object):
    """Local proxy for FIX client in agent."""

    def __init__(self, proxy, name: str):
        """(Internal) Constructor."""
        self._proxy = proxy
        self._name = name
        self._host = None
        self._port = None
        self._destroyed = False

        msg = ClientCreateMessage(self._name)
        self._proxy.send_request(msg)
        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)
        return

    def destroy(self):
        """Clean up this client, both locally and in the remote agent."""
        assert not self._destroyed

        request = ClientDestroyMessage(self._name)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)

        self._proxy.remove_client(self._name)
        self._destroyed = True
        return

    def connect(self, host: str, port: int):
        """Connect the client to the specified host and port.

        :param host: String host name or IP address.
        :param port: Integer TCP port number."""

        assert not self._destroyed

        self._host = host
        self._port = port

        msg = ClientConnectMessage(self._name, self._host, self._port)
        self._proxy.send_request(msg)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)
        return

    def disconnect(self):
        """Disconnect the client for its server peer."""
        assert not self._destroyed

        self._proxy.send_request({"message": "client_disconnect"})
        return

    def is_connected(self):
        """Returns True if connected to a peer server."""
        assert not self._destroyed

        request = ClientIsConnectedRequest(self._name)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)

        return response.connected

    def send(self, message: bytes):
        """Send a FIX message to the connected server peer.

        :param message: Byte array containing formatted FIX message to send."""
        assert not self._destroyed

        payload = base64.b64encode(message).decode("ascii")
        request = ClientSendMessage(self._name, payload)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)
        return

    def receive_queue_length(self) -> int:
        """Return number of messages waiting to be collected from the client."""
        assert not self._destroyed

        request = ClientReceiveCountRequest(self._name)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)
        return response.count

    def receive(self) -> bytes:
        """Return a FIX message received from the connected server.

        If no messages are queued, returns None."""

        request = ClientGetMessage(self._name)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)

        message = base64.b64decode(response.payload)
        return message


class Server(object):
    """Local proxy for FIX server in agent."""

    def __init__(self, proxy, name: str):
        """(Internal) Constructor."""
        self._proxy = proxy
        self._name = name
        self._clients = {}
        self._ports = []
        self._destroyed = False

        msg = ServerCreateMessage(self._name)
        self._proxy.send_request(msg)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)
        return

    def destroy(self):
        """Clean up this server, both locally and in remote agent."""
        assert not self._destroyed

        for session in self._clients.values():
            session.destroy()
        self._clients = {}

        for port in self._ports[:]:
            self.stop_listening(port)

        assert len(self._clients) == 0
        assert len(self._ports) == 0

        request = ServerDestroyMessage(self._name)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)

        self._proxy.remove_server(self._name)
        self._destroyed = True
        return

    def listen(self, port: int = 0):
        """Listen for connections on specified port.

        :param port: TCP port number on which to listen for connections.
        :returns: Listening port number."""
        assert not self._destroyed

        msg = ServerListenMessage(self._name, port)
        self._proxy.send_request(msg)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)

        actual_port = response.port
        self._ports.append(actual_port)
        return actual_port

    def stop_listening(self, port: int):
        """Stop listening for connections on specified port.

        :param port: TCP port number on which to stop listening."""
        assert not self._destroyed

        request = ServerUnlistenMessage(self._name, port)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)

        self._ports.remove(port)
        return

    def pending_accept_count(self):
        """Return the number of sessions waiting to be accepted."""
        assert not self._destroyed

        msg = ServerPendingAcceptCountRequest(self._name)
        self._proxy.send_request(msg)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)
        return response.count

    def accept(self, new_name: str):
        """Accept connection from a client.

        :param new_name: Name by which this session should become known."""
        assert not self._destroyed

        msg = ServerAcceptMessage(self._name, new_name)
        self._proxy.send_request(msg)

        response = self._proxy.await_response()
        logging.info("GOT accept response from agent")
        if not response.result:
            raise RuntimeError(response.message)

        client = ServerSession(self, self._proxy, response.session_name)
        self._clients[response.session_name] = client
        return client


class ServerSession(object):
    """Local proxy for server-side session with connected client."""

    def __init__(self, server, proxy, name):
        """(Internal) Constructor."""
        self._server = server
        self._proxy = proxy
        self._name = name
        self._connected = True
        return

    def destroy(self):
        """Clean up this session, both locally and in remote agent.

        Will disconnect the session if currently connected, and discard
        any queued messages."""
        if self._connected:
            self.disconnect()
        return

    def is_connected(self):
        """Return True if the session remains connected."""
        request = ServerIsConnectedRequest(self._name)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)

        return response.connected

    def disconnect(self):
        """Disconnect this session from its client."""
        request = ServerDisconnectMessage(self._name)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)

        self._connected = False
        return

    def send(self, message: bytes):
        """Send a message to the connected FIX client.

        :param message: Byte array of formatted FIX message to send."""

        assert message
        assert self._connected

        payload = base64.b64encode(message).decode("ascii")
        request = SessionSendMessage(self._name, payload)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)
        return

    def receive_queue_length(self):
        """Return the number of messages queued from the connected client."""

        assert self._connected

        request = SessionReceiveCountRequest(self._name)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)
        return response.count

    def receive(self) -> bytes:
        """Return a message received from the connected client.

        If no messages are queued, returns None."""
        assert self._connected

        request = SessionGetMessage(self._name)
        self._proxy.send_request(request)

        response = self._proxy.await_response()
        if not response.result:
            raise RuntimeError(response.message)

        message = base64.b64decode(response.payload)
        return message


class FixToolProxy(object):
    """Proxy for communication with remote FIX agent."""

    def __init__(self, host: str, port: int):
        """Constructor.

        :param host: String host name or IP address for agent."""
        self._host = host
        self._port = port
        self._clients = {}
        self._servers = {}

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((host, port))
        self._socket.setblocking(True)

        self._buffer = b''
        return

    def shutdown(self):
        """Shutdown the associated agent."""
        message = ShutdownMessage()
        self.send_request(message)

        self._socket.close()
        self._socket = None

        self._clients = {}
        self._servers = {}
        return

    def reset(self):
        """Reset the associated agent."""
        message = ResetMessage()
        self.send_request(message)

        self._clients = {}
        self._servers = {}
        return

    def create_client(self, name: str):
        """Create a FIX client.

        :param name: Unique name for this FIX client."""
        client = Client(self, name)
        self._clients[name] = client
        return client

    def create_server(self, name: str):
        """Create a FIX server.

        :param name: Unique name for this FIX server."""
        server = Server(self, name)
        self._servers[name] = server
        return server

    def send_request(self, message):
        """(Internal) Send message to agent."""
        payload = message.to_json().encode('UTF-8')
        payload_length = len(payload)
        header = struct.pack(">L", payload_length)
        self._socket.sendall(header + payload)
        return

    def await_response(self):
        """(Internal) Wait for message from agent."""
        while True:
            buf = self._socket.recv(65536)
            if len(buf) == 0:
                # Disconnected.
                return None

            self._buffer += buf
            if len(self._buffer) <= 4:
                continue

            message_length = struct.unpack(">L", self._buffer[:4])[0]
            self._buffer = self._buffer[4:]
            if len(self._buffer) < message_length:
                continue

            message_buf = self._buffer[:message_length]
            self._buffer = self._buffer[message_length:]

            d = json.loads(message_buf.decode())
            message = None
            message_type = d.get("type")
            if message_type == "client_created":
                message = ClientCreatedMessage.from_dict(d)

            elif message_type == "client_destroyed":
                message = ClientDestroyedMessage.from_dict(d)

            elif message_type == "client_connected":
                message = ClientConnectedMessage.from_dict(d)

            elif message_type == "client_is_connected_response":
                message = ClientIsConnectedResponse.from_dict(d)

            elif message_type == "client_sent":
                message = ClientSentMessage.from_dict(d)

            elif message_type == "client_receive_count_response":
                message = ClientReceiveCountResponse.from_dict(d)

            elif message_type == "client_got":
                message = ClientGotMessage.from_dict(d)

            elif message_type == "server_created":
                message = ServerCreatedMessage.from_dict(d)

            elif message_type == "server_destroyed":
                message = ServerDestroyedMessage.from_dict(d)

            elif message_type == "server_listened":
                message = ServerListenedMessage.from_dict(d)

            elif message_type == "server_unlistened":
                message = ServerUnlistenedMessage.from_dict(d)

            elif message_type == "server_pending_accept_response":
                message = ServerPendingAcceptCountResponse.from_dict(d)

            elif message_type == "server_accepted":
                message = ServerAcceptedMessage.from_dict(d)

            elif message_type == "server_is_connected_response":
                message = ServerIsConnectedResponse.from_dict(d)

            elif message_type == "server_disconnected":
                message = ServerDisconnectedMessage.from_dict(d)

            elif message_type == "session_receive_count_response":
                message = SessionReceiveCountResponse.from_dict(d)

            elif message_type == "session_sent":
                message = SessionSentMessage.from_dict(d)

            elif message_type == "session_got":
                message = SessionGotMessage.from_dict(d)

            else:
                logging.critical("Unknown message type: %s" % message_type)

            return message

    def remove_client(self, name):
        """(Iinternal) Remove named client from clients table."""
        del self._clients[name]
        return

    def remove_server(self, name):
        """(Internal) Remove named server from servers table."""
        del self._servers[name]
        return
