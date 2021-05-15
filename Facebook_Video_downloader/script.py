import re
import requests
import urllib.request
from tqdm import tqdm

video_link = input("Enter the video link: ")

req = requests.get(video_link, stream=True)

print("downloading......")
urllib.request.urlretrieve(video_link,"Facebook Video.mp4")
print("Downloaded successfully")
