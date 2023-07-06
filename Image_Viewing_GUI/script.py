from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry("600x600")


def resize_image(root, copy_image, label1):
    new_height = 600
    new_width = 600
    image = copy_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label1.configure(image=photo)
    label1.image = photo


def next():
    global n
    global itemslist
    n = (n+1) % len(itemslist)
    img1 = itemslist[n]

    image = Image.open(path+"/"+img1)
    copy_image = image.copy()
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.bind('<configure>', resize_image(root, copy_image, label1))
    label.pack()


def previous():
    global n
    global itemslist
    n = (n-1) % len(itemslist)
    img1 = itemslist[n]

    image = Image.open(path+"/"+img1)
    copy_image = image.copy()
    photo = ImageTk.PhotoImage(image)

    label2 = Label(root, image=photo)
    label2.bind('<configure>', resize_image(root, copy_image, label1))
    label2.pack()


n = 0
path = input(r"Enter path for the image folder: ")
itemslist = os.listdir(path)
img1 = itemslist[n]

image = Image.open(path+"/"+img1)
copy_image = image.copy()
photo = ImageTk.PhotoImage(image)

label1 = Label(root, image=photo)
label1.bind('<configure>', resize_image(root, copy_image, label1))
label1.pack()

btn1 = Button(root, text="next", width=5, height=10, command=next)
btn1.place(x=570, y=150)

btn1 = Button(root, text="prev", width=5, height=10, command=previous)
btn1.place(x=0, y=150)

root.mainloop()
