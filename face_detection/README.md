# FACE DETECTION

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This project is based on face detection using OpenCV with a webcam. It continuously captures frames, detects faces, and displays the frames with rectangles around the detected faces. Pressing the 'n' key terminates the program.

## Explanation of Code
1) import cv2: Necessary libraries imported.
2) cap = cv2.VideoCapture(0): Creates a video capture object to capture frames from webcam
3) Haar Cascade  Classifier is  used for face detection.
4) The detectMultiScale function detects objects (faces in this case) in the grayscale frame. The second and third arguments are the scale factor and minimum number of neighbors, respectively. Adjusting these parameters can affect the performance and accuracy of the face detection.
5) The infinite loop breaks when 'n' key is pressed



## Output :smiley:
<img width="528" alt="figure" src="https://github.com/naazkakria/face_recognition_/blob/main/image_detected.jpeg">

## Authors
1) Written by Sakshi
2) Written by [Naaz](https://github.com/naazkakria)



