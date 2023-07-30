import cv2
from tkinter.filedialog import *


# we will find number of blobs with pixel value 255 in the following image

# finding binary image
print("\nImage should preferably be white (lighter) blobs on black (darker) background ")
photo = askopenfilename()
img = cv2.imread(photo, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (300, 300))
n, l = img.shape
count = 0

# blur the image
ksize = (5, 5)  # kernel size
img = cv2.blur(img, ksize)

# thresholding the image
for i in range(n):
    for j in range(l):
        if (img[i, j] <= 127):
            img[i, j] = 0
        else:
            img[i, j] = 255


def dfs(i, j):
    img[i, j] = 127  # implying that we have visited this pixel for further reference
    if (i-1 >= 0):
        if (img[i-1, j] == 255):
            dfs(i-1, j)
    if (j-1 >= 0):
        if (img[i, j-1] == 255):
            dfs(i, j-1)
    if (j+1 < l):
        if (img[i, j+1] == 255):
            dfs(i, j+1)
    if (i+1 < n):
        if (img[i+1, j] == 255):
            dfs(i+1, j)
    if ((i-1 >= 0) and (j-1 >= 0)):
        if (img[i-1, j-1] == 255):
            dfs(i-1, j-1)
    if ((i-1 >= 0) and (j+1 < l)):
        if (img[i-1, j+1] == 255):
            dfs(i-1, j+1)
    if ((i+1 < n) and (j-1 >= 0)):
        if (img[i+1, j-1] == 255):
            dfs(i+1, j-1)
    if ((i+1 < n) and (j+1 < l)):
        if (img[i+1, j+1] == 255):
            dfs(i+1, j+1)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(1000)


for i in range(n):
    for j in range(l):
        if (img[i, j] == 255):
            count += 1  # to count number of white blobs
            dfs(i, j)

print("count is", count)
