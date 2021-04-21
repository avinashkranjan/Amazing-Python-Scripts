import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras import layers
import tensorflow as tf
from keras.preprocessing.image import img_to_array
from tensorflow.keras import backend
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from sklearn.metrics import classification_report
import sklearn.metrics as metrics
import itertools
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


def data_set(dir_data):
    data = []
    target = []
    data_map = {
        'with_mask': 1,
        'without_mask': 0
    }
    skipped = 0
    root = dir_data+'_annotations.csv'
    df1 = pd.read_csv(root)
    df1.dataframeName = '_annotations.csv'
    nRow, nCol = df1.shape
    for i in range(len(df1)):
        without_mask = 'without_mask'
        k = dir_data+df1['filename'][i]
        image = cv2.imread(k)
        xmin = int(df1['xmin'][i])
        ymin = int(df1['ymin'][i])
        xmax = int(df1['xmax'][i])
        ymax = int(df1['ymax'][i])
        #image=image[ymin:ymax,  xmin:xmax]
        try:
            # resizing to (70 x 70)
            image = cv2.resize(image, (70, 70))
        except Exception as E:
            skipped += 1
            print(E)
            continue
        if(df1['class'][i] == 'mask'):
            without_mask = 'with_mask'
        image = img_to_array(image)
        data.append(image)
        target.append(data_map[without_mask])
    data = np.array(data, dtype="float") / 255.0
    target = tf.keras.utils.to_categorical(np.array(target), num_classes=2)
    return data, target


training_data, training_target = data_set(
    './Face-Mask-Detection/kaggle/input/face-mask-detection/train/')
testing_data, testing_target = data_set(
    './Face-Mask-Detection/kaggle/input/face-mask-detection/test/')
valid_data, valid_target = data_set(
    './Face-Mask-Detection/kaggle/input/face-mask-detection/valid/')
plt.figure(0, figsize=(100, 100))
for i in range(1, 10):
    plt.subplot(10, 5, i)
    plt.imshow(training_data[i])
img_shape = training_data[0].shape
depth, height, width = 3, img_shape[0], img_shape[1]
img_shape = (height, width, depth)
chanDim = -1
# Returns a string, either 'channels_first' or 'channels_last'
if backend.image_data_format() == "channels_first":
    img_shape = (depth, height, width)
    chanDim = 1
model = Sequential()
model.add(layers.Conv2D(32, (3, 3), input_shape=img_shape))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(64, (3, 3)))
model.add(layers.Activation('relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(128, (3, 3)))
model.add(layers.Activation('relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(256, (3, 3)))
model.add(layers.Activation('relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.4))
model.add(layers.Dense(2, activation='softmax'))
adam = tf.keras.optimizers.Adam(0.001)
model.compile(loss='categorical_crossentropy',
              optimizer=adam, metrics=['accuracy'])
model.summary()
aug = ImageDataGenerator(rotation_range=25, width_shift_range=0.1,
                         height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                         horizontal_flip=True, fill_mode="nearest")
history = model.fit(aug.flow(training_data, training_target, batch_size=10),
                    epochs=70,
                    validation_data=(valid_data, valid_target),
                    verbose=2,
                    shuffle=True)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.ylabel(['accuracy'])
plt.xlabel(['epoch'])
plt.legend(['accuracy', 'val_accuracy'])
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.ylabel(['loss'])
plt.xlabel(['epoch'])
plt.legend(['loss', 'val_loss'])
loss, accuracy = model.evaluate(testing_data, testing_target)
print('accuracy= ', loss, " loss= ", loss)
yhat = model.predict(testing_data)
test_pred = np.argmax(yhat, axis=1)
testing_target = np.argmax(testing_target, axis=1)
report = classification_report(testing_target, test_pred)
print(report)


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.RdYlGn):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


confusion = metrics.confusion_matrix(testing_target, test_pred)
plt.figure()
plot_confusion_matrix(confusion, classes=[
                      'without_mask', 'with_mask'], title='Confusion matrix')
