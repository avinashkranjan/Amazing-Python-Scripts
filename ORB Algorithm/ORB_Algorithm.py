import cv2
import numpy as np

# Load the image
path=input('Enter the path of the image: ')
image = cv2.imread(path)
path2=input('Enter the path for testing image: ')
test_image=cv2.imread(path2)

#Resizing the image
image=cv2.resize(image,(600,600))
test_image=cv2.resize(test_image,(600,600))

# Convert the image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
test_gray = cv2.cvtColor(test_image, cv2.COLOR_RGB2GRAY)

#Display the given and test image
image_stack = np.concatenate((image, test_image), axis=1)
cv2.imshow('image VS test_image', image_stack)

#Implementing the ORB alogorithm
orb = cv2.ORB_create()

train_keypoints, train_descriptor = orb.detectAndCompute(gray, None)
test_keypoints, test_descriptor = orb.detectAndCompute(test_gray, None)

keypoints = np.copy(image)

cv2.drawKeypoints(image, train_keypoints, keypoints, color = (0, 255, 0))

# Display image with keypoints
cv2.imshow('keypoints',keypoints)
# Print the number of keypoints detected in the given image
print("Number of Keypoints Detected In The Image: ", len(train_keypoints))

# Create a Brute Force Matcher object.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

# Perform the matching between the ORB descriptors of the training image and the test image
matches = bf.match(train_descriptor, test_descriptor)

# The matches with shorter distance are the ones we want.
matches = sorted(matches, key = lambda x : x.distance)

result = cv2.drawMatches(image, train_keypoints, test_image, test_keypoints, matches, test_gray, flags = 2)

# Display the best matching points
cv2.imshow('result',result)

#Naming the output image
image_name = path.split(r'/')
image_path = image_name[-1].split('.')
output  = r"./ORB Algorithm/"+ image_path[0] + "(featureMatched).jpg"
cv2.imwrite(output,result)

# Print total number of matching points between the training and query images
print("\nNumber of Matching Keypoints Between The input image and Test Image: ", len(matches))
cv2.waitKey(0)
cv2.destroyAllWindows()
