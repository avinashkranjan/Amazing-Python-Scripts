from shutil import copy , copyfile
import os
dir = os.getcwd()
files = []
# files = ['diffcalc.py' , 'main.py' , 'filechange.py' , 'gitcommands.py' , 'repoInfo.py']
for file in os.listdir(dir):
    if(file.endswith('.py') and file != 'install.py'):
        files.append(file)
print(files)
def copyfiles(file:str , dst:str):
    copy(file , dst)
    print('Installation Successful\n')

def installfiles():
    location = input('Enter installation directory: ')
    print('Installing Files')
    for file in files:
        print('Installing %s' % file)
        copyfiles(file , location)

installfiles()