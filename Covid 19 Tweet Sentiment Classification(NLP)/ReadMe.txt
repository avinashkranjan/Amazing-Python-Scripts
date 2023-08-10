Description:
a text classification model using a pipeline with a TF-IDF vectorizer(NLP) and a Linear Support Vector Classifier (LinearSVC).

Details
The dataset : tweets about COVID-19, and the goal is to classify the sentiment of the tweets.
A text sentiment analysis task using a machine learning pipeline. It loads a dataset of COVID-19 related tweets, preprocesses the data, and performs sentiment classification using a Linear Support Vector Classifier (LinearSVC) combined with TF-IDF vectorization. The code splits the dataset into training and testing sets, trains the model, makes predictions on the test set, and then visualizes the resulting confusion matrix using Seaborn's heatmap.

Requirements:
pip install pandas scikit-learn seaborn jupyter numpy matplotlib
