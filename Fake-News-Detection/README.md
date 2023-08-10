# Fake-NewsDetection

This is a simple Fake News Detection project that utilizes Machine Learning (ML), Deep Learning (DL), LSTM (Long Short-Term Memory), Natural Language Processing (NLP), Stemming, Lemmatization, and Data Visualization techniques. The goal of this project is to build a model that can classify news articles as either real or fake.

Table of Contents: 
1. Introduction
2. Project Overview
3. Technologies Used
4. Dataset
5. Data Preprocessing
6. Feature Extraction
7. Model Architecture
8. Training
9. Evaluation
10. Usage

# Introduction:

Fake news has become a significant issue in the digital age, and developing methods to identify and combat it is crucial. This project aims to address the problem of fake news by leveraging Machine Learning and Deep Learning techniques to build a model that can distinguish between genuine and fake news articles.

# Project Overview
The project consists of several key steps:

1. Data collection and preprocessing: Obtain a dataset of labeled news articles and clean the data for further processing.

2. Feature extraction: Convert the textual data into numerical vectors using techniques like TF-IDF (Term Frequency-Inverse Document Frequency), stemming, and lemmatization.

3. Model Building: Implement a Deep Learning LSTM model to train on the extracted features.

4. Training: Train the LSTM model on the preprocessed data.

5. Evaluation: Evaluate the model's performance using various metrics to measure its effectiveness in detecting fake news.

6. Data Visualization: Visualize the results and important insights gained from the analysis.

# Technologies Used
The project employs the following technologies:

1. Machine Learning (ML) and Deep Learning (DL) techniques
2. Long Short-Term Memory (LSTM) neural networks
3. Natural Language Processing (NLP) for text data preprocessing
4. Stemming and Lemmatization for text normalization
5. Data Visualization libraries for presenting results effectively

# Dataset
The dataset used in this project is obtained from a reliable source and contains labeled news articles. It comprises two classes: "Real News" and "Fake News." The data should be split into training and testing sets to evaluate the model's performance.

# Data Preprocessing

Data preprocessing is a critical step to clean and prepare the text data for further analysis. The following preprocessing steps will be applied:

1. Removing HTML tags and special characters
2. Converting text to lowercase
3. Removing stopwords
4. Tokenization

Feature Extraction
To convert the textual data into numerical format for model training, the following techniques will be employed:

1. TF-IDF (Term Frequency-Inverse Document Frequency): To represent the importance of words in documents.
2. Stemming and Lemmatization: To reduce words to their base or root form.

# Model Architecture
The model architecture will consist of an LSTM neural network. LSTM is chosen for its ability to process sequential data and handle long-term dependencies, making it suitable for NLP tasks.


# Training
The training phase involves feeding the preprocessed data into the LSTM model. The model will be trained on the training dataset with an appropriate optimization algorithm and loss function.

# Evaluation
The model's performance will be evaluated using various metrics such as accuracy, precision, recall, and F1-score. Confusion matrix and ROC-AUC curves may also be employed to assess the model's effectiveness.

# Usage
To use this Fake News Detection project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using the provided requirements.txt file.
3. Run the data preprocessing scripts to clean and prepare the dataset.
4. Execute the feature extraction scripts to convert the text data into numerical vectors.
5. Train the LSTM model on the preprocessed data.
6. Evaluate the model's performance using the evaluation scripts.
7. Visualize the results and insights gained from the analysis.
8. Flask is used to view the website run the code run section and input your news articles, get the results as real or fake.

