#! /usr/bin/env python3
########################################################################
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
########################################################################

from fixtool import VERSION
import inspect
import os
import sys

from setuptools import setup

# Add fixtool to the PYTHONPATH so we can get the version.
d = os.path.dirname(inspect.getfile(inspect.currentframe()))
d = os.path.join(d, "python")
sys.path.append(d)


with open("README.rst") as readme:
    long_description = readme.read()

setup(name="fixtool",
      version=VERSION,
      description="FIX Protocol testing tool",
      long_description=long_description,
      url="https://github.com/da4089/fixtool",
      author="David Arnold",
      author_email="d+fixtool@0x1.org",
      license="MIT",
      keywords="fix testing",
      install_requires=["simplefix>=1.0.8"],
      package_dir={"": "python"},
      packages=["fixtool"],
      entry_points={
          "console_scripts": [
              "fixtool-agent=fixtool.agent:main"
          ]
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Topic :: System :: Networking',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      )


########################################################################
