#importing libraries 
import numpy as np
import cv2 as cv

#giving path of the image
path = input("Enter the path of the image\n")   
img_path= path

img = cv.imread(img_path)
orig=cv.resize(img,(540,540),interpolation=cv.INTER_AREA)
cv.imshow('Original image',orig)            #showing original image

hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
skinRegionHSV = cv.inRange(hsvim, lower, upper)
blurred = cv.blur(skinRegionHSV, (2,2))

ret,thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)  #thresholding

orig2=cv.resize(thresh,(540,540),interpolation=cv.INTER_AREA)
cv.imshow("thresh", orig2)
edges=cv.Canny(blurred,0,255)
print('Number of edges'+ '=' +str(len(edges)))     #printing number of edges
origi=cv.resize(edges,(540,540),interpolation=cv.INTER_AREA)
cv.imshow("canny",origi)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)   #contours 
print('Number of contours'+ '=' +str(len(contours)))                                  #printing number of contours
contours = max(contours, key=lambda x: cv.contourArea(x))
cv.drawContours(img, [contours], -1, (192, 57, 43), 3)
orig3=cv.resize(img,(540,540),interpolation=cv.INTER_AREA)
cv.imshow("contours", orig3)

hull = cv.convexHull(contours)       #convex hull
cv.drawContours(img, [hull], -1, (183, 21, 64), 2)
orig4=cv.resize(img,(540,540),interpolation=cv.INTER_AREA)
cv.imshow("hull", orig4)

hull = cv.convexHull(contours, returnPoints=False)
defects = cv.convexityDefects(contours, hull)
if defects is not None:
  cnt = 0
for i in range(defects.shape[0]):  # calculate the angle
  s, e, f, d = defects[i][0]
  start = tuple(contours[s][0])
  end = tuple(contours[e][0])
  far = tuple(contours[f][0])
  a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
  b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
  c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
  angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  #      cosine theorem
if angle <= np.pi / 2:  # angle less than 90 degree, treat as fingers
    cnt += 1
    cv.circle(img, far, 4, [0, 0, 255], -1)
if cnt > 0:
  cnt = cnt+1
  
cv.putText(img, str(cnt), (0, 50), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv.LINE_AA)
orig5=cv.resize(img,(540,540),interpolation=cv.INTER_AREA)

cv.imshow('final_result',orig5)   #final output image with Count
cv.waitKey(0)
