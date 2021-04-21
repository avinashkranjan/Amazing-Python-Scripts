import cv2

# getting the path for first image
src1 = input("Enter the path of the image 1\n")
src1 = cv2.imread(src1)
# src1 = cv2.resize(src1,(540,540))                 #resizing the image
# getting the path for second image
src2 = input("Enter the path of the image 2\n")
src2 = cv2.imread(src2)

# Resizing the image so that both images have same dimensions
src2 = cv2.resize(src2, src1.shape[1::-1])
# Applying Bitwise AND operation
andop = cv2.bitwise_and(src1, src2, mask=None)
andop = cv2.resize(andop, (640, 640))
cv2.imshow('Bitwise AND', andop)

orop = cv2.bitwise_or(src1, src2, mask=None)  # Applying Bitwise OR operation
orop = cv2.resize(orop, (640, 640))
cv2.imshow('Bitwise OR', orop)

xorop = cv2.bitwise_xor(src1, src2, mask=None)  # Applying Bitwise OR operation
xorop = cv2.resize(xorop, (640, 640))
cv2.imshow('Bitwise XOR', xorop)
cv2.waitKey(0)
cv2.destroyAllWindows()
