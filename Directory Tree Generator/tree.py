import os
import argparse
from datetime import datetime


def realname(path, root=None):
    """Return the real name of a path, including symbolic links."""
    if root is not None:
        path = os.path.join(root, path)
    result = os.path.basename(path)
    if os.path.islink(path):
        realpath = os.readlink(path)
        result = f'{os.path.basename(path)} -> {realpath}'
    return result


def get_file_info(path, root=None):
    """Return the file information including size and modification timestamp."""
    if root is not None:
        path = os.path.join(root, path)
    size = os.path.getsize(path)
    modified = os.path.getmtime(path)
    modified_time = datetime.fromtimestamp(
        modified).strftime('%Y-%m-%d %H:%M:%S')
    return f'{realname(path, root=root)} (Size: {size} bytes, Modified: {modified_time})'


def ptree(startpath, depth=-1):
    """Generate the directory tree structure starting from the given path."""
    assert os.path.isdir(startpath), "Directory not valid"
    if startpath != '/':
        if startpath.endswith('/'):
            startpath = startpath[:-1]

    for root, dirs, files in os.walk(startpath):
        level = root.count(os.sep) - startpath.count(os.sep)
        if depth > -1 and level > depth:
            continue

        indent = '|   ' * level + '|-- '
        print(f'{indent}{realname(root)}/')

        for d in dirs:
            if os.path.islink(os.path.join(root, d)):
                print(f'{indent}|   {realname(d, root=root)}')

        for f in files:
            print(f'{indent}|   {get_file_info(f, root=root)}')


if __name__ == '__main__':
    print("\nDirectory tree\n")

    parser = argparse.ArgumentParser(description='Prints directory tree.')
    parser.add_argument('startpath', type=str,
                        help='Path to starting directory')
    parser.add_argument('-d', '--depth', type=int, default=-
                        1, help='Depth of the directory tree')
    args = parser.parse_args()

    ptree(args.startpath, args.depth)

    input("\n\nPress enter to exit")
