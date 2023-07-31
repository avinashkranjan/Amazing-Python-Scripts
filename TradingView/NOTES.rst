Publishing a Release
====================

Check the setup.py version.
Commit and push everything.
Activate the 3.6 venv (to get twine, wheel, etc)
Run: rm -rf dist
Run: python setup.py sdist
Run: python setup.py bdist_wheel --universal
Run: twine upload dist/*
Run: git tag v$VERSION
Run: git push --tags
Go to GitHub and make a release
Bump the setup.py version for next time, and commit.

Control Protocol
================

The control protocol is used between the language APIs (including the
CLI) and the agent.  It enables the API clients to control the agent,
creating and using client (initiator) and server (responder) FIX peers.

The agent is controled via one or more TCP sessions.  The message
format used over this TCP session is as follows:

Each message consists of a framing header and a payload.

The framing header is a 4 byte big-endian integer number of bytes in
the payload.  That is, the number of bytes following the header in this
message.  The total TCP payload length will be this value, plus four.

The payload is JSON.  Each message must contain:
* the "type" field, a string, being the type of this message
* the "name" field, a string, identifying the entity to which the message
applies

Response messages, returned from the agent to the APIs will also contain:
* the "result" field, a boolean, indicating the success (or failure) of
their matching request.
* the "message" field, a string, describing the error if there was one.

FIX messages are transported as a JSON string.  JSON requires strings to
be valid UTF8, and a FIX message is not that, so they're encoded using
BASE64 before being sent.


So, applications should pass FIX messages to the language APIs as a
formatted byte array.