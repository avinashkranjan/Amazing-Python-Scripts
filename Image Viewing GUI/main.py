# importing the modules

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image viewer')
root.resizable(0, 0)

# fetching the images from the folder
cwd = os.path.dirname(os.path.realpath(__file__))
img_path = os.path.join(cwd, 'images')

# storing the images in a list
images = os.listdir(img_path)
image_list = [Image.open(os.path.join(img_path, image)) for image in images]

my_label = Label(image = image_list[0])
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
