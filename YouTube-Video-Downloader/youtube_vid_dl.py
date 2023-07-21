from tkinter import *
from pytube import YouTube
from pytube import Playlist

# select wether to download video or playlist


def mode_selector():
    url = link.get()
    if "watch?v=" in url:
        video_downloader(url)
    elif "playlist?list=" in url:
        playlist_downloader(url)
    else:
        print("Invalid YouTube URL!")
    Label(root, text='DOWNLOADED!', font='arial 15').place(x=280, y=230)

# function to download single video


def video_downloader(url):
    try:
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        yt.streams.first().download()
    except Exception as e:
        Label(root, text=f'Video Error Downloading!.... Try Again #{e}', font='arial 15').place(
            x=100, y=210)

# function to download playlist


def playlist_downloader(url):
    try:
        py = Playlist(url)
        for video in py.videos:
            video_downloader(video.watch_url)
    except Exception as e:
        Label(root, text=f'Playlist Error Downloading!.... Try Again #{e}', font='arial 15').place(
            x=100, y=210)
        print(e)


if __name__ == "__main__":
    root = Tk()
    root.geometry('800x600')
    root.resizable(0, 0)
    root.title("YouTube Video Downloader")

    Label(root, text='Copy the link of the VIDEO/PLAYLIST you want to download from YouTube',
          font='arial 15 bold').pack()

    # enter link
    link = StringVar()

    Label(root, text='Paste Link Here:',
          font='arial 15 bold').place(x=270, y=60)
    Entry(root, width=80, textvariable=link).place(x=32, y=90)
    Button(root, text='DOWNLOAD', font='arial 15 bold', bg='white',
           padx=2, command=mode_selector).place(x=280, y=150)

    root.mainloop()
