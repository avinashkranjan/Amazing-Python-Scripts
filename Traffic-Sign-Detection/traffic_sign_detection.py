# -*- coding: utf-8 -*-

import os
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow import keras
import tensorflow as tf
from imgaug import augmenters as iaa
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np
import cv2 as cv
import csv
import random
PATH = '/content/Dataset'
TESTING_PATH = '/content/Dataset/Test'

# Minimal number of samples for each class for data augmentation
MIN_IMGS_IN_CLASS = 500

# Learning parameters
EPOCHS = 100
INIT_LR = 0.001
BATCH_SIZE = 256
SET_DECAY = True

# Imports

# images and corresponding labels
images = []
labels = []

# loop over all 43 classes
gtFile = open(PATH + '/Train.csv')
gtReader = csv.reader(gtFile, delimiter=',')  # csv parser for annotations file
next(gtReader)

# loop over all images in current annotations file
for row in gtReader:
    img = cv.imread(PATH + '/' + row[7])
    images.append(cv.resize(img, (28, 28)))
    labels.append(row[6])  # the 6th column is the label
gtFile.close()

print('Number of loaded images: ' + str(len(images)))
print('Number of loaded labels: ' + str(len(labels)))

train_X = np.asarray(images)
train_X = train_X / 255
train_X = np.asarray(train_X, dtype="float32")
train_Y = np.asarray(labels, dtype="float32")

print('Shape of training array: ' + str(train_X.shape))


def count_images_in_classes(lbls):
    """
    Determining number of images in a class for Graph
    :param lbls: Labels (different classes)
    :return: Dictionary of labels and count
    """
    dct = {}
    for i in lbls:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct


samples_distribution = count_images_in_classes(train_Y)
print(samples_distribution)


def distribution_diagram(dct):
    """
    Histogram of Count and Label
    :param dct: Dictionary of labels and count
    :return: Histogram
    """
    plt.bar(range(len(dct)), list(dct.values()), align='center')
    plt.xticks(range(len(dct)), list(dct.keys()), rotation=90, fontsize=7)
    plt.show()


distribution_diagram(samples_distribution)


def preview(images, labels):
    """
    Preview of a Images rom a label
    :param images: Image from a Label
    :param labels: Label
    """
    plt.figure(figsize=(16, 16))
    for c in range(len(np.unique(labels))):
        i = random.choice(np.where(labels == c)[0])
        plt.subplot(10, 10, c + 1)
        plt.axis('off')
        plt.title('class: {}'.format(c))
        plt.imshow(images[i])


preview(train_X, train_Y)


def augment_imgs(imgs, p, imgaug=None):
    """
    Performs a set of augmentations with with a probability p
    :param imgs: Performs Data Augmentation
    :param p: Probability for augmentation
    """
    from imgaug import augmenters as iaa
    augs = iaa.SomeOf(
        (2, 4),
        [
            # crop images from each side by 0 to 4px (randomly chosen)
            iaa.Crop(px=(0, 4)),
            iaa.Affine(scale={
                "x": (0.8, 1.2),
                "y": (0.8, 1.2)
            }),
            iaa.Affine(translate_percent={
                "x": (-0.2, 0.2),
                "y": (-0.2, 0.2)
            }),
            # rotate by -45 to +45 degrees)
            iaa.Affine(rotate=(-45, 45)),
            # shear by -10 to +10 degrees
            iaa.Affine(shear=(-10, 10))
        ])

    seq = iaa.Sequential([iaa.Sometimes(p, augs)])
    res = seq.augment_images(imgs)
    return res


def augmentation(imgs, lbls):
    """
    Data Augmentation for a Label
    :param imgs: Images
    :param lbls: Labels
    """
    classes = count_images_in_classes(lbls)
    for i in range(len(classes)):
        if classes[i] < MIN_IMGS_IN_CLASS:
            # Number of samples to be added
            add_num = MIN_IMGS_IN_CLASS - classes[i]
            imgs_for_augm = []
            lbls_for_augm = []
            for j in range(add_num):
                im_index = random.choice(np.where(lbls == i)[0])
                imgs_for_augm.append(imgs[im_index])
                lbls_for_augm.append(lbls[im_index])
            augmented_class = augment_imgs(imgs_for_augm, 1)
            augmented_class_np = np.array(augmented_class)
            augmented_lbls_np = np.array(lbls_for_augm)
            imgs = np.concatenate((imgs, augmented_class_np), axis=0)
            lbls = np.concatenate((lbls, augmented_lbls_np), axis=0)
    return imgs, lbls


train_X, train_Y = augmentation(train_X, train_Y)

print(train_X.shape)
print(train_Y.shape)

augmented_samples_distribution = count_images_in_classes(train_Y)
print(augmented_samples_distribution)

distribution_diagram(augmented_samples_distribution)

preview(train_X, train_Y)

train_X = rgb2gray(train_X)


def build(width, height, depth, classes):
    """
    Initialize the model and its dimension
    """
    model = keras.Sequential()
    inputShape = (height, width, depth)
    chanDim = -1

    # CONV => RELU => BN => POOL
    model.add(Conv2D(8, (5, 5), padding="same", input_shape=inputShape))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # first set of (CONV => RELU => CONV => RELU) * 2 => POOL
    model.add(Conv2D(16, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(Conv2D(16, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # second set of (CONV => RELU => CONV => RELU) * 2 => POOL
    model.add(Conv2D(32, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(Conv2D(32, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # first set of FC => RELU layers
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation("relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    # second set of FC => RELU layers
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation("relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    # softmax classifier
    model.add(Dense(classes))
    model.add(Activation("softmax"))

    # return the constructed network architecture
    return model


model = build(28, 28, 1, 43)

if SET_DECAY:
    opt = Adam(lr=INIT_LR, decay=INIT_LR / (EPOCHS * 0.5))
else:
    opt = Adam(lr=INIT_LR)
model.compile(loss="sparse_categorical_crossentropy",
              optimizer=opt,
              metrics=["accuracy"])

test_images = []
test_labels = []
test = '/content/Dataset'
# loop over all 43 classes
gtFile = open('/content/Dataset/Test.csv')  # annotations file
gtReader = csv.reader(gtFile, delimiter=',')  # csv parser for annotations file
next(gtReader)

# loop over all images in current annotations file
for row in gtReader:
    img = cv.imread(PATH + '/' + row[7])
    test_images.append(cv.resize(img, (28, 28)))
    test_labels.append(row[6])
gtFile.close()

test_X = np.asarray(test_images)
test_X = test_X / 255
test_X = np.asarray(test_X, dtype="float32")

test_X = rgb2gray(test_X)

test_Y = np.asarray(test_labels, dtype="float32")

print(train_X.shape)
train_X_ext = np.expand_dims(train_X, axis=3)
print(train_X_ext.shape)
print(train_Y.shape)
train_Y_ext = np.expand_dims(train_Y, axis=1)
print(train_Y_ext.shape)

with tf.device('/device:GPU:0'):
    os.mkdir("models_Xception")
    for i in range(EPOCHS):
        model.save("models_Xception/model_" + str(i) + ".h5")
        H = model.fit(train_X_ext, train_Y, epochs=1, batch_size=BATCH_SIZE)

print(model.summary())

model.save_weights('model_final.h5')
