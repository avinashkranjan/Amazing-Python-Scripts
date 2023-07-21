# importing the libraries for loading data and visualisation
import os
import cv2
import numpy as np
from PIL import Image
# import for train-test-split
from sklearn.model_selection import train_test_split
# import for One Hot Encoding
from keras.utils import to_categorical
# importing libraries for Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Flatten, Dropout, BatchNormalization

# loading the data of images and setting their labels
data = []
labels = []

Parasitized = os.listdir("../input/malaria/cell_images/Parasitized/")

for a in Parasitized:
    try:
        imageP = cv2.imread("../input/malaria/cell_images/Parasitized/" + a)
        image_from_arrayP = Image.fromarray(imageP, 'RGB')
        size_imageP = image_from_arrayP.resize((36, 36))
        data.append(np.array(size_imageP))
        labels.append(0)
    except AttributeError:
        print("")

Uninfected = os.listdir("../input/malaria/cell_images/Uninfected/")

for b in Uninfected:
    try:
        imageU = cv2.imread("../input/malaria/cell_images/Uninfected/" + b)
        image_from_arrayU = Image.fromarray(imageU, 'RGB')
        size_imageU = image_from_arrayU.resize((36, 36))
        data.append(np.array(size_imageU))
        labels.append(1)
    except AttributeError:
        print("")

# Creating single numpy array of all the images and labels
data1 = np.array(data)
labels1 = np.array(labels)
print('Cells : {} and labels : {}'.format(data1.shape, labels1.shape))

# lets shuffle the data and labels before splitting them into training and testing sets
n = np.arange(data1.shape[0])
np.random.shuffle(n)
data2 = data1[n]
labels2 = labels1[n]

# Splitting the dataset into the Training set and Test set
X_train, X_valid, y_train, y_valid = train_test_split(data2,
                                                      labels2, test_size=0.2, random_state=0)
X_trainF = X_train.astype('float32')
X_validF = X_valid.astype('float32')
y_trainF = to_categorical(y_train)
y_validF = to_categorical(y_valid)

classifier = Sequential()
# CNN layers
classifier.add(Conv2D(32, kernel_size=(3, 3),
                      input_shape=(36, 36, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(BatchNormalization(axis=-1))
classifier.add(Dropout(0.5))   # Dropout prevents overfitting
classifier.add(Conv2D(32, kernel_size=(3, 3),
                      input_shape=(36, 36, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(BatchNormalization(axis=-1))
classifier.add(Dropout(0.5))
classifier.add(Flatten())
classifier.add(Dense(units=128, activation='relu'))
classifier.add(BatchNormalization(axis=-1))
classifier.add(Dropout(0.5))
classifier.add(Dense(units=2, activation='softmax'))
classifier.compile(optimizer='adam',
                   loss='categorical_crossentropy', metrics=['accuracy'])
history = classifier.fit(X_trainF, y_trainF,
                         batch_size=120, epochs=15,
                         verbose=1, validation_data=(X_validF, y_validF))
classifier.summary()

y_pred = classifier.predict(X_validF)
y_predF = np.argmax(y_pred, axis=1)
y_valid_one = np.argmax(y_validF, axis=1)
classifier.save("./Malaria/Models/malaria.h5")
