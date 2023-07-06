from shutil import copy, copyfile
import os
print(dir)
files = ['filechange.py', 'main.py']


def copyfiles(file: str, dst: str):
    copy(file, dst)
    print('Installation Successful\n')


def installfiles():
    location = input('Enter installation directory: ')
    print('Installing Files')
    for file in files:
        print('Installing %s' % file)
        copyfiles(file, location)


installfiles()
