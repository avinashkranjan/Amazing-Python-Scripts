# importing the libraries for loading data and visualisation
import os
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline 
from PIL import Image
import seaborn as sns
# import for train-test-split
from sklearn.model_selection import train_test_split
# import for One Hot Encoding
from keras.utils import to_categorical
# importing libraries for Model
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Flatten, Dropout, BatchNormalization
# importing libraries for evaluating the model
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# loading the data of images and setting their labels
data = []
labels = []

Parasitized = os.listdir("../input/cell-images-for-detecting-malaria/cell_images/Parasitized/")

for a in Parasitized:
    try:
        image = cv2.imread("../input/cell-images-for-detecting-malaria/cell_images/Parasitized/" + a)
        image_from_array = Image.fromarray(image, 'RGB')
        size_image = image_from_array.resize((36, 36))
        data.append(np.array(size_image))
        labels.append(0)
    except AttributeError:
        print("")

Uninfected = os.listdir("../input/cell-images-for-detecting-malaria/cell_images/Uninfected/")

for b in Uninfected:
    try:
        image = cv2.imread("../input/cell-images-for-detecting-malaria/cell_images/Uninfected/" + b)
        image_from_array = Image.fromarray(image, 'RGB')
        size_image = image_from_array.resize((36, 36))
        data.append(np.array(size_image))
        labels.append(1)
    except AttributeError:
        print("")

# Creating single numpy array of all the images and labels
data1 = np.array(data)
labels1 = np.array(labels)

print('Cells : {} and labels : {}'.format(data1.shape , labels1.shape))

# lets shuffle the data and labels before splitting them into training and testing sets
n = np.arange(data.shape[0])
np.random.shuffle(n)
data2 = data1[n]
labels2 = labels1[n]


### Splitting the dataset into the Training set and Test set

X_train, X_valid, y_trainPre, y_validPre = train_test_split(data2, labels2, test_size = 0.2, random_state = 0)
X_train = X_train.astype('float32')  
X_valid = X_valid.astype('float32')
# One Hot Encoding 
y_train = to_categorical(y_trainPre)
y_valid = to_categorical(y_validPre)


classifier = Sequential()
# CNN layers
classifier.add(Conv2D(32, kernel_size=(3, 3), input_shape = (36, 36, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(BatchNormalization(axis = -1))
classifier.add(Dropout(0.5))   # Dropout prevents overfitting
classifier.add(Conv2D(32, kernel_size=(3, 3), input_shape = (36, 36, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(BatchNormalization(axis = -1))
classifier.add(Dropout(0.5))
classifier.add(Flatten())
classifier.add(Dense(units=128, activation='relu'))
classifier.add(BatchNormalization(axis = -1))
classifier.add(Dropout(0.5))
classifier.add(Dense(units=2, activation='softmax'))
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
history = classifier.fit(X_train, y_train, batch_size=120, epochs=15, verbose=1, validation_data=(X_valid, y_valid))
classifier.summary()

y_pred = classifier.predict(X_valid)
# Convert back to categorical values 
y_predf = np.argmax(y_pred, axis=1)
y_validf = np.argmax(y_valid, axis=1)
classifier.save("./Malaria/Models/malaria.h5")
