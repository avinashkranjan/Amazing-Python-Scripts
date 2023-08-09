import cv2
import numpy as np
from tkinter.filedialog import *
import tkinter as tk

window = tk.Tk()
window.title("Line detection using Hough transform")
window.geometry('380x100')
label = tk.Label(window, text="Choose an option").grid(row=0, column=0)
# displaying a menu window for choosing transforms


def hough():
    photo = askopenfilename()
    img = cv2.imread(photo)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi/180, 500)
    for line in lines:
        rho, theta = line[0]
        # defining lines with the parameters returned by HoughLines()
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        # drawing lines on image to mark
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
    cv2.imwrite('houghlines.jpg', img)
    cv2.imshow("houghlines", img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


def houghP():
    photo = askopenfilename()
    img = cv2.imread(photo)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100,
                            minLineLength=100, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]  # endpoints are returned by HoughLinesP()
        # drawing lines by joining those
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
    cv2.imwrite('houghlinesP.jpg', img)
    cv2.imshow("houghlinesP", img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


rad1 = tk.Radiobutton(window, text='Hough Transform', value=1, command=hough)
rad2 = tk.Radiobutton(
    window, text='Probabilistic Hough Transform', value=2, command=houghP)

rad1.grid(row=1, column=0)
rad2.grid(row=2, column=0)

label = tk.Label(window, text="Check the output image in this folder you are working in").grid(
    row=3, column=0)

window.mainloop()
