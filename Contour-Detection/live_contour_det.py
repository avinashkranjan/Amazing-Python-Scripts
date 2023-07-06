# importing libraries
import cv2
import numpy as np

# initialize camera settings
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


def empty(a):
    pass


# name of the window
cv2.namedWindow("Parameters")

# resize the window
cv2.resizeWindow("Parameters", 640, 240)

# creating trackbars
cv2.createTrackbar("Threshold1", "Parameters", 23, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 20, 255, empty)
cv2.createTrackbar("Area", "Parameters", 5000, 30000, empty)

# function for stacking images together


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(
                        imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(
                    imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(
                    imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # detect the area of each contour and based on the area we can remove all the contours that we are not interested in
    # so in order to do that we will need a for loop
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)

            # find the corner points, so in order to do that we need to first find the length of contours
            # true basically means that the contour is closed
            peri = cv2.arcLength(cnt, True)

            # to approximate what type of shape this is, we will use the approximation of poly method
            # we will input the contour, will give it a resolution and then we will define again that this is a closed contour
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))

            # create a bounding box because we need to highlight the area of where the object is
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)

            # to display values so that we can easily see the number of points and the area detected
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x +
                        w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w +
                        20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)


# reading each frame
while True:
    success, img = cap.read()
    imgContour = img.copy()

    # converting img into blur version
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)

    # converting it into gray scale
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    # define trackbar positions
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    # canny edge detector
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    # define kernel for dilation
    kernel = np.ones((5, 5))

    # to overcome the overlaps and noise, we use dilation function
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
    getContours(imgDil, imgContour)

    # stacking images together as we want images side by side instead of different window
    imgStack = stackImages(0.8, ([img, imgCanny],
                                 [imgDil, imgContour]))

    # displaying it
    cv2.imshow("Result", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
