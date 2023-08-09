# import the required libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read Image in GrayScale
img = cv2.imread("scene.jpg", cv2.IMREAD_GRAYSCALE)

titles = ["image"]
images = [img]

# Applying gradient
for i in range(1):
    plt.subplot(1, 1, i + 1), plt.imshow(images[i], "grey")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
