"""
    File Downloader

        This python script will help users to download any kind of files, irrespective of their size from the internet.<br>
        You just need to have the url and you are good to go!
"""
import os
import requests
from tqdm import tqdm
import math
import time

url=input("Enter the url of the file you want to download: ")

r=requests.get(url)
#receives data from the url

file_size=int(r.headers['Content-Length'])
chunk_size=256

"""Chunk size is the
number of bytes downloaded at a time
"""

r=requests.get(url,stream=True)

"""streams=True ensures that
will not get data at once, but will get data one by one

"""

extension=(os.path.splitext(url))[-1]
file="file"+extension

iterations=math.ceil(file_size/chunk_size)

with open(file, "wb") as file:
	for chunk in tqdm(r.iter_content(chunk_size=chunk_size),total=iterations):
		time.sleep(0.5)
		file.write(chunk)
