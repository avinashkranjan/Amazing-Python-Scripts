import os
from pathlib import Path
import sys

# Taking input
print_string = """
Type Path of the directory
OR
Press enter for running the script on current directory:
OR
Type quit
"""
print(print_string + "\n\n")
input_path = input("Input:")
print("\n\n")

# Script will terminate if input is 'quit'
if input_path == "quit":
    sys.exit(1)

# If nothing is entered then current working directory will be taken as the input path
if input_path == "":
    input_path = os.getcwd()

input_path = Path(input_path)

# Changing the working directory to input path
os.chdir(input_path)

# Creates a dictionary "dic" with key,value pairs where key is extension and value is no. of files with that extension
dic = {}
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        extension = file.split(".")[-1]
        dic[extension] = dic.get(extension, 0) + 1

for key in dic:
    print(f"There are {dic[key]} files  file with extension {key}")
print("\n\n")

# assigning a variable named current Path of current working directory just for simplicity.
# could have used input_path too
current = Path(os.getcwd())
'''
When this script would run the structure of the current directory would change.Hence,
we are assigning list_dir variable the files and dirs in current working directory which the script would modify
'''
list_dir = os.listdir(current)

# keys of dic are extensions of the file
for key in dic:
    # try except block for making directory if it doesn't exists already
    try:
        os.mkdir(key)
    except:
        print(
            f"directory named {key} already exists so it won't be overwrited \n"
        )

    # goes through the files in list_dir
    # we are not using os.listdir() as the directory structure will change during the execution
    for file in list_dir:
        if file.split(".")[-1] == key and os.path.isfile(file):
            # prints absolute path of the file
            print(os.path.abspath(file))
            # Renames the path of the file or moves the file in to the newly created directory
            Path.rename(Path(os.path.abspath(file)),
                        current / Path("./{}/".format(key) + file))

# This block just prints a note and the current structure of the directory

print(
    "\n Script has organised files as per their extensions into different directories! \n"
)
for file in os.listdir(os.getcwd()):
    if not (os.path.isfile(file)):
        print(file)
