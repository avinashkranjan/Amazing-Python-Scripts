# *^_^* coding:utf-8 *^_^*
"""
计算图像累积灰度值，并保存到文件
"""
from __future__ import print_function

__author__ = 'stone'
__date__ = '16-2-18'

import cv2
import numpy as np

DEFAULT_VIDEO_SRC = '/home/stone/Code/FlameSmokeDetect/medias/videos/CTC.BG.055_11_320x240.avi'
cumsum_file = '/home/stone/Code/FlameSmokeDetect/medias/videos/cumulate_gray.txt'

if __name__ == '__main__':
    import sys
    try:
        video_src = sys.argv[1]
    except IndexError:
        video_src = DEFAULT_VIDEO_SRC

    cap = cv2.VideoCapture(video_src)

    frame_count = 1
    cumsum_value = []
    while 1:
        ret, frame = cap.read()
        if frame is None:
            print('The End!!!')
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cumulate_gray = np.cumsum(gray_frame, 0)
        # print(cumulate_gray[-1])

        cumsum_value.append(cumulate_gray[-1])

        cv2.imshow('frame', cumulate_gray)
        cv2.imshow('a', gray_frame)
        frame_count += 1
        k = cv2.waitKey(10) & 0xFF

        if k == 27:
            break

    np.savetxt(cumsum_file, cumsum_value, fmt='%d')
    cap.release()
    cv2.destroyAllWindows()
