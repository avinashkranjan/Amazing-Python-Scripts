
import difflib

def getMaxSpaces(file):
    max = float('-inf')
    for ele in file:
        ele = ele.strip()
        if(len(ele) > max):
            max = len(ele)
    return max

def calcDiff(firstFile , secondFile):
    diff = difflib.ndiff(firstFile , secondFile)
    deltainit = ''.join(x[2:] for x in diff if x.startswith('+ '))
    deltainit = deltainit.split('\n')
    maxspacesinit = getMaxSpaces(deltainit)
    print('CHANGED LINES ARE:-\n' , '-' * maxspacesinit)
    for ele in deltainit:
        print(str(ele.strip()) , ' ' * (maxspacesinit - len(ele.strip())), '+|')
    print('' , '-' * maxspacesinit)
    