from tkinter.filedialog import *
import tkinter as tk
import cv2


def select_image():  # selecting image and thresholding it to binary format
    photo = askopenfilename()
    global img, thresh
    img = cv2.imread(photo)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold_value = 125  # this value needs to be adjusted for every image
    ret, thresh = cv2.threshold(gray, threshold_value, 255, 0)


def erosion():
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded = cv2.erode(thresh, kernel, iterations=1)
    eroded = cv2.resize(eroded, (300, 300))
    cv2.imshow("Erosion", eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def dilation():
    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (5, 5))  # elliptic kernel
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    dilated = cv2.resize(dilated, (300, 300))
    cv2.imshow("Dilation", dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def opening():
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    opened = cv2.resize(opened, (300, 300))
    cv2.imshow("Opening", opened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def closing_opn():
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.resize(closed, (300, 300))
    cv2.imshow("Closing", closed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def morph_grad():
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    grad = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)
    grad = cv2.resize(grad, (300, 300))
    cv2.imshow("Morph gradient", grad)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def top_hat():
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    tophat = cv2.morphologyEx(thresh, cv2.MORPH_TOPHAT, kernel)
    tophat = cv2.resize(tophat, (300, 300))
    cv2.imshow("Top hat", tophat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def black_hat():
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    blackhat = cv2.morphologyEx(thresh, cv2.MORPH_BLACKHAT, kernel)
    blackhat = cv2.resize(blackhat, (300, 300))
    cv2.imshow("Black hat", blackhat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


window = tk.Tk()
window.title("Morphological transformations")
window.geometry('320x220')
label = tk.Label(window, text="Select an image and then choose an option").grid(
    row=0, column=0)
b = tk.Button(window, text="Select image",
              command=select_image).grid(row=1, column=0)


rad1 = tk.Radiobutton(window, text='erosion', value=1, command=erosion)
rad2 = tk.Radiobutton(window, text='dilation', value=2, command=dilation)
rad3 = tk.Radiobutton(window, text='opening', value=3, command=opening)
rad4 = tk.Radiobutton(window, text='closing', value=4, command=closing_opn)
rad5 = tk.Radiobutton(window, text='morph gradient',
                      value=5, command=morph_grad)
rad6 = tk.Radiobutton(window, text='top hat', value=6, command=top_hat)
rad7 = tk.Radiobutton(window, text='black hat', value=7, command=black_hat)

rad1.grid(row=2, column=0)
rad2.grid(row=3, column=0)
rad3.grid(row=4, column=0)
rad4.grid(row=5, column=0)
rad5.grid(row=6, column=0)
rad6.grid(row=7, column=0)
rad7.grid(row=8, column=0)

window.mainloop()
