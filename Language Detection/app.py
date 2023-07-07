# importing libraries
from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from googletrans import Translator
le = LabelEncoder()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    # loading the dataset
    data = pd.read_csv("language_detection.csv")
    y = data["Language"]

    # label encoding
    y = le.fit_transform(y)

    # loading the model and cv
    model = pickle.load(open("model.pkl", "rb"))
    cv = pickle.load(open("transform.pkl", "rb"))

    if request.method == "POST":
        # taking the input
        text = request.form["text"]
        # preprocessing the text
        text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', '', text)
        text = re.sub(r'[[]]', '', text)
        text = text.lower()
        dat = [text]
        # creating the vector
        vect = cv.transform(dat).toarray()
        # prediction
        my_pred = model.predict(vect)
        my_pred = le.inverse_transform(my_pred)

    return render_template("home.html", pred="{}".format(my_pred[0]))


@app.route("/translate", methods=["POST"])
def translate():
    translator = Translator()
    if request.method == "POST":
        # taking the input
        text = request.form["text"]
        # taking the target language
        target_lang = request.form["lang"]
        # translating the text
        translation = translator.translate(text, dest=target_lang)
    return render_template("home.html", translation=translation.text)


if __name__ == "__main__":
    app.run(debug=True)
