# importing required libraries

import cv2
import pytesseract
from PIL import Image

# Put the path where you stored the tesseract.exe file in your machine
pytesseract_file = input(
    "Enter the path where you stored the tesseract.exe file\n")
pytesseract.pytesseract.tesseract_cmd = pytesseract_file


cam = cv2.VideoCapture(0)  # Starting your webcam

while True:
    ret, img = cam.read()  # Capturing the image
    # Can convert colour image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Original", img)
    # Removing noise from the image
    ret, thresh = cv2.threshold(
        gray, 1010, 200, cv2.THRESH_OTSU, cv2.THRESH_BINARY)
    cv2.imshow("After removing noise", thresh)

    if not ret:
        break

    k = cv2.waitKey(1)  # Taking input from you

    if k % 256 == 27:  # Press Esc for exit
        # For Esc key
        print("Close")
        break

    elif k % 256 == 32:  # Press Space for capture the image
        # For Space key
        print("Image saved")
        # Put the path where you want to store the captured image in your machine
        path = input("Enter the path where you want to store the image\n ")
        path = path+'\img.jpg'
        cv2.imwrite(path, thresh)
        break

src = Image.open(path)

text = pytesseract.image_to_string(src)  # Extracting the text from image
print(text)

cam.release
cv2.destroyAllWindows
