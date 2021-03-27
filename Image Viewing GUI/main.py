# importing the modules

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image viewer')
root.resizable(0, 0)

# opening the images from the image folder
img1 = Image.open("./Image Viewing GUI/images/img1.jpg")
img2 = Image.open("./Image Viewing GUI/images/img2.jpg")
img3 = Image.open("./Image Viewing GUI/images/img3.jpg")
img4 = Image.open("./Image Viewing GUI/images/img4.jpg")
img5 = Image.open("./Image Viewing GUI/images/img5.jpg")

# resizing the images
resized_img1 = img1.resize((500, 500), Image.ANTIALIAS)
resized_img2 = img2.resize((500, 500), Image.ANTIALIAS)
resized_img3 = img3.resize((500, 500), Image.ANTIALIAS)
resized_img4 = img4.resize((500, 500), Image.ANTIALIAS)
resized_img5 = img5.resize((500, 500), Image.ANTIALIAS)

new_pic1 = ImageTk.PhotoImage(resized_img1)
new_pic2 = ImageTk.PhotoImage(resized_img2)
new_pic3 = ImageTk.PhotoImage(resized_img3)
new_pic4 = ImageTk.PhotoImage(resized_img4)
new_pic5 = ImageTk.PhotoImage(resized_img5)

# creating a list of all the images
image_list = [new_pic1,new_pic2,new_pic3,new_pic4,new_pic5]

my_label = Label(image = new_pic1)
my_label.grid(row = 0, column = 0, columnspan = 3)

# defining a function to show the previous image
def back(image_num):
    global my_label
    global back_btn
    global next_btn

    my_label.grid_forget()
    my_label = Label(image = image_list[image_num - 1])

    next_btn = Button(root, text = "next", command = lambda:next(image_num + 1))
    back_btn = Button(root, text = "back", command = lambda: back(image_num - 1))


    if(image_num == 1):
        back_btn = Button(root, text = "back", state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    back_btn.grid(row = 1, column = 0)
    next_btn.grid(row = 1, column = 2)

# defining a function to show the next image
def next(image_num):
    global my_label
    global back_btn
    global next_btn

    my_label.grid_forget()
    my_label = Label(image = image_list[image_num - 1])

    next_btn = Button(root, text = "next", command = lambda:next(image_num + 1))
    back_btn = Button(root, text = "back", command = lambda: back(image_num - 1))

    if(image_num == len(image_list)):
        next_btn = Button(root, text = "next", state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    back_btn.grid(row = 1, column = 0)
    next_btn.grid(row = 1, column = 2)

back_btn = Button(root, text = "back", command = back, state = DISABLED)
next_btn = Button(root, text = "next", command = lambda:next(2))

back_btn.grid(row = 1, column = 0)
next_btn.grid(row = 1, column = 2)

# creating the mainloop
root.mainloop()
