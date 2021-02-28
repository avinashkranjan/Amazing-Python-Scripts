import numpy as np
import matplotlib.pyplot as plt
import tensorflow.keras as keras
#from keras.layers import *
#from keras.models import *
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tkinter import filedialog
import tkinter as tk

window = tk.Tk()
window.title("Detection of Covid-19 Using X-Ray")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'

window.geometry('1280x720')

window.configure(background='yellow')

#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window,
                   text="Detection of Covid-19 Using X-Ray",
                   bg="orange",
                   fg="white",
                   width=50,
                   height=3,
                   font=('times', 30, 'italic bold underline'))
message.place(x=200, y=20)

#txt = tk.Entry(window,width=20  ,bg="blue" ,fg="red",font=('times', 15, ' bold '))
#txt.place(x=700, y=215)

lbl3 = tk.Label(window,
                text="Status of a Person : ",
                width=20,
                fg="red",
                bg="green",
                height=2,
                font=('times', 15, ' bold underline '))
lbl3.place(x=400, y=400)

message = tk.Label(window,
                   text="",
                   bg="blue",
                   fg="red",
                   width=30,
                   height=2,
                   activebackground="yellow",
                   font=('times', 15, ' bold '))
message.place(x=700, y=400)


# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(224, 224))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img


# load an image and predict the class


def run_example():
    # load the image
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select file",
                                          filetypes=(("*.jpeg", "*.jpg"),
                                                     ("all files", "*.*")))
    img = load_image(filename)
    # load model
    model = load_model('model_adv.h5')
    # predict the class
    result = model.predict(img)

    run_example.num = result[0]
    print(result[0])
    if (run_example.num == 0.):
        res = "Covid_19"
        message.configure(text=res)
    else:
        res = "Normal"
        message.configure(text=res)


#clearButton = tk.Button(window, text="Clear", command=clear  ,fg="red"  ,bg="green"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
#clearButton.place(x=950, y=200)

takeImg = tk.Button(window,
                    text="Click to load X-ray Images ",
                    command=run_example,
                    fg="red",
                    bg="green",
                    width=20,
                    height=3,
                    activebackground="Red",
                    font=('times', 15, ' bold '))
takeImg.place(x=400, y=500)

quitWindow = tk.Button(window,
                       text="Quit",
                       command=window.destroy,
                       fg="red",
                       bg="green",
                       width=20,
                       height=3,
                       activebackground="Red",
                       font=('times', 15, ' bold '))
quitWindow.place(x=900, y=500)
window.mainloop()

# entry point, run the example
