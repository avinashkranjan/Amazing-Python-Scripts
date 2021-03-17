# Face Recognition using OpenCV's Builtin Recognizer 

## About This Project

Aim: This script recognizes the face in from video stream. 

## Implementation 

Captures images from your webcam video stream
Extracts all Faces from the image frame (using haarcascades)
Stores the Face information into numpy arrays

1. Read and show video stream, capture images
2. Detect Faces and show bounding box (haarcascade)
3. Flatten the largest face image(gray scale) and save in a numpy array
4. Repeat the above for multiple people to generate training data

Recognise faces using some classification algo - logistic, KNN, SVM etc.

1. Read a video stream using opencv
2. extract faces out of it 
3. load the training data(numpy array of all the persons)
	a. x-values are stored in numpy arrays
	b. y-values we need to assign for each person 
4. use knn to find the prediction of face(int)
5. map the predicted id to name of the user 
6. display the predictions on the screen - bounding box and name

## Application

Using this script we can recognize the faces in the running videos (frame by frame). Face recognition is also useful in human computer interaction, virtual reality, database recovery, multimedia, computer entertainment, information security.

## How To Run

To run the script use following commands

1. Get the required modules
    ```bash
    pip install -r requirements.txt
    ```

2. Get multiple images of multiple person from face_data_collect.py and save them in numpy array.
    
3. Run the face_recognition.py 
    

