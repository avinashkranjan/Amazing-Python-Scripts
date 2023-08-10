import cv2
import tkinter as tk
from tkinter.filedialog import *

window = tk.Tk()
window.title("Matching shapes")
window.geometry('350x200')


def image1():  # getting image 1
    photo1 = askopenfilename()
    global gray1
    img1 = cv2.imread(photo1)
    img1 = cv2.resize(img1, (500, 500))
    gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)


def image2():  # getting image 2
    photo2 = askopenfilename()
    global gray2
    img2 = cv2.imread(photo2)
    img2 = cv2.resize(img2, (500, 500))
    gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)


def proceeds():  # detecting shape matching using contours
    ret, threshold = cv2.threshold(gray1, 127, 255, 0)
    ret, threshold2 = cv2.threshold(gray2, 127, 255, 0)
    contours, hierarchy, rem1 = cv2.findContours(threshold, 2, 1)
    cnt1 = contours[0]
    contours, hierarchy, rem2 = cv2.findContours(threshold2, 2, 1)
    cnt2 = contours[0]
    ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
    print(ret)
    label = tk.Label(window, text="Probability of shapes matching: " +
                     str(1-ret)).grid(row=4, column=1)


label = tk.Label(window, text="Image 1").grid(row=1, column=0)
label = tk.Label(window, text="Image 2").grid(row=2, column=0)

b1 = tk.Button(window, text='choose image 1', command=image1)
b2 = tk.Button(window, text='choose image 2', command=image2)
proceed = tk.Button(window, text='Proceed', command=proceeds)

b1.grid(row=1, column=1)
b2.grid(row=2, column=1)
proceed.grid(row=3, column=1)

window.mainloop()
cv2.destroyAllWindows()
