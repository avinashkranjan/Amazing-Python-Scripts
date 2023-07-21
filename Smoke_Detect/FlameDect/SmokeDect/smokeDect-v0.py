# *_* coding:utf-8 *_*

__author__ = 'stone'
__date__ = '15-9-28'

import numpy as np
import cv2

vName = '../videos/CTC_FG.028_9.mpg'
# CTC_FG.028_9.mpg
# Homewood_BGsmokey.050_10.mpg
# Heavenly_FG.052_09.mpg
# CTC.BG.055_11.mpg
# camera2.mov


cap = cv2.VideoCapture(vName)


# fgbg = cv2.createBackgroundSubtractorKNN()


def draw_detections(img, rects, thickness=1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15 * w), int(0.05 * h)
        cv2.rectangle(img, (x + pad_w, y + pad_h),
                      (x + w - pad_w, y + h - pad_h), (0, 255, 0), thickness)


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
while True:
    ret, frame = cap.read()
    if frame is None:
        print("视频读取完毕！")
        break
    height, width, ret = frame.shape
    # 视频旋转问题
    # center = (height, width)
    # angle = 30
    # scale = 1
    # rotate = cv2.getRotationMatrix2D(center, angle, scale)

    # 缩小 n 倍显示视频
    n = 1
    small_frame = cv2.resize(
        frame, (width / n, height / n), interpolation=cv2.INTER_CUBIC)

    # fgmask = fgbg.apply(small_frame)
    # median = cv2.medianBlur(fgmask, 3)

    found, w = hog.detectMultiScale(
        small_frame, winStride=(8, 8), padding=(8, 8), scale=1.05)
    draw_detections(small_frame, found, 3)

    print "found: {}".format(found)
    print 'w: {}'.format(w)

    # GsBlur = cv2.GaussianBlur(fgmask, (5, 5), 0)
    # kernel = np.ones((5, 5), np.uint8)
    # opening = cv2.morphologyEx(median, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("video", small_frame)
    # cv2.imshow("frame", fgmask)
    # cv2.imshow("test", median)

    # if found is not ():
    #     cv2.waitKey(0)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        print("终止播放！")
        break

cap.release()
cv2.destroyAllWindows()
