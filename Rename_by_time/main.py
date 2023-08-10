import os
from math import log10

files = os.listdir(".")

files.sort(key=lambda x: os.path.getmtime(x))
# print(files) # list index 0 hold the oldest file
digits = int(log10(len(files)))+1

print(f"\nPlease verify the new file names for accuracy: press 'p' to review the file names, or 'y'/'Y' to proceed with the renaming process. Press any other key to exit the program.\n")
n = input()

if (n == "y" or n == "Y" or n == "p"):
    rename, hidden = 0, 0
    for i in range(len(files)-1):

        oldname = files[i]

        if (files[i][0] == "."):
            hidden += 1
            continue

        if "_" in files[i] and files[i][0] != "_":
            index = files[i].find("_")
            isNum = files[index-1]

            if (isNum >= "0" and isNum <= "9"):
                tempOld = files[i][index+1:]
            else:
                tempOld = files[i]
        else:
            tempOld = files[i]

        rename += 1
        newfile_name = f"{str(rename).zfill(digits)}_{tempOld}"

        if (n == "p"):
            print(f"{tempOld} --> {newfile_name}")
        else:
            os.rename(oldname, newfile_name)

    print(
        f"\nNumber of hidden files are {hidden}. For safety purpose, they will be kept unchanged.")

else:
    print("File renaming cancel.")
    exit(0)

if n == "y" or n == "Y":
    print("\nFile renaming successful.")
