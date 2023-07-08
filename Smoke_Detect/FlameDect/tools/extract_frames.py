# *^_^* coding:utf-8 *^_^*
"""
Extract Frames from video.

USAGE
    extract_frames.py [ <videos_src|-> <frames_path|-> ]     # '-' means default

    default_video_src = '/home/stone/Code/FlameSmokeDetect/medias/videos/side/daria_side.avi'
    default_frames_path = '/home/stone/Pictures/extractFrames/'

    exit: Esc
"""
__author__ = 'stone'
__date__ = '16-1-14'

import cv2
import sys
import os

print __doc__
COUNT = 1
N_FRAME = 100    # 每隔N_FRAME帧保存一张图片
default_video_src = ''
default_frames_path = '/home/stone/Pictures/extractFrames/'

# 判断是否有视频参数并判断视频是否存在 ‘-’意思是使用默认参数
try:
    video_src = sys.argv[1]
except IndexError:
    video_src = default_video_src

if video_src == '-':
    video_src = default_video_src
if not os.path.exists(video_src):
    print 'video is not exist'
    exit()

# 判断是否有输出目录参数并判断是否存在，不存在则创建
try:
    frames_path = sys.argv[2]
except:
    frames_path = default_frames_path

if video_src == '-':
    video_src = default_video_src
if not os.path.exists(frames_path):
    print 'create direction %s ......' % video_src
    os.mkdir(frames_path)

print 'video_src = %s' % video_src
print 'frames_path = %s' % frames_path
cap = cv2.VideoCapture(video_src)

while True:
    ret, frames = cap.read()
    if frames is None:
        print 'The End!!!'
        print 'Total frames: %d' % COUNT
        break

    frame_name = '%sframe%d.jpg' % (frames_path, COUNT)
    if (COUNT % N_FRAME) == 0:
        cv2.imwrite(frame_name, frames)

    COUNT += 1
    cv2.imshow('frames', frames)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
