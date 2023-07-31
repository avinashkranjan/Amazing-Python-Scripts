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

"""FIX protocol simulator and control APIs."""

import logging
import os
import stat
from .proxy import FixToolProxy
from .version import VERSION


def spawn_agent():
    """Create a new agent, and associated proxy.

    :returns: Reference to proxy, or None on error."""

    # Spawned agents are spawned from the calling process, and usually
    # dedicated to it.  It's possible to contact a spawned agent from
    # an independent process, but that's not the intended use case.
    #
    # When the agent starts, it is allocated an ephemeral port number.
    # That port number is reported on stdout from the process, and
    # can be read by the proxy which subsequently connects to it on
    # that port.
    #
    # The agent can be explicitly shutdown at any time by the proxy,
    # but will also be implicitly killed if the proxy instance is
    # deleted.

    # Look for fixtool-agent in PATH, then parent dirs of $CWD
    path = os.getenv("PATH", "")
    path_dirs = path.split(os.pathsep)
    cwd = os.path.realpath(os.curdir)
    while cwd != "/":
        path_dirs.append(cwd)
        cwd = os.path.dirname(cwd)

    fixtool_agent = None
    for dir_name in path_dirs:
        file_name = os.path.join(dir_name, "fixtool-agent")
        if os.path.exists(file_name):
            mode = os.stat(file_name).st_mode
            if mode & stat.S_IXUSR or \
                    mode & stat.S_IXGRP or \
                    mode & stat.S_IXOTH:
                fixtool_agent = file_name
                break

    if not fixtool_agent:
        logging.error("Unable to find agent executable")
        return None

    logging.info("Using agent: %s", fixtool_agent)

    agent = os.popen(fixtool_agent + ' start')
    status = agent.readline()
    agent.close()  # Just the parent; the forked agent is still running

    logging.info("Agent output: %s", status)

    if status[:2] != "OK":
        logging.error("Failed to start agent: %s", status)
        return None

    try:
        port = int(status[3:])
    except ValueError:
        logging.error("Unable to read port number from agent output")
        return None

    agent_proxy = FixToolProxy("localhost", port)
    return agent_proxy


def connect_agent(host: str, port: int):
    """Create a proxy, and connect it to an existing agent.

    :param host: String host name or IP address for the agent.
    :param port: Integer TCP port number for the agent."""

    agent_proxy = FixToolProxy(host, port)
    return agent_proxy
