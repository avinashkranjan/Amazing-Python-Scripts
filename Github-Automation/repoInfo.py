import subprocess
import os
mypath = os.getcwd()
infofile = mypath + '/.git/config'


def takeInfo():
    print('No Existing repo info found\n')
    url = str(input('Enter the Github Repo URL: '))
    branch = str(input('Enter the branch: '))
    info = ['n', url, branch]
    return info


def checkinfoInDir():
    if (os.path.exists(infofile)):
        url = subprocess.Popen(
            'git config --get remote.origin.url',
            stdout=subprocess.PIPE).stdout.read().decode('utf-8')

        branch = subprocess.Popen(
            'git rev-parse --symbolic-full-name HEAD',
            stdout=subprocess.PIPE).stdout.read().decode('utf-8')

        url, branch = url.split('\n')[0], branch.split('\n')[0].split('/')[2]
        info = [url, branch]
    else:
        info = takeInfo()
    return info
