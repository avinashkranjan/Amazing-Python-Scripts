# ALL Imports
import time
from tkinter.ttk import *
import tkinter as tk
from requests import get, HTTPError, ConnectionError
from re import findall
from urllib.parse import unquote
from threading import Thread
import queue
from queue import Empty

def Invalid_Url():
    """ Sets Status bar label to error message """
    Status["text"] = "Invalid URL..."
    Status["fg"] = "red"

def get_downloadlink(url):

    url = url.replace("www", "mbasic")
    try:
        r = get(url, timeout=5, allow_redirects=True)
        if r.status_code != 200:
            raise HTTPError
        a = findall("/video_redirect/", r.text)
        if len(a) == 0:
            print("[!] Video Not Found...")
            exit(0)
        else:
            return unquote(r.text.split("?src=")[1].split('"')[0])
    except (HTTPError, ConnectionError):
        print("[x] Invalid URL")
        exit(1)



def Download_vid():

    # Validates Link and download Video
    global Url_Val
    url=Url_Val.get()

    Status["text"]="Downloading"
    Status["fg"]="green"


    # Validating Input

    if not "www.facebook.com" in url:
        Invalid_Url()
        return

    link=get_downloadlink(url)

    start_downloading()

    download_thread=VideoDownload(link)
    download_thread.start()
    monitor(download_thread)



def monitor( download_thread):
    """ Monitor the download thread """
    if download_thread.is_alive():

        try:
            bar["value"]=queue.get(0)
            ld_window.after(10, lambda: monitor(download_thread))
        except Empty:
            pass



class VideoDownload(Thread):

    def __init__(self, url):
        super().__init__()

        self.url = url

    def run(self):
        """ download video"""

        # save the picture to a file
        block_size = 1024  # 1kB
        r = get(self.url, stream=True)
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

# GUI

ld_window=tk.Tk()
ld_window.title("Facebook Video Downloader")
ld_window.geometry("400x300")

# Label for URL Input
input_label= tk.Label(ld_window,text="Enter Facebook Video URL:")
input_label.pack()

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

queue=queue.Queue()
# Text for Status of Downloading
Status = tk.Label(ld_window, text="Hello!! :D", fg="blue", font=("Calibri", 9), bd=1, relief=tk.SUNKEN, anchor=tk.W, padx=3)
Status.pack(side=tk.BOTTOM, fill=tk.X)

ld_window.mainloop() 