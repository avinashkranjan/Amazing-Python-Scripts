'''
  For using this Script you need to install OpenCV in your machine
'''
# Importing openCV library
import cv2 as cv

# Taking path of input from the user
path = input("Enter the path of image: ")
img = cv.imread(path)
img = cv.resize(img, (640, 640))  # resizing the image

# Printing the original image
cv.imshow('Original', img)

# Initiate FAST object with default values
fast = cv.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img, None)
img2 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))

# Print all default parameters
print("Threshold: {}".format(fast.getThreshold()))
print("nonmaxSuppression:{}".format(fast.getNonmaxSuppression()))
print("neighborhood: {}".format(fast.getType()))
print("Total Keypoints with nonmaxSuppression: {}".format(len(kp)))

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)

print("Total Keypoints without nonmaxSuppression: {}".format(len(kp)))
final = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))

# Naming the output image
image_name = path.split(r'/')
image = image_name[-1].split('.')
output = r".\\" + image[0] + "(_detected).jpg"

# Saving the image
cv.imwrite(output, final)

# Printing the final output image
cv.imshow('Final', final)
cv.waitKey(0)
cv.destroyAllWindows()
