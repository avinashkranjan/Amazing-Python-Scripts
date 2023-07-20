from tkinter import *
from PIL import ImageTk, Image
import os


def rotate_image():
    global counter
    img_label.config(image=img_array[counter % len(img_array)])
    counter = counter+1


counter = 1
root = Tk()
root.title('Wallpaper viewer')
root.minsize(250, 400)
root.configure(background='black')
# img = Image.open('wallpaper/Screenshot_20210215-182223_Truecaller.jpg')
files = os.listdir(r'.\wallpaper')
# files = os.listdir('.')
img_array = []
for file in files:
    img = Image.open(os.path.join(r'.\wallpaper', file))
    resized_img = img.resize((250, 300))
    img_array.append(ImageTk.PhotoImage(resized_img))
img_label = Label(root, image=img_array[0])
img_label.pack(pady=(15, 10))

next_btn = Button(root, text='Next', bg='white', fg='black',
                  width=25, height=2, command=rotate_image)


next_btn.pack()
root.mainloop()
