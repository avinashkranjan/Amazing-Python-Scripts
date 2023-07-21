# import OS module
import os
# provide path
path = "H:\gulshan_jakhon\Gulshan_jakhon"


print("===================")
print("Contain Folders:")
print("===================")
# Access subdirectories using os.listdir
path = 'H:\gulshan_jakhon\Gulshan_jakhon'
for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
        print(entry)


print("===================")
print("Contain Files:")
print("===================")


# to store files in a list
list = []

# dirs=directories
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.txt' in f:
            print(f)
