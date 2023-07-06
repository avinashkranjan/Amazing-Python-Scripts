import os
import time
from os import listdir
from os.path import isfile, join
print("ENTER THE PATH TO FOLDER")
path = input()
files_list = [f for f in listdir(path) if isfile(join(path, f))]
for k in files_list:
    print(k)
    access_time = os.path.getatime(path + "\\" + k)
    local_time = time.ctime(access_time)
    print("Last access time(Local time):", local_time)
