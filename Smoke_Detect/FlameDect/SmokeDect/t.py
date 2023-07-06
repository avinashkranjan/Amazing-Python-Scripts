# *^_^* coding:utf-8 *^_^*

from __future__ import print_function  # use print()


import cv2
import numpy as np
import matplotlib.pyplot as plt

file_path = '/home/stone/Code/FlameSmokeDetect/medias/videos/055_11_320x240_gray.txt'

data = np.loadtxt(file_path).astype(np.int32)
print(data.shape)
# i = 200
# data_50 = data[i:i+50]
# data_mid = data[i+100:i+125]
#
# mean_50 = [np.mean(col_mean).astype(np.int32) for col_mean in data_50.T]
# print(mean_50)
# mean_mid = np.array([np.mean(col_mean).astype(np.int32) for col_mean in data_mid.T])
# print(mean_mid)
#
# T_vData = (mean_mid-mean_50)
# print(T_vData)
#
# plt.plot(T_vData)
# plt.show()
