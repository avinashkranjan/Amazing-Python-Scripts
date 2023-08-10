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

import fixtool
import simplefix


def test_spawn():
    proxy = fixtool.spawn_agent()
    assert proxy is not None

    proxy.shutdown()
    return


def test_create_server():
    proxy = fixtool.spawn_agent()
    assert proxy is not None

    s1 = proxy.create_server("s1")
    s1.listen(23456)

    c1 = proxy.create_client("c1")
    c1.connect('localhost', 23456)

    assert s1.pending_accept_count() == 1
    cs1 = s1.accept("cs1")
    assert c1.is_connected()
    assert cs1.is_connected()

    fix_msg = simplefix.FixMessage()
    fix_msg.append_pair(8, "FIX.4.2")
    fix_msg.append_pair(35, 0)
    fix_msg.append_pair(34, 1)
    fix_msg.append_utc_timestamp(52)
    send_buf = fix_msg.encode()

    c1.send(send_buf)
    assert cs1.receive_queue_length() == 1

    m1 = cs1.receive()

    c1.destroy()
    s1.destroy()
    proxy.shutdown()
    return


def xxx_test_connect_disconnect():
    proxy = fixtool.FixToolProxy("localhost", 11011)
    client = proxy.create_client("c1")
    server = proxy.create_server("s1")
    server.listen(12000)
    assert server.pending_accept_count() == 0

    client.connect("localhost", 12000)
    assert server.pending_accept_count() == 1

    server_session = server.accept("ss1")
    assert server_session.is_connected()
    assert client.is_connected()

    server_session.disconnect()
    assert not server_session.is_connected()
    assert not client.is_connected()

    client.destroy()
    server_session.destroy()
    server.destroy()
    return
