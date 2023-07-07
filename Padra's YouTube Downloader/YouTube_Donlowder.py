from pytube import YouTube
from tkinter import *
from pytube.cli import on_progress
# Asking for all the video links
n = int(input("Enter the number of youtube videos you want to download:"))
# A list to store all the links
links = []
# Asking for the links one per line
print("\nEnter every one of the links in individual line:")
for i in range(0, n):
    temp = input()
    links.append(temp)
# Showing all details for videos and downloading them one by one
for i in range(0, n):
    link = links[i]
    yt = YouTube(link, on_progress_callback=on_progress)
    print(yt)
    print("\nDetails for Video", i+1, "\n")
    print("Video's Title:   ", yt.title)
    print("Number of views:  ", yt.views)
    print("video's Length:  ", yt.length, "seconds")

    # Filter to select only progressive streams
    stream = str(yt.streams.filter(progressive=True))
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    print("\nAll available options for downloads:\n")

    # loop around all available streams and print them for user to decide
    for i in range(0, len(streamlist)):
        st = streamlist[i].split(" ")
        print(i+1, ") ", st[1], " and ", st[3], sep='')

    # ask user the tag forthe stream to download

    '''
    272: webm video 2880p/4320p
    94: mp4 video 144p
    395: mp4 video 240p
    396: mp4 video 360p
    397: mp4 video 480p
    398: mp4 video 720p
    399: mp4 video 1080p
    400: mp4 video 1440p
    401: mp4 video 2160p
    402: mp4 video 2880p
    298: mp4 video 720p60
    299: mp4 video 1080p60
    '''

    tag = int(input("\nEnter the itag of your preferred stream to download:   "))
    ys = yt.streams.get_by_itag(tag)
    print("\nDownloading...")

    ys.download()
    print("\nDownload completed :)")
    print()
