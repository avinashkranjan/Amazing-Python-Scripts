import cv2                           #importing cv library
import numpy as np                   #importing numpy library as np                      

path = input('Enter the path for image: ')   #Taking image path from user

img = cv2.imread(path)
  
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h),    #Drawing rectangles on the faces detected
                  (0, 0, 255), 2)
      
    faces = img[y:y + h, x:x + w]
    cv2.imshow('Cropped faces',faces)     #Displaying the cropped faces
   
  
cv2_imshow('Original Image',img)              #Displaying the original Image
cv2.waitKey()
cv2.destroyAllWindows()
