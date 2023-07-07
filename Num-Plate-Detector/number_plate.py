# importing libraries
import numpy as np
import cv2
import imutils
import sys
import pytesseract
import pandas as pd
import time

image = cv2.imread(input("Enter the path of image: "))

image = imutils.resize(image, width=500)

pytesseract.pytesseract.tesseract_cmd = input(
    "Enter the path of tesseract in your local system : ")

# displaying it
cv2.imshow("Original Image", image)

# converting it into gtray scale
# cv2.imshow("1 - Grayscale Conversion", gray)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow("2 - Bilateral Filter", gray)
gray = cv2.bilateralFilter(gray, 11, 17, 17)

# canny edge detector
# cv2.imshow("4 - Canny Edges", edged)
edged = cv2.Canny(gray, 170, 200)

"""
there are three arguments in cv2.findContours() function, first one is source image, 
second is contour retrieval mode, third is contour approximation method.py

If you pass cv2.CHAIN_APPROX_NONE, all the boundary points are stored.
But actually do we need all the points? For eg, you found the contour of a straight line.
Do you need all the points on the line to represent that line?
No, we need just two end points of that line.
This is what cv2.CHAIN_APPROX_SIMPLE does.
It removes all redundant points and compresses the contour, thereby saving memory.
"""

cnts, _ = cv2.findContours(
    edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# contour area is given by the function cv2.contourArea()
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
NumberPlateCnt = None

count = 0
for c in cnts:
    """
    contour perimeter is also called arclength. It can be found out using cv2.arcLength()
    function.Second argument specify whether shape is a closed contour( if passed
    True), or just a curve.
    """
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        NumberPlateCnt = approx
        break

# Masking the part other than the number plate
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [NumberPlateCnt], 0, 255, -1)
new_image = cv2.bitwise_and(image, image, mask=mask)
cv2.namedWindow("Final_image", cv2.WINDOW_NORMAL)
cv2.imshow("Final_image", new_image)

# Configuration for tesseract
config = ('-l eng --oem 1 --psm 3')

# Run tesseract OCR on image
text = pytesseract.image_to_string(new_image, config=config)

# Data is stored in CSV file
raw_data = {'date': [time.asctime(time.localtime(time.time()))],
            'v_number': [text]}

df = pd.DataFrame(raw_data, columns=['date', 'v_number'])
df.to_csv('data.csv')

# Print recognized text
print(text)

cv2.waitKey(0)
