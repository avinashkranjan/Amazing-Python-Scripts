# ALL Imports

import tkinter as tk
import requests as req
import html


def Invalid_Url():
    """ Sets Status bar label to error message """
    Download_Window.insert(tk.END,f"Invalid URL")
    Status["text"] = "Invalid URL..."
    Status["fg"] = "red"


def Download_vid():

    # Validates Link and download Video
    Download_Window.delete("0.0", "end")
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

            r = req.get(videourl, stream=True)

            total_size = int(r.headers.get('content-length', 0))

            block_size = 1024  

            with open('video.mp4', 'wb') as file:
                totaldata=0;
                for data in r.iter_content(block_size):
                    totaldata+=len(data)
                    per_downloaded=totaldata*100/total_size
                    Download_Window.delete("1.0","end")
                    Download_Window.insert(tk.END,f"Dowloaded.... {per_downloaded}%")
                    file.write(data)
                print("Download Finished")
            break  

    Status["text"] = "Finished!!"
    Status["fg"] = "green"


# GUI

ld_window=tk.Tk()
ld_window.title("Linkedin Video Downloader")
ld_window.geometry("400x400")

# Label for URL Input
input_label= tk.Label(ld_window,text="Enter Linkedin Video URL:")
input_label.pack()

# Input of URL
Url_Val = tk.StringVar()
Url_Input = tk.Entry(ld_window, textvariable=Url_Val, font=("Calibri", 9))
Url_Input.place( x=25,y=50, width=350)

# Button for Download
Download_button = tk.Button(ld_window, text="Download", font=("Calibri", 9), command=Download_vid)
Download_button.place(x=100, y=100, width=200)

# Download Window

Download_Window = tk.Text(ld_window, font=("Calibri", 9), bg="black", fg="white", bd=1, relief=tk.SUNKEN, wrap=tk.WORD)
Download_Window.insert(tk.END, "Welcome to Linkedin Video Downloader, Provide a Linkedin post link in the above box and click download to start the process. :D")
Download_Window.place(x=25, y=200, width=350, height=250)

# Text for Status of Downloading
Status = tk.Label(ld_window, text="Hello!! :D", fg="blue", font=("Calibri", 9), bd=1, relief=tk.SUNKEN, anchor=tk.W, padx=3)
Status.pack(side=tk.BOTTOM, fill=tk.X)

ld_window.mainloop() 