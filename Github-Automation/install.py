from shutil import copy, copyfile
import os
dir = os.getcwd()

files = [
    file for file in os.listdir(dir)
    if file.endswith('.py') and file != 'install.py'
]
files.append('tmp.json')
print(files)


def checkForIgnore(dst):
    return os.path.isfile(os.path.join(dst, '.gitignore'))


def addToIgnore(dst):
    with open(os.path.join(dst, '.gitignore'), "a") as f:
        f.write('\nauto-scripts\n.idea\n__pycache__\n.git')
        f.close()


def makeIgnore(dst):
    f = open(os.path.join(dst, '.gitignore'), "x")
    f.write('auto-scripts\n.idea\n__pycache__\n.git')
    f.close()


def copyfiles(file: str, dst: str):
    copy(file, dst)
    print('Installation Successful\n')


def installfiles():
    location = input('Enter installation directory: ')
    if (checkForIgnore(location)):
        print('.gitignore found')
        addToIgnore(location)
    else:
        print('.gitignore not found, creating one')
        makeIgnore(location)
    os.makedirs(os.path.join(location, 'auto-scripts'))
    location = os.path.join(location, 'auto-scripts')
    print('Installing Files')
    for file in files:
        print('Installing %s' % file)
        copyfiles(file, location)


installfiles()
