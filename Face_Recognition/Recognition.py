import numpy as np
import cv2 as cv
import os
haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = []
DIR = r'images'  # DIR - path of the folder containing images
for i in os.listdir(DIR):
    people.append(i)

# LBPHFaceRecognizer - instatiate the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# We are using the trained yml file.
face_recognizer.read('face_trained.yml')

# img = cv.imread(r'images\henry\13.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces)
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0,
               (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('detected face', img)

cv.waitKey(0)
