# searching_specific_files.py

import fnmatch
import os

root_path = '/home/tuts/Documents'
_pattern = '*.mp4'

for _root, dirs, _files in os.walk(root_path):
for _file in fnmatch.filter(_files, _pattern):
print( os.path.join(_root, _file))