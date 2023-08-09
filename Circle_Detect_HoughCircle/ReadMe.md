# Circle detection
This python script will allow us to identify circles in an image using Hough circle transform

## Setup Instructions
### Install python3
sudo apt-get install python3
### Install pip (package installer for python)
sudo apt-get install python3-pip
### Install Numpy library with pip
pip3 install numpy
### Install OpenCV library with pip
pip3 install opencv-python
### Install tkinter library
sudo apt-get install python3-tk

## Details/Output
User is prompted to select an image and this script detects circles in it using the hough circle transform.  
 
**Note** Each image needs its own set of parameters in cv2.HoughCircles() function. What worked for one might not work for another image.  
minDist(minimum distance between two centers), param1(parameter 1), param2(parameter 2) are to be adjusted until we get desired output.

The output image is written/stored in the current folder.

## Author
Github: invigorzz313