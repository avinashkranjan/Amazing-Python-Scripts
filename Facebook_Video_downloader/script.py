from tkinter import *
import subprocess
import requests
import re
from datetime import datetime
from tqdm import tqdm


def Invalid_URL():
    """ Sets Status bar label to error message """
    Status["text"] = "Invalid URL..."
    Status["fg"] = "red"


def Download_vid():
    """ Validates link and Downloads Video """
    Download_Window.delete("0.0", "end")
    global URL_Val
    url = URL_Val.get()

    Status["text"] = "Downloading in SD quality..."
    Status["fg"] = "green"

    # Validate input
    if not "facebook.com" in url:
        Invalid_URL()
        return
    response = requests.get(url)
    if not response.status_code == 200:
        Invalid_URL()
        response.close()
        return
    response.close()

    video_url = re.search(rf'{url}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    with open(filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()

    Status["text"] = "Finished!!"
    Status["fg"] = "green"


# <----- GUI Code Block Start ----->
gui = Tk()
gui.title("Facebook Video Downloader")
gui.geometry("600x400")

URL_Label = Label(gui, text="Enter Facebook Video URL:", anchor=W, font=("Calibri", 9))
URL_Label.place(x=30, y=20)

URL_Val = StringVar()
Input = Entry(gui, textvariable=URL_Val, font=("Calibri", 9))
Input.place(x=60, y=50, width=400)

button = Button(gui, text="Download", font=("Calibri", 9), command=Download_vid)
button.place(x=250, y=80, width=100)

Download_Window = Text(gui, font=("Calibri", 9), bg="light blue", fg="red", bd=1, relief=SUNKEN, wrap=WORD)
Download_Window.insert(END, "Welcome to Facebook Video Downloader! Provide a Facebook video link in the above box and click download to start the process. ")
Download_Window.place(x=30, y=120, width=530, height=250)

Status = Label(gui, text="Hello!! ", fg="orange", font=("Calibri", 9), bd=1, relief=SUNKEN, anchor=W, padx=3)
Status.pack(side=BOTTOM, fill=X)

gui.mainloop()
