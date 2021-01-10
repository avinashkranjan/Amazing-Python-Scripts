from subprocess import call
from sys import platform as _platform
def init():
    print('git init')
# git add <filename>
def createReadme():
    if _platform == "linux" or _platform == "linux2":
        call('touch README.md')
    elif _platform == "darwin":
        call('touch README.md')
    elif _platform == "win32":
        call('type nul>README.md')


# Windows
def add(filelist):
    for file in filelist:
        # perform git add on file
        print("Adding" , file)
        call(('git add ' + file))

# git commit -m "passed message"
def commit(filelist):
    for file in filelist:
        # ask user for commit message
        msg = str(input('Enter the commit message for ' + file +  ' or enter -r to reject commit'))
        # if msg == -r reject commit
        if(msg == '-r'):
            filelist.remove(file)
            print('commit rejected')
            call('cls', shell=True)
            return False
        # else execute git commit for the file
        #added a comment
        else:
            filelist.remove(file)
            print('git commit -m "' + msg + '"')
            call('cls' , shell=True)
# git push
def push(url , branch):
    call('git push -u ' + url + ' ' + branch)
    #added a comment
