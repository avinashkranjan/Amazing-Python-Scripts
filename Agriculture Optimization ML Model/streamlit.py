import streamlit as st
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
data = pd.read_excel("data.xlsx")
y = data['label']
X = data.drop(["label"], axis=1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)
lr = LogisticRegression()
lr.fit(X_train, y_train)


def predict_crop(input_data):
    crop_label = lr.predict(input_data)
    return crop_label[0]


def main():
    st.title("Agriculture Optimisation App")
    st.write("Enter the parameter values to predict the crop label:")

    n = st.number_input("N", value=0.0)
    p = st.number_input("P", value=0.0)
    k = st.number_input("K", value=0.0)
    temperature = st.number_input("Temperature", value=0.0)
    humidity = st.number_input("Humidity", value=0.0)
    ph = st.number_input("pH", value=0.0)
    rainfall = st.number_input("Rainfall", value=0.0)

    input_data = np.array([[n, p, k, temperature, humidity, ph, rainfall]])

    crop_label = predict_crop(input_data)

    st.subheader("Predicted Crop Label:")
    st.write(crop_label)


if __name__ == '__main__':
    main()
