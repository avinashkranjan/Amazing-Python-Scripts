
# *-* coding:utf-8 *-*

import numpy as np
import cv2
import time

t = time.time()
"""读视频文件"""
vName = '../video/Boat_Fire_Stream.wmv'
cap = cv2.VideoCapture(vName)
tm = time.time()


"""二值化图像并取白色区域为火灾区域，用红色方框标出"""
while 1:
    ret, frame = cap.read()
    for i in xrange(50):
        if i % 50 != 0:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, binary = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)

        #    e1 = cv2.getTickCount()
            t1 = time.time()
            height, width = binary.shape
            x1, y1 = width, height
            x2, y2 = 0, 0
            n = 1
            for i in range(height):
                for j in range(width):
                    if binary[i][j] == 255:
                        if i < x1:
                            x1 = i
                        if i > x2:
                            x2 = i
                        if j < y1:
                            y1 = j
                        if j > y2:
                            y2 = j
        #    e2 = cv2.getTickCount()
            t2 = time.time()
        #    print e2 - e1
            print t2 - t1
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.rectangle(gray, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.rectangle(binary, (x1, y1), (x2, y2), (255), 2)

            cv2.imshow('frame', frame)
            cv2.imshow('gray', gray)
            cv2.imshow('binary', binary)

        t3 = time.time()
        print 'total time %f' % (t3 - t)
        print x1, y1, x2, y2

    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
