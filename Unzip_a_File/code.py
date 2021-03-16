---
#Project Name -> Unzip a File using Python
#Author -> Priya Mondal
---

#What is a ZIP File? -> ZIP is a archive file format that supports losless data compression.
# A ZIP file may contain one or more files or directories that may have been compressed.
#Helps to reduce the file size
#Helps to keep the data in one place
# Faster than the general files we use, over many connections.
# Module used -> zipfile

import zipfile as z

target = 'demo.zip'

print('Starting to unzip the file...')

root = z.ZipFile(target)

#A folder being created named 'new' and acts as the destination for the unzipped file.
root.extractall('new')

root.close()

print("\nFile is succesfully Unzipped!")
