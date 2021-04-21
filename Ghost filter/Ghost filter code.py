import matplotlib.pyplot as plt
import numpy as np
import cv2
import os.path

# take path of the image as input
# example -> C:\Users\xyz\OneDrive\Desktop\project\image.jpg
img_path = input("Enter the path here:")
img = cv2.imread(img_path)
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
image_small = cv2.pyrDown(img)
number_iter = 5
for _ in range(number_iter):
    image_small = cv2.bilateralFilter(
        image_small, d=9, sigmaColor=9, sigmaSpace=7)
image_rgb = cv2.pyrUp(image_small)
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
image_blur = cv2.medianBlur(image_gray, 7)
image_edge = cv2.adaptiveThreshold(
    image_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 2)
image_edge = cv2.cvtColor(image_edge, cv2.COLOR_GRAY2RGB)
# taking xor between image and image_edge to get ghost filter
array = cv2.bitwise_xor(image, image_edge)
plt.figure(figsize=(10, 10))
plt.imshow(array)
plt.axis('off')

filename = os.path.basename(img_path)

plt.savefig("(Filtered)"+filename)
plt.show()  # real ghost filtered photo
