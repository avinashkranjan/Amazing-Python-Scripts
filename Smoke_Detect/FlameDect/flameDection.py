
# -*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('fire/fd.png', 1)
# img = cv2.medianBlur(img,5)
img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                             cv2.THRESH_BINARY, 11, 2)
ret, img3 = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

plt.subplot(2, 2, 1), plt.imshow(img, 'gray'), plt.title('original')
plt.subplot(2, 2, 2), plt.imshow(img2, 'gray'), plt.title('adThres')
plt.subplot(2, 2, 3), plt.imshow(img3, 'gray'), plt.title('Thres')

plt.show()
