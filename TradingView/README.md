
=======
Trading View
=======

| |PyPI|  |Python|

Introduction
============

This utility provides a means of establishing a connection, using the
FIX protocol, with an existing FIX application.  The connection is made
from a background agent process, but controlled by either a command-line
tool, or a programming language API.

It is intended for use in either ad-hoc FIX testing (using the command-line)
or for integration testing of FIX applications, where it can be configured
to simulate the intended FIX peer.  To automate testing, an existing
language unit testing framework is helpful: test cases can be written to
exercise your code, and interleaved with that you can drive the FIX peer
to confirm receipt of appropriate messages from your application, and to
craft responses (both correct and incorrect) to implement your testing
scenarios.

The agent process communicates with the command-line tool and programming
language APIs using a TCP session.  The protocol is simple, and uses
JSON-formatted messages.

Language SDKs are planned for Python, Java, DotNET, and possibly Go and
C/C++.  The command-line client enables use from shell scripts or ad-hoc
use from a shell session.

Caveats
=======

This project is very young.  It's nowhere near finished.  It probably
doesn't do what you need yet.

Contributing
============

Comments, suggestions, bug reports, bug fixes -- all contributions to
this project are welcomed.  See the project's `GitHub
<https://github.com/da4089/fixtool>`_ page for access to the latest
source code, and please open an `issue
<https://github.com/da4089/fixtool/issues>`_ for comments,
suggestions, and bugs.



.. |Build Status| image:: https://travis-ci.org/da4089/fixtool.svg?branch=master
    :target: https://travis-ci.org/da4089/fixtool
    :alt: Build status
.. |Docs| image:: https://readthedocs.org/projects/fixtool/badge/?version=latest
    :target: http://fixtool.readthedocs.io/en/latest/
    :alt: Docs
.. |Code Health| image:: https://api.codacy.com/project/badge/Grade/abd5c37cfe834d5ca5edb74853223986
    :target: https://app.codacy.com/app/da4089/fixtool/dashboard
    :alt: Code Health
.. |Coverage| image:: https://api.codacy.com/project/badge/Coverage/abd5c37cfe834d5ca5edb74853223986
    :target: https://app.codacy.com/app/da4089/fixtool/dashboard
    :alt: Coverage
.. |PyPI| image:: https://img.shields.io/pypi/v/fixtool.svg
    :target: https://pypi.python.org/pypi/fixtool
    :alt: PyPI
.. |Python| image:: https://img.shields.io/pypi/pyversions/fixtool.svg
    :target: https://pypi.python.org/pypi/fixtool
    :alt: Python
.. |Landscape| image:: https://landscape.io/github/da4089/fixtool/master/landscape.svg?style=flat
    :target: https://landscape.io/github/da4089/fixtool/master
    :alt: Code Health
.. |Coveralls| image:: https://coveralls.io/repos/github/da4089/fixtool/badge.svg?branch=master
    :target: https://coveralls.io/github/da4089/fixtool?branch=master
    :alt: Coverage
