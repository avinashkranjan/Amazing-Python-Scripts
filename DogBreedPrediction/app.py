import numpy as np
import cv2
import streamlit as st
from keras.models import load_model

st.set_page_config(
    page_title="Dog Breed Prediction",
    page_icon="🐶",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={"Get Help": None, "Report a Bug": None, "About": None},
)

st.markdown(
    """
    <style>
    .stButton button {
        background-color: white;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
    }

    .stButton button:hover {
        background-color: #1a5f95;
    }

    .stFileUploader label {
        color: #1f80c9;
        font-size: 18px;
    }

    .stTitle {
        font-size: 36px;
        color: #1f80c9;
        text-align: center;
        margin-bottom: 20px;
    }

    .stMarkdown {
        font-size: 20px;
    }

    .stApp {
        background-color: white;
    }

    .result-box {
        background-color: #e6f7ff;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }

    .result-text {
        font-size: 24px;
        color: #1f80c9;
        text-align: center;
        margin-top: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

model = load_model("breed_prediction.h5")
Class_Names = ['boston_bull', 'golden_retriever',
               'labrador_retriever', 'german_shepherd', 'border_collie']

header_image = "dog.png"
st.image(header_image, use_column_width=True)

st.title("Dog Breed Prediction")
st.markdown("Upload an image of the dog and let us predict its breed!")

dog_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if dog_image is not None:
    st.image(dog_image, caption="Uploaded Image", use_column_width=True)

    img_array = np.array(cv2.imdecode(
        np.fromstring(dog_image.read(), np.uint8), 1))
    img_array = cv2.resize(img_array, (224, 224))
    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    predicted_class = Class_Names[np.argmax(prediction)]

    st.markdown(
        f'<div class="result-box"><p class="result-text">Prediction: The dog breed is <b>{predicted_class}</b></p></div>',
        unsafe_allow_html=True
    )
