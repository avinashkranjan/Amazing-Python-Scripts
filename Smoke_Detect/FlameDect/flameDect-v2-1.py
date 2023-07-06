#! /usr/bin/env python
# coding=utf-8

# ++++++++++++++++++++++++++++++++++++++++++++++++++
# 存在的问题：
# 1.RGB下火焰像素点的规律未掌握
# 2.程序现在的运行速度是每祯处理2秒
#
# 先灰度化，二值化，中值滤波，开运算，
# 根据颜色找火焰区域，画轮廓
#
# author：stone 2015.08.30
# ++++++++++++++++++++++++++++++++++++++++++++++++++

import numpy as np
import cv2
import time

tStart = time.time()
# ++++++++++++++++++++++获取视频+++++++++++++++++++++
vName = 'videos/forest1.avi'
# Boat_Fire_Stream.wmv
# controlled3.avi
# Extreme_Fire_Scenes_Stream.wmv
# forest1.avi
# forest2.avi

cap = cv2.VideoCapture(vName)

# +++++++++++++++++++++处理视频++++++++++++++++++++++
while True:
    ret, frame = cap.read()
    if frame is None:
        print("视频读取完毕")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ret, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    height, width = binary.shape
    npframe = np.array(frame)
    # nphsv = np.array(hsv)
    npbinary = np.array(binary)
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
    openning2 = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernal2)

    # +++++++++++++++判断亮点颜色是否R >= G > B+++++++++++++
    binary_x = 0
    Rt = 135
    St = 55
    while binary_x < height:
        binary_y = 0
        while binary_y < width:
            if (opening[binary_x, binary_y] == 255):
                p = npframe[(binary_x, binary_y)]
                # p2 = hsv[(binary_x, binary_y)]
                #    ？？？？？？怎么转换到hsv颜色空间，然后再增加一条限制： S >= （（255-R）*ST/RT）
                # ？？？？？？加上S限制之后效果不好，可能是S有误，需要研究一下HSV 或者 HSI 或者其他有S的颜色空间
                if p[2] >= p[1] >= p[0]:  # & p2[2] >= 5:
                    binary_y += 1
                    continue
                else:
                    opening[binary_x, binary_y] = 0
            binary_y += 1
        binary_x += 1
    # +++++++++++++++显示高亮区域轮廓+++++++++++++++++++++++
    image, contour, hierarchy = cv2.findContours(opening,
                                                 cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contour == []:
        print('无轮廓')
    else:
        #    在视频窗口中显示轮廓
        cv2.drawContours(frame, contour, -1, (0, 0, 255), 2)

        # +++++++++++++++图像中的点是否在轮廓内++++++++++++++++++++

        # ？？？无轮廓时索引异常
    #    if np.array(contour)[0] == None:
    #        print '无轮廓'
    #    else:
    #        npcontour = np.array(contour)[0]
    #    npframe = np.array(frame)
    #    t = time.time()
    #    for x in xrange(height):
    #        for y in xrange(width):
    #            inContour = cv2.pointPolygonTest(npcontour, (x, y), False)
    #            if (inContour > 0):
    #                print npframe[(x, y)]
    #                t1 = time.time()
    #                print t - t1

    # ++++++++++++++++++++++显示视频++++++++++++++++++++++
    cv2.imshow('frame', frame)  # 原图像
    cv2.imshow('binary', binary)
    # cv2.imshow('hsv', hsv)
    #    cv2.imshow('contour', opening)  #开运算图像
    #    cv2.imshow('opening2', openning2)          #中值模糊图像
    tEnd = time.time()
    totalTime = (tEnd - tStart)
    print(tStart)
    print(tEnd)
    print('总时间 %d ' % totalTime)
    if cv2.waitKey(1) & 0xFF == 27:
        print('中止播放')
        break
# tEnd = time.time()

cap.release()
cv2.destroyAllWindows()
# totalTime = (tEnd - tStart)
print(time.clock())
# print '总时间 %d ' % totalTime
