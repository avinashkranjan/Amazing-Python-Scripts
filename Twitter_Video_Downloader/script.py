from tkinter import *
import subprocess
import requests


def Invalid_URL():
    """ Sets Status bar label to error message """
    Status["text"] = "Invalid URL..."
    Status["fg"] = "red"


def Download_vid():
    """ Validates link and Downloads Video """
    Download_Window.delete("0.0", "end")
    global URL_Val
    url = URL_Val.get()

    Status["text"] = "Downloading..."
    Status["fg"] = "green"

    # Validate input
    if not "twitter.com" in url:
        Invalid_URL()
        return
    response = requests.get(url)
    if not response.status_code == 200:
        Invalid_URL()
        response.close()
        return
    response.close()

    with subprocess.Popen("youtube-dl {} --no-cache-dir".format(url), stdout=subprocess.PIPE, shell=True, universal_newlines=True) as Process:
        for line in Process.stdout:
            Download_Window.insert(END, line)
            main.update_idletasks()

    Status["text"] = "Finished!!"
    Status["fg"] = "green"


# <----- GUI Code Block Start ----->
main = Tk()
main.title("Twitter Video Downloader")
main.geometry("600x400")

URL_Label = Label(main, text="Enter Twitter Video URL:",
                  anchor=W, font=("Calibri", 9))
URL_Label.place(x=30, y=20)

URL_Val = StringVar()
URL_Input = Entry(main, textvariable=URL_Val, font=("Calibri", 9))
URL_Input.place(x=60, y=50, width=400)

Download_button = Button(main, text="Download", font=(
    "Calibri", 9), command=Download_vid)
Download_button.place(x=250, y=80, width=100)

Download_Window = Text(main, font=("Calibri", 9), bg="black",
                       fg="white", bd=1, relief=SUNKEN, wrap=WORD)
Download_Window.insert(
    END, "Welcome to Twitter Video Downloader, Provide a Twitter video link in the above box and click download to start the process. :D")
Download_Window.place(x=30, y=120, width=530, height=250)

Status = Label(main, text="Hello!! :D", fg="orange", font=(
    "Calibri", 9), bd=1, relief=SUNKEN, anchor=W, padx=3)
Status.pack(side=BOTTOM, fill=X)

main.mainloop()
# <----- GUI Code Block End ----->
