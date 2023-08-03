import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report


def sentiment_analysis():
    """
    Perform sentiment analysis using an SVM classifier.

    The function reads the data from a CSV file, preprocesses it, and trains an SVM classifier
    for sentiment analysis on the 'text' column with the 'label' column as the target.

    Prints the accuracy and classification report on the test data.
    """
    # Load data from a CSV file (replace 'data.csv' with your data file)
    data = pd.read_csv('data.csv')

    # Preprocess data (remove any special characters, convert to lowercase, etc.)
    data['text'] = data['text'].apply(preprocess_text)

    # Split the data into features (X) and labels (y)
    X = data['text']
    y = data['label']

    # Convert text data to numerical features using TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(X)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Train an SVM classifier
    svm_classifier = SVC(kernel='linear')
    svm_classifier.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = svm_classifier.predict(X_test)

    # Calculate and print accuracy and classification report
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(classification_report(y_test, y_pred, zero_division=1))


def preprocess_text(text):
    # Replace special characters with spaces
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('-', ' ')

    # Convert to lowercase
    text = text.lower()

    return text


if __name__ == '__main__':
    sentiment_analysis()
