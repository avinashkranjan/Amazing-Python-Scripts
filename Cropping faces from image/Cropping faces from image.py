import cv2                           #importing cv library
import numpy as np                   #importing numpy library as np                      
from google.colab.patches import cv2_imshow 

img = cv2.imread('/content/guju.jpg')
  
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), 
                  (0, 0, 255), 2)
      
    faces = img[y:y + h, x:x + w]
    cv2_imshow(faces)
   # cv2.imwrite('face.jpg', faces)
  
cv2_imshow( img)
cv2.waitKey()
