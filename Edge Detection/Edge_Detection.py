'''
  For using this Script you need to install OpenCV in your machine
 '''
# Importing openCV library
import cv2 as cv

# Taking path of input from the user
path = input("Enter the path of uploaded image: ")
img = cv.imread(path)
img = cv.resize(img, (640, 640))  # resizing the image

# Printing the original image
cv.imshow('Original', img)
# Reducing the noise from the image
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

# Using Canny algorithm to detect the edges of the image
final = cv.Canny(gray, 100, 200)
print('Number of edges' + '=' + str(len(final)))  # printing Number of edges
cv.imshow('Final', final)
cv.waitKey(0)
cv.destroyAllWindows()
