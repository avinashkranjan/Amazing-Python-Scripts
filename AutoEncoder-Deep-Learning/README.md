# AutoEncoder-Deep-Learning

This code implements an AutoEncoder algorithm for recommendation system using the MovieLens dataset. AutoEncoders are neural networks designed for unsupervised learning, particularly for dimensionality reduction and feature extraction tasks.

## Code Overview
The code begins by downloading and extracting the MovieLens dataset using the `wget` and `unzip` commands. It imports the necessary libraries and modules for data processing and model training.

## Data Preparation
The MovieLens dataset files **(movies.dat, users.dat, and ratings.dat)** are loaded into DataFrames using pandas.
The training and test sets **(u1.base and u1.test)** are loaded and converted into numpy arrays.
The number of users and movies in the dataset is determined.

## Data Conversion
The training and test sets are converted into a list of lists, where each inner list represents the ratings of a user for different movies. This conversion is necessary for the input format required by the AutoEncoder.
The converted data is then transformed into PyTorch FloatTensors.

## AutoEncoder Model
The AutoEncoder model is defined using a custom class `SAE`, which inherits from `nn.Module`.
The model architecture consists of fully connected layers (`nn.Linear`) with a sigmoid activation function (`nn.Sigmoid`) in between.
The forward pass of the model applies the activation function after each hidden layer.
The model uses the Mean Squared Error (`MSE`) loss (`nn.MSELoss`) and RMSprop optimizer (`optim.RMSprop`) for training.

## Training the Model
The training loop runs for a specified number of epochs.
For each epoch, the model is trained on the training set by iterating over each user's ratings.
Input and target tensors are created, and the model is trained to reconstruct the input.
The loss is calculated and accumulated for each user, considering only non-zero ratings.
The mean loss is computed and printed for each epoch.

## Testing the Model
The trained model is evaluated on the test set using a similar process as in training.
The reconstructed output is compared with the target ratings.
The test loss is calculated and averaged over all users.
The test loss is printed as the final result.

Please note that this code appears to be a Jupyter Notebook file (`.ipynb extension`).
