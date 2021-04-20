
import cv2
import numpy as np
from tkinter.filedialog import *

photo = askopenfilename()
img = cv2.imread(photo)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 5)
edges = cv2.adaptiveThreshold(
    grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# cartoonize
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Image", img)
cv2.imshow("Cartoon", cartoon)

# save
cv2.imwrite("cartoon.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
