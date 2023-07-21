import numpy as np
import cv2
import math

# video capture
capture = cv2.VideoCapture(0)

while True:
    success, img = capture.read()

    # Frame Cropping
    cv2.rectangle(img, (20, 20), (400, 300), (0, 255, 0), 0)
    crop_image = img[20:300, 20:400]

    # TODO: Grey Filter (pass crop_image)
    # grey = your code
    grey = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)

    # TODO: Gaussian Blur to smoothen the image (pass grey)
    # blur = your code
    blur = cv2.GaussianBlur(grey, (35, 35), 0)

    # TODO: thresholding the image using Binary inversion + OTSU
    # ret,thresh= your code
    ret, thresh = cv2.threshold(
        blur, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # show threshold
    cv2.imshow("Threshold", thresh)

    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    try:
        # TODO: contour with maximum area
        # contour = your code
        contour = max(contours, key=lambda x: cv2.contourArea(x))

        # bounding rectangle for the contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 0)

        # TODO: create hull
        # hull = your code  (important: do not use returnPoints argument)
        hull = cv2.convexHull(contour)

        drawing = np.zeros(img.shape, np.uint8)
        cv2.drawContours(drawing, [contour], -1, (0, 255, 0), 0)
        cv2.drawContours(drawing, [hull], -1, (0, 0, 255), 0)

        # TODO: finding convex hull
        # hull = your code  (important: use returnPoints argument as False)
        hull = cv2.convexHull(contour, returnPoints=False)

        # TODO: finding convexity defects
        # defects = your code
        defects = cv2.convexityDefects(contour, hull)

        count_defects = 0
        # TODO: refer to the math for calculating the angle part of README
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])

            a = math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
            b = math.sqrt((-start[0] + far[0]) ** 2 +
                          (-start[1] + far[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b**2 + c**2 - a**2) / (2*b*c)))*57

            if angle <= 90:
                count_defects += 1
                cv2.circle(crop_image, far, 1, [0, 0, 255], -1)
            cv2.line(crop_image, start, end, [0, 255, 0], 2)

        # output
        # TODO: Complete the logic
        if count_defects == 0:
            cv2.putText(img, "ONE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        # elif count_defects == 1:
        elif count_defects == 1:
            cv2.putText(img, "TWO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 2:
            cv2.putText(img, "THREE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 3:
            cv2.putText(img, "FOUR", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 4:
            cv2.putText(img, "FIVE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

        else:

            pass

    except:
        pass

    cv2.imshow("Gesture", img)
    all_image = np.hstack((drawing, img))

    cv2.imshow('contours', all_image)

    if cv2.waitKey(1) == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()
