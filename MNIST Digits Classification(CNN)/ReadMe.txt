Description:
Convolutional Neural Network to recognize handwritten digits from the MNIST dataset.We began by preprocessing the data, reshaping images, and converting labels to one-hot encoding. Our CNN architecture involved convolutional layers with ReLU activation and MaxPooling for feature extraction, followed by BatchNormalization for stabilization. We added dense layers for classification, including a final softmax layer. After training the model and evaluating its performance on test data, we visualized training and validation accuracy over epochs using matplotlib.

Dataset:
MNIST Handwritten Digits

Requirements:
pip install numpy keras matplotlib
