# Directory Tree Generator

import os
import argparse


def realname(path, root=None):
    if root is not None:
        path = os.path.join(root, path)
    result = os.path.basename(path)
    if os.path.islink(path):
        realpath = os.readlink(path)
        result = '%s -> %s' % (os.path.basename(path), realpath)
    return result


def ptree(startpath, depth=-1):
    prefix = 0
    assert os.path.isdir(startpath), "Directory not valid"
    if startpath != '/':
        if startpath.endswith('/'):
            startpath = startpath[:-1]
        prefix = len(startpath)
    for root, dirs, files in os.walk(startpath):
        level = root[prefix:].count(os.sep)
        if depth > -1 and level > depth:
            continue
        indent = subindent = ''
        if level > 0:
            indent = '|   ' * (level-1) + '|-- '
        subindent = '|   ' * (level) + '|-- '
        print('{}{}/'.format(indent, realname(root)))

        for d in dirs:
            if os.path.islink(os.path.join(root, d)):
                print('{}{}'.format(subindent, realname(d, root=root)))
        for f in files:
            print('{}{}'.format(subindent, realname(f, root=root)))


if __name__ == '__main__':

    print("\nDirectory tree \n")

    parser = argparse.ArgumentParser(description='prints directory tree.')
    parser.add_argument('startpath', type=str,
                        help='path to stating directory')
    args = parser.parse_args()
    argsd = vars(args)
    ptree(**argsd)

    input("\n\nPress enter to exit")
