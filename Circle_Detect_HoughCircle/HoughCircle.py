# from turtle import circle
import cv2
import numpy as np
from tkinter.filedialog import *
import tkinter as tk

photo = askopenfilename()
img = cv2.imread(photo, cv2.IMREAD_GRAYSCALE)
blurred = cv2.medianBlur(img, 5)
edges = cv2.Canny(blurred, 50, 150, apertureSize=3)
# the image read in grayscale format is blurred and edges are detected in it
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT,
                           1, 30, param1=50, param2=31, minRadius=0, maxRadius=0)
# the parameters in the above function needs to be adjusted for each image accordingly.
circles = np.uint16(np.around(circles))

colorImg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
for i in circles[0, :]:
    cv2.circle(colorImg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # drawing the circle
    cv2.circle(colorImg, (i[0], i[1]), 2, (0, 0, 255), 3)
    # drawing its center

cv2.imwrite('output.jpg', colorImg)
cv2.imshow('output', colorImg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
