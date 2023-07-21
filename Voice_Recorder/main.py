import sounddevice
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter.filedialog import askdirectory

PRIMARY_FONT = ("Comic Sans MS", 18)
SECONDARY_FONT = ("Comic Sans MS", 12)


addr = ""


def file_path():
    global addr
    addr = askdirectory()
    l4["text"] = "Path : \n" + addr
    # print(addr)


def savefile():
    global addr
    global filename
    try:
        time = int(sec.get())
        add = addr + "/" + str(filename.get()) + ".wav"
        showinfo(title="Start", message="Recording started")
        rece = sounddevice.rec(frames=time * 44100,
                               samplerate=44100, channels=2)
        sounddevice.wait()
        write(add, rate=44100, data=rece)
        showinfo(title="End", message="Recording stopped")

    except:
        showwarning(title="Wrong Time", message="Wrong format of time!!!")


def main_window():
    global sec, filename, l4
    win = Tk()
    win.geometry("500x600")
    win.resizable(False, False)
    win.title("Voice Recorder")
    win.config(bg="Lightblue")

    img1 = PhotoImage(file="Images/voice.png")
    l1 = Label(win, image=img1, bg="Lightblue")
    l1.place(x=186, y=20, height=128, width=128)

    l2 = Label(win, text="Time in Sec", font=PRIMARY_FONT, bg="Lightblue")
    l2.place(x=0, y=180, height=50, width=200)

    sec = Entry(win, font=(20))
    sec.place(x=180, y=180, height=50, width=200)

    b = Button(win, text="Select Path", font=SECONDARY_FONT, command=file_path)
    b.place(x=150, y=280, height=50, width=200)

    l4 = Label(
        win, text="Path : Path name here..." + addr, font=SECONDARY_FONT, bg="Lightblue"
    )
    l4.place(x=10, y=330, height=50, width=500)

    img2 = PhotoImage(file="Images/mic.png")

    l3 = Label(text="File name : ", font=PRIMARY_FONT, bg="Gray")
    l3.place(x=60, y=400, height=50, width=150)

    filename = Entry(win, font=(20))
    filename.place(x=210, y=400, height=50, width=250)
    filename.insert(0, "file1")

    start = Button(win, image=img2, bg="Darkgray", command=savefile)
    start.place(x=220, y=480, height=60, width=60)

    win.mainloop()


# savefile(5)
main_window()
