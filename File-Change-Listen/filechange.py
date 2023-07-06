import os
from os import listdir
from os.path import isfile, join
import time
mypath = os.getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


def read_file():
    filecontent = []
    for file in onlyfiles:
        with open(onlyfiles[onlyfiles.index(file)], "r") as f:
            filecontent.append(f.readlines())
    return filecontent


def ischanged():
    changedfile = []
    print('Listening for changes....')
    initial = list(read_file())
    while True:
        current = list(read_file())
        changeditem = []
        previtem = []
        if (current != initial):

            for ele in initial:
                if ele not in current:
                    for item in ele:
                        previtem.append(item)
            for ele in current:
                if ele not in initial:
                    changeditem.append(ele)

            # changedDiff = list(set(changeditem[0]) - set(previtem))
            # prevDiff = list(set(previtem) - set(changeditem[0]))
            for i in range(0, len(changeditem)):
                print('loop :-', i)
                changedfile.append(onlyfiles[current.index(changeditem[i])])
            print('Changed file is:-', changedfile)
            # print('changed lines are:- ' ,prevDiff,' -> ',changedDiff)
            initial = current
