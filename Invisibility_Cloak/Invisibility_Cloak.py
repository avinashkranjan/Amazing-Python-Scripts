import cv2
import numpy as np
import time

print("!! Invisibility is no more a Dream !!")

cap = cv2.VideoCapture(0)
time.sleep(3)
background = 0
for i in range(20):
    ret, background = cap.read()

background = np.flip(background, axis=1)

while (cap.isOpened()):
    ret, img = cap.read()

    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (35, 35)
    blurred = cv2.GaussianBlur(hsv, value, 0)

    low_red1 = np.array([0, 120, 70])
    low_red2 = np.array([170, 120, 70])

    up_red1 = np.array([10, 255, 255])
    up_red2 = np.array([180, 255, 255])

    cloak = cv2.inRange(hsv, low_red1, up_red1) + \
        cv2.inRange(hsv, low_red2, up_red2)
    cloak = cv2.morphologyEx(cloak, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    img[np.where(cloak == 255)] = background[np.where(cloak == 255)]
    cv2.imshow('Display', img)
    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
