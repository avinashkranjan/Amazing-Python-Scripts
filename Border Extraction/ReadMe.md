# Border extraction
This python script will allow us to extract borders of objects in an image.

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
User should select an image and the script returns an output image of borders of the objects in it.  
The input image is converted into binary format and then we use morphological transformation of dilation minus erosion.  
**Note** The threshold value while converting an image into binary format needs to be adjusted for every image.

## Author
Github: invigorzz313