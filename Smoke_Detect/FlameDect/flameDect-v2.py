#! /usr/bin/env python
# coding=utf-8
import numpy as np
import cv2
import time

# tStart = time.time()
# ++++++++++++++++++++++获取视频+++++++++++++++++++++
vName = '../video/forest1.avi'
# Boat_Fire_Stream.wmv
# controlled3.avi
# Extreme_Fire_Scenes_Stream.wmv
# forest1.avi
# forest2.avi

cap = cv2.VideoCapture(vName)

# +++++++++++++++++++++处理视频++++++++++++++++++++++
while True:
    ret, frame = cap.read()
    if frame == None:
        print "视频读取完毕"
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    height, width = binary.shape

# +++++++++++++++++++++去噪+++++++++++++++++++++++++
# 二维卷积
#    kernel = np.ones((5, 5), np.float32)/25
#    dst = cv2.filter2D(binary, -1, kernel)

# 中值模糊
    dst = cv2.medianBlur(binary, 5)

# 高斯模糊
#    dst = cv2.GaussianBlur(binary, (5, 5), 0)

# 均值模糊
#    dst = cv2.blur(binary, (5, 5))

# +++++++++++++++做开运算（先腐蚀再膨胀）除噪点++++++++++++
    kernal2 = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernal2)

# +++++++++++++++显示高亮区域轮廓+++++++++++++++++++++++
    image, contour, hierarchy = cv2.findContours(opening,
                                                 cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 在视频窗口中显示轮廓
    cv2.drawContours(frame, contour, -1, (0, 0, 255), 2)

# +++++++++++++++图像中的点是否在轮廓内++++++++++++++++++++

# ？？？无轮廓时索引异常
    if np.array(contour)[0] == None:
        print '无轮廓'
    else:
        npcontour = np.array(contour)[0]
    npframe = np.array(frame)
#    t = time.time()
    for x in xrange(height):
        for y in xrange(width):
            inContour = cv2.pointPolygonTest(npcontour, (x, y), False)
            if (inContour > 0):
                print npframe[(x, y)]
#                t1 = time.time()
#                print t - t1

# ++++++++++++++++++++++显示视频++++++++++++++++++++++
    cv2.imshow('frame', frame)  # 原图像
    cv2.imshow('opening', opening)  # 开运算图像
    cv2.imshow('binary', binary)  # 二值化图像
    cv2.imshow('dst', dst)  # 中值模糊图像

    if cv2.waitKey(25) & 0xFF == 27:
        print '中止播放'
        break
# tEnd = time.time()
cap.release()
cv2.destroyAllWindows()
# totalTime = (tEnd - tStart)
print time.clock()
# print '总时间 %d ' % totalTime
