# ALL Imports

import tkinter as tk
import requests as req
import html
import time
from tkinter.ttk import *
from threading import Thread
import queue
from queue import Empty


def Invalid_Url():
    """ Sets Status bar label to error message """
    Status["text"] = "Invalid URL..."
    Status["fg"] = "red"


def Download_vid():

    # Validates Link and download Video
    global Url_Val
    url=Url_Val.get()

    Status["text"]="Downloading"
    Status["fg"]="green"


    # Validating Input

    if not "linkedin.com/posts" in url:
        Invalid_Url()
        return

    response =req.get(url)

    if not response.status_code == 200:
        Invalid_Url()
        return       

    htmlsource = response.text

    sources = html.unescape(htmlsource).split()

    for source in sources:

        if "dms.licdn.com" in source:

            videourl = source.split(',')[0].split('"src":')[1][1:-1]
            start_downloading()

            download_thread=VideoDownload(videourl)
            download_thread.start()
            monitor(download_thread)
            break  


class VideoDownload(Thread):
    
    def __init__(self, url):
        super().__init__()

        self.url = url

    def run(self):
        """ download video"""

        # save the picture to a file
        block_size = 1024  # 1kB
        r = req.get(self.url, stream=True)
        total_size = int(r.headers.get("content-length"))

        with open('video.mp4', 'wb') as file:
            totaldata=0;
            for data in r.iter_content(block_size):
                totaldata+=len(data)
                per_downloaded=totaldata*100/total_size
                queue.put(per_downloaded)
                bar['value'] = per_downloaded
                file.write(data)
                time.sleep(0.01)
            file.close()    
            print("Download Finished")

        print("Download Complete !!!")
        Status["text"] = "Finished!!"
        Status["fg"] = "green"


#start download
def start_downloading():
   bar["value"]=0;

def monitor( download_thread):
    """ Monitor the download thread """
    if download_thread.is_alive():

        try:
            bar["value"]=queue.get(0)
            ld_window.after(10, lambda: monitor(download_thread))
        except Empty:
            pass

# GUI

ld_window=tk.Tk()
ld_window.title("Linkedin Video Downloader")
ld_window.geometry("400x300")

# Label for URL Input
input_label= tk.Label(ld_window,text="Enter Linkedin Video URL:")
input_label.pack()

queue=queue.Queue()

# Input of URL
Url_Val = tk.StringVar()
Url_Input = tk.Entry(ld_window, textvariable=Url_Val, font=("Calibri", 9))
Url_Input.place( x=25,y=50, width=350)

# Button for Download
Download_button = tk.Button(ld_window, text="Download", font=("Calibri", 9), command=Download_vid)
Download_button.place(x=100, y=100, width=200)

# Progress Bar
bar = Progressbar(ld_window, length=350, style='grey.Horizontal.TProgressbar',mode='determinate')
bar.place(y=200,width=350,x=25)


# Text for Status of Downloading
Status = tk.Label(ld_window, text="Hello!! :D", fg="blue", font=("Calibri", 9), bd=1, relief=tk.SUNKEN, anchor=tk.W, padx=3)
Status.pack(side=tk.BOTTOM, fill=tk.X)

ld_window.mainloop() 