# Network-Usage-Tracker
A python script to keep a track of network usage and notify you if it exceeds a specified limit
(only support for wifi right now)

### Requirements:

#####**This script needs Python 3+**

You may also need to install vnstat if you don't have it already installed
```bash
$ sudo apt-get install vnstat
```

### Usage:

```bash
$ python bandwidth_py3.py xxx MiB/GiB &
```
The '&' has been added to run the process in background. If you want to stop the process at any time use :

```bash
$ ps -ef
```
to get the list of running processes and then get the pid of the process you want to kill and do :

```bash
$ sudo kill pid
```
