import difflib

def calcDiff(firstFile , secondFile):
    diff = difflib.ndiff(firstFile , secondFile)
    delta = ''.join(x[2:] for x in diff if x.startswith('+ '))
    deltaNoSpace = delta.split('\n')
    print('CHANGED LINES ARE:-\n-----------------')
    for ele in deltaNoSpace:
        print(ele.strip())
    print('-----------------\n')
