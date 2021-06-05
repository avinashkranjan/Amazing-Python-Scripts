
# Neon Effect Filter

Converting an image into an neon effect filtered image using some of the python libraries.

## Libraries used
Firstly import the following python libraries 
* OpenCv
* Os
* Matplotlib 
* Numpy

Taking path of the image/Real image as input using os and finally reading it using cv2

## Detailed explanation of the method used

* Imported the required libraries ( Numpy, Matplotlib, OpenCv, Os)
* Read the input path of the image using Cv2 library
* Used Bilateral Filter
* Followed by Median Blur
* Followed by Adaptive Threshold
* Followed by Bitwise "and" between original image and edge image
* And at last used Bitwise "xor" between orginal and output of the above "bitwise and image"
* Finally converted the image into "Neon Effect Filtered" image

## Original Image
<img src="Image/image_.jpg" height="500px">

## Neon Effect Filtered Image
<img src="Image/(Neon Effect Filter)image_.jpg" height="500px">

## Author(s)
[Akriti](https://github.com/A-kriti)
