# *^_^* coding:utf-8 *^_^*

from __future__ import print_function

__author__ = 'stone'
__date__ = '16-1-22'

import cv2
import numpy as np
import os

direction = 'clips'
hog_save_directory = 'hog/'


def hog_feature(img):
    """
    Extract HOG feature
    """
    win_size = (16, 16)
    block_size = (16, 16)
    block_stride = (8, 8)
    cell_size = (8, 8)
    nbins = 9
    descriptor = cv2.HOGDescriptor(
        win_size, block_size, block_stride, cell_size, nbins)
    hog = descriptor.compute(img)
    return hog


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


if __name__ == '__main__':
    path = file_path(direction)
    for i in path:
        img = cv2.imread(i)
        hog = hog_feature(img)
        hog_file = '%s%s.txt' % (hog_save_directory, i.split('/')[-1])
        print(hog)
        np.savetxt(hog_file, hog)
