# THIS IS A PYTHON PROGRAM WITH GUI THAT GENERATES A QR CODE OF THE INPUT 
# THE INPUT CAN BE A TEXT OR A LINK
# THE QR CODE CAN BE SCANNED BY ANY SCANNER APP
# AUTHOR : https://github.com/sagnik-p

from tkinter import *
from tkinter import messagebox
import os
import pyqrcode

#create a GUI window with tkinter
window = Tk()
window.title("QR Code Generator APP")

# a function to generate all widgets
def generate():
    if len(Subject.get()) != 0:
        global qr, photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showerror("Error","Enter subject first")
    try:
        showcode()
    except:
        pass

# a function to show the qr code on the screen
def showcode():
    imageLabel.config(image=photo)
    subLabel.config(text="QR of " + Subject.get())

# A function to save the qr code as a png file
def save():
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0:
            qr.png(os.path.join(dir, name.get() + ".png"), scale=8)
        else:
            messagebox.showerror("Error","Enter file name first")
    except:
        messagebox.showerror("Error","Generate the QR code first")

# specifying all details for the widgets
Sub = Label(window, text="Enter URL/Subject")
Sub.grid(row=0, column=0, sticky=N + S + W + E)

FName = Label(window, text="Enter filename to save as")
FName.grid(row=1, column=0, sticky=N + S + W + E)

Subject = StringVar()
SubEntry = Entry(window, textvariable=Subject)
SubEntry.grid(row=0, column=1, sticky=N + S + W + E)

name = StringVar()
nameEntry = Entry(window, textvariable=name)
nameEntry.grid(row=1, column=1, sticky=N + S + W + E)

button = Button(window, text="Generate QR Code", width=15, command=generate)
button.grid(row=0, column=3, sticky=N + S + W + E)

imageLabel = Label(window)
imageLabel.grid(row=2, column=1, sticky=N + S + W + E)

subLabel = Label(window, text="")
subLabel.grid(row=3, column=1, sticky=N + S + W + E)

saveB = Button(window, text="Save as PNG File", width=15, command=save)
saveB.grid(row=1, column=3, sticky=N + S + W + E)

Rows = 3
Columns = 3

for row in range(Rows + 1):
    window.grid_rowconfigure(row, weight=1)

for col in range(Columns + 1):
    window.grid_columnconfigure(col, weight=1)

# let the program run forever untill manually closed by the user
window.mainloop()