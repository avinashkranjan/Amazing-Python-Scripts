import cv2
import tkinter as tk
from tkinter.filedialog import *


def choose_image():  # reading the image
    photo = askopenfilename()
    global img
    img = cv2.imread(photo)
    img = cv2.resize(img, (500, 500))

#  functions for every border type


def constant_border():
    bordered = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT)
    cv2.imshow("Constant border", bordered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def reflection_border():
    bordered = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT)
    cv2.imshow("Reflection border", bordered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def default_border():
    bordered = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_DEFAULT)
    cv2.imshow("Default border", bordered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def replicate_border():
    bordered = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REPLICATE)
    cv2.imshow("Replicate border", bordered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def wrap_border():
    bordered = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_WRAP)
    cv2.imshow("Wrap border", bordered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


window = tk.Tk()  # displaying menu and options
window.title("Borders on images")
window.geometry('320x220')
label = tk.Label(window, text="Select an image and then choose an option").grid(
    row=0, column=0)
b = tk.Button(window, text="Choose image",
              command=choose_image).grid(row=1, column=0)

rad1 = tk.Radiobutton(window, text='Constant border',
                      value=1, command=constant_border)
rad2 = tk.Radiobutton(window, text='reflection border',
                      value=2, command=reflection_border)
rad3 = tk.Radiobutton(window, text='default border',
                      value=3, command=default_border)
rad4 = tk.Radiobutton(window, text='replicate border',
                      value=4, command=replicate_border)
rad5 = tk.Radiobutton(window, text='wrap border', value=5, command=wrap_border)

rad1.grid(row=2, column=0)
rad2.grid(row=3, column=0)
rad3.grid(row=4, column=0)
rad4.grid(row=5, column=0)
rad5.grid(row=6, column=0)

window.mainloop()
