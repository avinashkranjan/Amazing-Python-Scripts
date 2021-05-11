import cv2                           #importing cv library
import numpy as np                   #importing numpy library as np   
import os                            #importing os module

path = input('Enter the path for image: ')   #Taking image path from user

img = cv2.imread(path)
  
# Convert image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   

#cascade loading
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h),    #Drawing rectangles on the faces detected
                  (0, 0, 255), 2)
      
    faces = img[y:y + h, x:x + w]
    cv2.imshow('Cropped faces',faces)     #Displaying the cropped faces
   
  
cv2.imshow('Original Image',img)              #Displaying the original Image

#Saving the image of cropped faces
directory = input('Enter the directory where you want to save the image: ')    #Taking input for desired directory
os.chdir(directory)
cv2.imwrite('Cropped faces.jpg',faces)   #saving the image
cv2.waitKey()
cv2.destroyAllWindows()
