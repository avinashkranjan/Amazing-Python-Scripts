# ALL Imports
from tkinter.ttk import *
import tkinter as tk
from requests import get, HTTPError, ConnectionError
from re import findall
from urllib.parse import unquote


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

    download(link)

    Status["text"] = "Finished!!"
    Status["fg"] = "green"

def download(url):
    block_size = 1024  # 1kB
    r = get(url, stream=True)
    total_size = int(r.headers.get("content-length"))

    with open('video.mp4', 'wb') as file:
        totaldata=0;
        for data in r.iter_content(block_size):
            totaldata+=len(data)
            per_downloaded=totaldata*100/total_size
            bar['value'] = per_downloaded
            file.write(data)
        file.close()    
        print("Download Finished")

    print("Download Complete !!!")

    pass


# GUI

ld_window=tk.Tk()
ld_window.title("Facebook Video Downloader")
ld_window.geometry("400x400")

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
bar['value'] = 0
bar.place(y=200,width=350,x=25)


# Text for Status of Downloading
Status = tk.Label(ld_window, text="Hello!! :D", fg="blue", font=("Calibri", 9), bd=1, relief=tk.SUNKEN, anchor=tk.W, padx=3)
Status.pack(side=tk.BOTTOM, fill=tk.X)

ld_window.mainloop()