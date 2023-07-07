import tensorflow as tf
import tensorflow.keras.applications.mobilenet_v2 as mobilenet
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np


def classify_image(image_path):
    # Load the pre-trained MobileNetV2 model
    model = mobilenet.MobileNetV2(weights='imagenet')

    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    processed_img = preprocess_input(img_array)

    # Perform image classification
    predictions = model.predict(processed_img)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    return decoded_predictions


# Example usage
image_path = "image.jpg"
predictions = classify_image(image_path)

# Print the top 3 predictions
for prediction in predictions:
    print(f"{prediction[1]}: {prediction[2]*100:.2f}%")
