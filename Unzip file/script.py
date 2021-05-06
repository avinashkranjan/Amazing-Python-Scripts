import zipfile

target = input(r"Enter file to be unzipped: ")
handle = zipfile.ZipFile(target)
handle.extractall("./Unzip file/Unzip files")
handle.close()
