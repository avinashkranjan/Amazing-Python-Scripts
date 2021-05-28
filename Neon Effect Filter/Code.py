import numpy as np
import cv2
import os.path 
from matplotlib import pyplot as plt

img_path = input("Enter the path of image: ")  #example -> C:\Users\xyz\OneDrive\Desktop\project\image.jpg 
img = cv2.imread(img_path)
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_small = cv2.pyrDown(image)
num_iter = 5
for _ in range(num_iter):
    img_small= cv2.bilateralFilter(img_small, d=9, sigmaColor=9, sigmaSpace=7)

img_rgb = cv2.pyrUp(img_small)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)
img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 2)

img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
array = cv2.bitwise_and(image, img_edge)
array1 = cv2.bitwise_xor(array, image)
plt.figure(figsize= (10,10))
plt.imshow(array1,cmap='gray')
plt.title("Neon Effect Filtered Photo")
plt.axis('off')
filename = os.path.basename(image_path)
plt.savefig("./Neon Effect Filter/Neon Effect Filter"+filename)  #saved file name as (Filtered)image_name.jpg

plt.show()
