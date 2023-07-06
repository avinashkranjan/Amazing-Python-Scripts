from subprocess import call
from sys import platform as _platform
from colors import logcolors


def init():
    call('git init')


def createReadme():
    if _platform == "linux" or _platform == "linux2":
        call('touch README.md')
    elif _platform == "darwin":
        call('touch README.md')
    elif _platform == "win32":
        call('type nul>README.md')


def add(filelist):
    for file in filelist:
        # perform git add on file
        print(f"{logcolors.SUCCESS}Adding{logcolors.ENDC}",
              file.split('\\')[-1])
        call(('git add ' + file))


# git commit -m "passed message"


def commit(filelist, *args, **kwargs):
    diffarr = kwargs.get('diffarr', -1)
    for file in filelist:
        # ask user for commit message
        msg = str(
            input(
                f'{logcolors.BOLD}Enter the commit message for{logcolors.ENDC} '
                + file.split('\\')[-1] +
                f' {logcolors.BOLD}or enter {logcolors.ERROR}-r{logcolors.ENDC} to reject commit{logcolors.ENDC}'
            ))
        # if msg == -r reject commit
        if (msg == '-r'):
            print(f'{logcolors.ERROR}commit rejected{logcolors.ENDC}')
            if (diffarr != -1):
                diffarr.remove(diffarr[filelist.index(file)])
            filelist.remove(file)
            call('cls', shell=True)
            return False
        # else execute git commit for the file
        # added a comment
        else:
            call('git commit -m "' + msg + '"')
            call('cls', shell=True)
            print(
                f'Commited {logcolors.CYAN}{file}{logcolors.ENDC} with msg: {logcolors.BOLD}{msg}{logcolors.ENDC}'
            )


def setremote(url):
    call('git remote add origin ' + url)


def setBranch(branch):
    call('git branch -M ' + branch)


# git push


def push(url, branch):
    call('git push -u ' + url + ' ' + branch)
    call('cls', shell=True)
    print(f'{logcolors.SUCCESS}Successfully Pushed Changes{logcolors.ENDC}')
