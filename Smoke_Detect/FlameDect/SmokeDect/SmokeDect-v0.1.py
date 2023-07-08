# *^_^* coding:utf-8 *^_^*

"""
Smoke detection based on SVM and HOG
"""

__author__ = 'stone'
__date__ = '15-11-13'

import os
import cv2
import numpy as np

train_dir = '../medias/smoke/positive'
test_dir = '../medias/smoke/test'
svm_params = dict(kernel_type=cv2.ml.SVM_LINEAR,
                  svm_type=cv2.ml.SVM_C_SVC,
                  C=2.67, gamma=5.385)


def image_path(path):
    files = os.listdir(path)
    img_path = []

    for name in files:
        fullname = os.path.join(path, name)
        img_path.append(fullname)

    return img_path


def hog_feature(path):
    img = cv2.imread(path)
    padding = (8, 8)
    block_stride = (8, 8)
    descriptor = cv2.HOGDescriptor()
    hog = descriptor.compute(img, block_stride, padding)
    return hog


if __name__ == '__main__':
    print __doc__

    train_image = image_path(train_dir)
    test_image = image_path(test_dir)
    response = [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1]
    print(response)
    response = np.array(response)
    train_data = train_image[:]
    train_hog = []
    for img in train_data:
        hog = hog_feature(img)
        print 'hog_values'
        print hog
        print '\n'
        train_hog.append(hog)
    # np.savetxt('0.1hog_train.txt', train_hog)
    test_hog = []
    print test_image
    for img in test_image:
        hog = hog_feature(img)
        test_hog.append(hog)
    # np.savetxt('0.1hog_test.txt', test_hog)

    train_hog = np.float32(train_hog)
    test_hog = np.float32(test_hog)

    svm = cv2.ml.SVM_create()
    svm.setGamma(0.5)
    svm.setC(1)
    svm.setKernel(cv2.ml.SVM_RBF)
    svm.setType(cv2.ml.SVM_C_SVC)
    print(train_hog)
    svm.train(train_hog, cv2.ml.ROW_SAMPLE, response)
    print(svm.isTrained())
    result = svm.predict(test_hog)
    print result
