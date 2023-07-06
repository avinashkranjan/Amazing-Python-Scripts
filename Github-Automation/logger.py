import json
import os
from colors import logcolors
import filechange
jsonpath = os.path.join(os.getcwd(), 'auto-scripts', 'tmp.json')
buffer = []


def writedata(*args, **kwargs):
    data = {}
    global buffer
    updatedbuffer = kwargs.get('buffer', -1)
    path = kwargs.get('path', None)
    diff = kwargs.get('diff', None)
    if (updatedbuffer != -1):
        buffer = updatedbuffer
        with open(jsonpath, 'w') as file:
            json.dump([obj for obj in buffer], file, indent=4)
    elif (path and diff):
        data['path'] = path
        data['changes'] = diff
        buffer.append(data)
        with open(jsonpath, 'w') as file:
            json.dump([obj for obj in buffer], file, indent=4)


def updatedata(filename, diffarr):
    if (os.path.getsize(jsonpath) > 0):
        with open(jsonpath, 'r') as file:
            readdata = json.load(file)
        if (len(readdata) == 0):
            print('No changed file left')
        else:
            tmpdata, tmpfile, tmpdiff = readdata.copy(), filename.copy(
            ), diffarr.copy()
            print('Found some changed files')
            for file, diff in zip(filename, diffarr):
                print(f'Removing {str(file)} from json file')
                for obj in readdata:
                    if obj['path'] == file and obj['changes'] == diff:
                        tmpdata.remove(obj)
                        tmpfile.remove(file)
                        tmpdiff.remove(diff)
            # make the original lists empty without changing address
            del filename[:], diffarr[:]
            writedata(buffer=tmpdata)

    else:
        print('No data to read')


def checkdata(url, branch):
    if (os.path.getsize(jsonpath) > 0):
        with open(jsonpath, 'r') as file:
            initdata = json.load(file)
        if (len(initdata) == 0):
            print(f'{logcolors.SUCCESS}Change tree clean{logcolors.ENDC}')
        else:
            filechange.ischanged(url, branch, initbuffer=initdata)
    else:
        print(
            f'{logcolors.ERROR}No changes found from previous session{logcolors.ENDC}'
        )
