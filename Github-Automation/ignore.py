import os

cwd = os.getcwd()
ignorepath = os.path.join(cwd, '.gitignore')


def getIgnoreFiles():
    ignorefiles = []
    with open(ignorepath) as ignore:
        files = ignore.readlines()
        for file in files:
            file = ''.join(file.splitlines())
            if (file != ''):
                filepath = os.path.join(cwd, file)
                if (os.path.isfile(filepath) or os.path.isdir(filepath)):
                    ignorefiles.append(file)
    return ignorefiles
