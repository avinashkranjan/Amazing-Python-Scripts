# -*- coding: utf-8 -*-

#image enhancement CLAHE - Contrast Limited Adaptive Histogram Equalization
import cv2

#read the  image
img = cv2.imread('default.jpg')

#preparation for CLAHE
clahe= cv2.createCLAHE()

#COnvert to Gray Scale image 

gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Lets apply enhancement finally

ench_img=clahe.apply(gray_img)

#And save it into a file

cv2.imwrite('enhanced.jpg',ench_img)

print("Done!!")
