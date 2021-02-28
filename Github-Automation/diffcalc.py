from colors import logcolors
from difflib import ndiff
from utils import getMaxSpaces


def calcDiff(firstFile, secondFile):
    # calculate raw diff
    diff = ndiff(firstFile, secondFile)
    # calculate unique lines in secondfile
    deltainit = ''.join(x[2:] for x in diff if x.startswith('+ '))
    # reformat the lines
    deltainit = deltainit.split('\n')
    maxspacesinit = getMaxSpaces(deltainit)
    print(f'{logcolors.BOLD}CHANGED LINES ARE{logcolors.ENDC}\n',
          f'{logcolors.BOLD}-{logcolors.ENDC}' * maxspacesinit)

    for ele in deltainit:
        print(f'{logcolors.SUCCESS} {str(ele.strip())} {logcolors.ENDC}',
              ' ' * (maxspacesinit - len(ele.strip())), '+')

    print('', f'{logcolors.BOLD}-{logcolors.ENDC}' * maxspacesinit)
    return deltainit
