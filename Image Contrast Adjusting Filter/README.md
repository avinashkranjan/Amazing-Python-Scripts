
# Adjusting the contrast of an image to get a better version of it.

Used some of the python libraries to convert an image into a high contrast image.
* Matplotlib,
* IPython.display
* NumPy
* PIL

## Steps:
* Imported the required libraries ( Numpy, Matplotlib, PIL, IPython.display)
* Read the input image using Image from PIL library

### Methods applied 
* Converted the image into an array and then flatten it making it a 1d array
* Count the number of occurance of each pixel in the image and hence getting an array of frequency count of each pixels
* Then making cdf from the frequency count list 
* Normalizing the cdf
* Converting the cdf shape into the shape of given image
* Finally converted the image into contrast adjusted image


## Original Image
<img src="Images/Original_image.jpg" height="300px">

## Comparison With The Result 
<img src="Images/Result.jpg" height="300px">
