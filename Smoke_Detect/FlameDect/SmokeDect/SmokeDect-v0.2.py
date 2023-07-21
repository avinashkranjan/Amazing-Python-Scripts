# *^_^* coding:utf-8 *^_^*
"""
SmokeDect-v0.2
检测方法：用MOG2提取运动区域，分小块提取hog特征，用svm分类
"""

from __future__ import print_function  # use print()

__author__ = 'stone'
__date__ = '15-11-30'

import cv2
import numpy as np
from time import time
import os

DEBUG_MOD = True
vName = '/home/stone/Code/FlameSmokeDetect/medias/videos/CTC.BG.055_11_320x240.avi'
train_directory = '/home/stone/Code/FlameSmokeDetect/tools/clips'
BLOCK_SIZE = 40


def hog_feature(img):
    """
    Extract HOG feature
    """
    win_size = (16, 16)
    block_size = (8, 8)
    block_stride = (8, 8)
    cell_size = (8, 8)
    nbins = 9
    descriptor = cv2.HOGDescriptor(
        win_size, block_size, block_stride, cell_size, nbins)
    hog_feature_hog = descriptor.compute(img)
    hog_feature_hog = np.float32(hog_feature_hog)
    return hog_feature_hog


def svm_create():
    """
    initial a SVM
    """
    svm_params = dict(kernel_type=cv2.ml.SVM_LINEAR,
                      svm_type=cv2.ml.SVM_C_SVC,
                      C=1,
                      gamma=0.5)
    svm = cv2.ml.SVM_create()
    svm.setKernel(svm_params['kernel_type'])
    svm.setType(svm_params['svm_type'])
    svm.setC(svm_params['C'])
    svm.setGamma(svm_params['gamma'])
    return svm


def file_path(directory):
    """
    generate a full directory path
    """
    files = os.listdir(directory)
    path = []

    for name in files:
        full_name = os.path.join(directory, name)
        path.append(full_name)
    print('%s 的文件数: %d\n' % (directory, len(path)))
    return path


# def load_hog(hog_path):
#     """
#     load hog files
#     """
#     print('loading hog files...')
#     hog = []
#     for fp in hog_path:
#         content = np.loadtxt(fp)
#         hog.append(content)
#     hog = np.float32(hog)
#     # print(hog)
#     print('finished!')
#     return hog


def split(img, cell_size, flatten=False):
    """
    Split into small blocks
    """
    split_h, split_w = img.shape[:2]
    sx, sy = cell_size
    split_cells = [np.hsplit(row, split_w // sx)
                   for row in np.vsplit(img, split_h // sy)]
    split_cells = np.array(split_cells)
    if flatten:
        split_cells = split_cells.reshape(-1, sy, sx)
    return split_cells


if __name__ == '__main__':
    print(__doc__)
    start_time = time()
    count = 0

    # create and train a SVM
    train_path = file_path(train_directory)
    train_hog = []
    response = []
    for img_path in train_path:
        print(img_path.split('-')[0])
        if img_path.split('-')[0] == '/home/stone/Code/FlameSmokeDetect/tools/clips/p':
            response.append(1)
        elif img_path.split('-')[0] == '/home/stone/Code/FlameSmokeDetect/tools/clips/n':
            response.append(0)
        img = cv2.imread(img_path)
        train_hog.append(hog_feature(img))
    print(len(train_hog[0]))
    train_hog = np.float32(train_hog)
    print(response)
    response = np.array(response)
    svm = svm_create()
    svm.train(train_hog, cv2.ml.ROW_SAMPLE, response)
    if svm.isTrained():
        print('SVM is trained!')

    cap = cv2.VideoCapture(vName)
    fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

    while 1:
        result = []
        ret, frame = cap.read()
        if frame is None:
            print("The End!!!")
            break

        # if count < 500:
        #     count += 1
        #     continue

        frame_copy = frame.copy()
        frame = cv2.GaussianBlur(frame, (5, 5), 2)
        frame = cv2.medianBlur(frame, 5)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fmask = fgbg.apply(gray_frame)

        kernel = np.ones((20, 20), np.uint8)
        fmask = cv2.medianBlur(fmask, 3)
        fmask = cv2.dilate(fmask, kernel)

        fmask_copy = fmask.copy()

        contour_img, contours, hierarchy = cv2.findContours(
            fmask_copy, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if contours is None:
            continue

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)

            if w < BLOCK_SIZE or h < BLOCK_SIZE:
                pass
            else:
                cells = split(frame, (BLOCK_SIZE, BLOCK_SIZE), flatten=False)
                cells_x_1 = x / BLOCK_SIZE
                cells_x_2 = (x + w) / BLOCK_SIZE
                cells_y_1 = y / BLOCK_SIZE
                cells_y_2 = (y + h) / BLOCK_SIZE
                for candidate in cells[cells_y_1:cells_y_2, cells_x_1:cells_x_2]:
                    for i in xrange(candidate.shape[0]):
                        hog = []
                        hog.append(hog_feature(candidate[i]))
                        hog = np.float32(hog)

                        result.append(svm.predict(hog)[0])
                        # print('HogFeature/hog%d-%d-%d' % (count, i, j))
                        # hog_file = 'HogFeature/hog%d-%d-%d' % (count, i, j)
                        # np.savetxt(hog_file, hog)

            if DEBUG_MOD is True:
                cv2.rectangle(frame_copy, (x, y),
                              (x + w, y + h), (0, 255, 0), 2)

        print(result)
        if 0 in result:
            print('yes')
        print('frame %d' % count)
        cv2.imshow('fmask', frame_copy)
        frame_and = cv2.bitwise_and(frame, frame, mask=fmask)

        count += 1
        k = cv2.waitKey(100) & 0xFF
        if k == 27:
            break

    end_time = time()
    total_time = end_time - start_time
    print('Total time: %d' % total_time)
    print(count)
    cap.release()
    cv2.destroyAllWindows()
