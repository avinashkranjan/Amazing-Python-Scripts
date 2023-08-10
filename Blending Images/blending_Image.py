import cv2
import tkinter as tk
from tkinter.filedialog import *

window = tk.Tk()
window.title("Image blending")
window.geometry('300x140')


def image1():  # getting image 1
    photo1 = askopenfilename()
    global img1
    img1 = cv2.imread(photo1)
    img1 = cv2.resize(img1, (500, 500))


def image2():  # getting image 2
    photo2 = askopenfilename()
    global img2
    img2 = cv2.imread(photo2)
    img2 = cv2.resize(img2, (500, 500))


def proceeds():  # reading alpha and displaying output
    global alpha
    alpha = t.get(1.0, "end-1c")
    alpha = float(alpha)
    if alpha >= 0 and alpha <= 1:
        beta = 1-alpha
        res = cv2.addWeighted(img1, alpha, img2, beta, 0.0)
        cv2.imshow('Result', res)
        cv2.imwrite("Output.jpg", res)
        cv2.waitKey(0)
    else:  # when alpha is invalid
        print("invalid alpha")
        exit()


label = tk.Label(window, text="Enter alpha (0 to 1)").grid(row=0, column=0)
label = tk.Label(window, text="Image 1").grid(row=1, column=0)
label = tk.Label(window, text="Image 2").grid(row=2, column=0)

t = tk.Text(window, height=1, width=5)
b1 = tk.Button(window, text='choose image 1', command=image1)
b2 = tk.Button(window, text='choose image 2', command=image2)
proceed = tk.Button(window, text='Proceed', command=proceeds)

t.grid(row=0, column=1)
b1.grid(row=1, column=1)
b2.grid(row=2, column=1)
proceed.grid(row=3, column=1)

window.mainloop()
cv2.destroyAllWindows()
