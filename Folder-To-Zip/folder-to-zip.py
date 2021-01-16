import os
import zipfile
from random import randrange


def zip_dir(path, zip_handler):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip_handler.write(os.path.join(root, file))


if __name__ == '__main__':
    to_zip = input("""
Enter the name of the folder you want to zip
(N.B.: The folder name should not contain blank spaces)
>
""")
    to_zip = to_zip.strip() + "/"
    zip_file_name = f'zip{randrange(0,10000)}.zip'
    zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
    zip_dir(to_zip, zip_file)
    zip_file.close()
    print(f'File Saved as {zip_file_name}')
