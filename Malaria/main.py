# import important libraries
import os
from PIL import Image
import tensorflow as tf
import numpy as np

# Configuring user's pc so that tensorflow model built on other's pc can run
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'

# reading image
val_path = input("Enter image path name eg.Images/cell1.jpg: ")
img = Image.open(val_path)
# confiiguring input image according to the model's requirement
img = img.resize((36, 36))
img = np.asarray(img)
img = img.reshape((1, 36, 36, 3))
img = img.astype(np.float64)
model_path = "./Malaria/Models/malaria.h5"
model = tf.keras.models.load_model(model_path)
pred = np.argmax(model.predict(img)[0])
if pred == 1:
    print("Infected Cell")
else:
    print("Healthy Cell")
