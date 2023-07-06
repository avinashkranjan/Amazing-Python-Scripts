# Imports
import hashlib
import os
import sys
import keyboard


def image_finder(parent_folder):
    # A dictionary to store Hash of Images corresponding to names
    """
    Sample -
    {hash:[names]}
    """
    duplicate_img = {}
    for dirName, subdirs, fileList in os.walk(parent_folder):
        # Iterating over various Sub-Folders
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hash_file(path)
            # Add or append the file path in the dictionary
            if file_hash in duplicate_img:
                duplicate_img[file_hash].append(path)
            else:
                duplicate_img[file_hash] = [path]
    return duplicate_img


def delete_duplicate(duplicate_img):
    # Deleting those values whose keys are not unique
    for key in duplicate_img:
        file_list = duplicate_img[key]
        while len(file_list) > 1:
            item = file_list.pop()
            os.remove(item)


# Joins two dictionaries
def join_dicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


# For finding Hash of various Files
# If 2 files have the same md5checksum,they most likely have the same content
def hash_file(path, blocksize=65536):
    img_file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = img_file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = img_file.read(blocksize)
    img_file.close()
    # Return Hex MD5
    return hasher.hexdigest()


def print_results(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Found Duplicated Images - ')
        print('Details -')
        print('<--------------------->')
        for result in results:
            # Print Path of Files
            for subresult in result:
                print('\t%s' % subresult)
            print('<--------------------->')

    else:
        print('Unable to identify Similar Images')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        duplicate = {}
        folders = sys.argv[1:]
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                # Find the duplicated files and append them to the dictionary
                join_dicts(duplicate, image_finder(i))
            else:
                print('%s is not a valid path, please verify' % i)
                sys.exit()
        print_results(duplicate)
        # Delete Duplicate Images
        # Comment if not required
        print(
            "Do you want to delete the Duplicate Images (If Any)? Press [y] for Yes."
        )
        while True:
            if keyboard.read_key() == "y":
                print("Deleting Duplicate Files\n")
                delete_duplicate(duplicate)
                print("Thank You\n")
                break
            else:
                print("Nothing Deleted!!! Thank You\n")
                break
    else:
        print("Use Command Line Interface")
        print("Hint: python file_finder.py <path of folders>")
        print("Please Read comments for greater detailing")
        '''
        Suggestions :------ 
        Usage - python file_finder.py <path of folder1, path  of folder2, .....>
        folder1 - Parent Folder
        folder2, folder3 .... - Subsequent Folders
        Comparisons are done with in the folder, and from Parent to Subsequent Folders. 

        No Files are deleted form Parent Folder but the files which are Duplicate to the files in Subsequent Folders are
        deleted. Make sure that the paths are correct 
        
        Be careful during Keyboard Input.
        '''
