import cv2
import numpy as np
import tkinter as tk
from tkinter.filedialog import *

# asking input from user
photo = askopenfilename()
img = cv2.imread(photo)
imgcopy = img

a,b = -1,-1
rect = (0,0,0,0)
draw = False
count = 0

# for selecting the required foreground portion with a rectangle
def rect_draw(event, x, y, flag, param):
    global draw,a,b,rect,count
    if (event == cv2.EVENT_LBUTTONDOWN):
        draw = True
        a,b = x,y
    elif (event == cv2.EVENT_MOUSEMOVE):
        if (draw==True):
            rect = (a,b,x,y)
    elif (event == cv2.EVENT_LBUTTONUP):
        draw = False
        count = 1
        cv2.rectangle(img, (a,b),(x,y), (0,255,0), 1)
        rect = (a,b,x,y)
        cv2.imshow('Mark foreground', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

cv2.namedWindow('Mark foreground')
cv2.setMouseCallback('Mark foreground', rect_draw) # call back function
while count==0:
    cv2.imshow('Mark foreground', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

# Using the grabcut algorithm
mask = np.zeros(imgcopy.shape[:2], np.uint8)
bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)
cv2.grabCut(imgcopy, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
imgcopy = imgcopy*mask2[:,:,np.newaxis]

# displaying and saving the output image
cv2.imshow("Output", imgcopy)
cv2.imwrite("Output.png", imgcopy)
cv2.waitKey(0)
cv2.destroyAllWindows()
