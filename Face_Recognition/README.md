# Face Recognition using OpenCV's Builtin Recognizer 

## About This Project

Aim: This script recognizes the face in an image using OpenCV's built-in recognizer. 

## Application

Using this script we can recognize the faces in the running videos (frame by frame).

## How To Run

To run the script use following commands

1. Get the required modules
    ```bash
    pip install -r requirements.txt
    ```

2. Get multiple images of multiple person and add the path of that folder in the following line of face_train.py
    ```python
    DIR = r' ' 
    ```
3. Run face_train.py so that it could read the faces and label them
    
4. Files face_trained.yml, features.npy and labels.npy will be created 

5. Run the recognition.py and insert any random images of the person you are recognizing 
    ```python
    img = cv.imread(r' ')
    ```
    

