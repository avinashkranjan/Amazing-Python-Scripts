# Face Recognition with OpenCV built in classifier
# Aim: This script recognizes the face in an image using OpenCV's built-in recognizer. The vast application of this project is 
# recognizing the images in the running videos. 
# Feature: Easy and understandable code 

import os
import cv2 as cv
import numpy as np

people = []
DIR = r'images' # DIR - path of the folder containing images
for i in os.listdir(DIR): # Will append the names of the person in the people list 
    people.append(i)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# For every face in the list the corresponding labels to the features are designated. 
features = [] 
labels = []

def train_face():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_arr = cv.imread(img_path)
            gray = cv.cvtColor(img_arr,cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=4)

            for (x,y,w,h) in face_rect:
                face_roi = gray[y:y+h , x:x+w]
                features.append(face_roi)
                labels.append(label)

train_face()

# Feature and labels numpy array
features = np.array(features,dtype='object') 
labels = np.array(labels)

# Train our recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Trained on features and the labels list
face_recognizer.train(features,labels)

# Just like haar cascade yml file, we can save this file in yml format so that 
# we can easily access this trained model
face_recognizer.save('face_trained.yml')

####  save the features and labels into the numpy file 
# simply remove the comments of the below 2 line
#
# np.save('features.npy', features) 
# np.save('labels.npy',labels)