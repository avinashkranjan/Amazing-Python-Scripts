# *^_^* coding:utf-8 *^_^*
"""
提取图片中的目标区域
    USAGE:  click with left button the image show the clip image.
            press 's' save the clip in current frame, while press 'n', go to next frame
"""
from __future__ import print_function

__author__ = 'stone'
__date__ = '16-1-21'

import cv2
import numpy as np

VIDEO_SRC = '/home/stone/Code/FlameSmokeDetect/medias/videos/CTC_FG.028_9_320x240.avi'
SIZE = (40, 40, 3)


def get_clip(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        p1 = (x - SIZE[0] / 2, y - SIZE[1] / 2)
        p2 = (x + SIZE[0] / 2, y + SIZE[1] / 2)
        temp = frame[p1[1]:p2[1], p1[0]:p2[0]]
        clip[:, :] = temp
        cv2.imshow('clip', clip)


if __name__ == '__main__':
    print(__doc__)

    frame_count = 0
    clip = np.zeros(SIZE, np.uint8)

    cap = cv2.VideoCapture(VIDEO_SRC)
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', get_clip)

    while True:
        block_count = 0
        ret, frame = cap.read()
        if frame is None:
            print("The End!!!")
            break
        cv2.imshow('frame', frame)

        print('current frame: %d' % frame_count)
        k = cv2.waitKey(0) & 0xFF
        if k == ord('s'):
            while True:
                clip_name = 'clips/n-clip%d-%d.jpg' % (
                    frame_count, block_count)
                cv2.imwrite(clip_name, clip)
                print('saved %s' % clip_name)
                block_count += 1
                sk = cv2.waitKey(0) & 0xFF
                if sk == ord('n'):
                    break
        elif k == 27:
            break
        frame_count += 1
    cv2.destroyAllWindows()
