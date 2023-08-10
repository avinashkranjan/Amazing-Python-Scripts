import numpy as np
import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


df = pd.read_csv("city_day.csv", na_values="=")

numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())


df = df.drop(["Date", "AQI_Bucket"], axis=1)


label_encoder = LabelEncoder()
df["City"] = label_encoder.fit_transform(df["City"])
city_mapping = {
    'Ahmedabad': 0,
    'Amaravati': 1,
    'Aizawl': 2,
    'Amritsar': 3,
    'Bengaluru': 4,
    'Bhopal': 5,
    'Brajrajnagar': 6,
    'Chandigarh': 7,
    'Chennai': 8,
    'Coimbatore': 9,
    'Delhi': 10,
    'Ernakulam': 11,
    'Gurugram': 12,
    'Guwahati': 13,
    'Hyderabad': 14,
    'Jaipur': 15,
    'Jorapokhar': 16,
    'Kochi': 17,
    'Kolkata': 18,
    'Lucknow': 19,
    'Mumbai': 20,
    'Patna': 21,
    'Shillong': 22,
    'Talcher': 23,
    'Thiruvananthapuram': 24,
    'Visakhapatnam': 25
}


y = df.pop("AQI")


x_train, x_test, y_train, y_test = train_test_split(
    df, y, test_size=0.2, random_state=0)


model = RandomForestRegressor(max_depth=50, random_state=0)
model.fit(x_train, y_train)


def main():
    st.title("Air Quality Index Prediction")

    st.write("## User Input Features")

    city = st.selectbox("City", df["City"].unique())
    pm2_5 = st.slider("PM2.5", float(df["PM2.5"].min()), float(
        df["PM2.5"].max()), float(df["PM2.5"].mean()))
    pm10 = st.slider("PM10", float(df["PM10"].min()), float(
        df["PM10"].max()), float(df["PM10"].mean()))
    no = st.slider("NO", float(df["NO"].min()), float(
        df["NO"].max()), float(df["NO"].mean()))
    no2 = st.slider("NO2", float(df["NO2"].min()), float(
        df["NO2"].max()), float(df["NO2"].mean()))
    nox = st.slider("NOx", float(df["NOx"].min()), float(
        df["NOx"].max()), float(df["NOx"].mean()))
    nh3 = st.slider("NH3", float(df["NH3"].min()), float(
        df["NH3"].max()), float(df["NH3"].mean()))
    co = st.slider("CO", float(df["CO"].min()), float(
        df["CO"].max()), float(df["CO"].mean()))
    so2 = st.slider("SO2", float(df["SO2"].min()), float(
        df["SO2"].max()), float(df["SO2"].mean()))
    o3 = st.slider("O3", float(df["O3"].min()), float(
        df["O3"].max()), float(df["O3"].mean()))
    benzene = st.slider("Benzene", float(df["Benzene"].min()), float(
        df["Benzene"].max()), float(df["Benzene"].mean()))
    toluene = st.slider("Toluene", float(df["Toluene"].min()), float(
        df["Toluene"].max()), float(df["Toluene"].mean()))
    xylene = st.slider("Xylene", float(df["Xylene"].min()), float(
        df["Xylene"].max()), float(df["Xylene"].mean()))

    input_data = pd.DataFrame(
        {
            "City": [city],
            "PM2.5": [pm2_5],
            "PM10": [pm10],
            "NO": [no],
            "NO2": [no2],
            "NOx": [nox],
            "NH3": [nh3],
            "CO": [co],
            "SO2": [so2],
            "O3": [o3],
            "Benzene": [benzene],
            "Toluene": [toluene],
            "Xylene": [xylene]
        }
    )

    st.sidebar.write("## City Label Mapping")
    st.sidebar.write(city_mapping)

    prediction = model.predict(input_data)

    st.write("## Prediction")
    st.write(f"Predicted AQI: {prediction[0]}")


if __name__ == "__main__":
    main()
