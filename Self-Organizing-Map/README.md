# Self-Organizing Map

This code implements a Self-Organizing Map (SOM) algorithm for fraud detection using credit card application data. The SOM is a type of artificial neural network that is used for unsupervised learning and is particularly useful for visualizing high-dimensional data.

## Code Overview
The code starts by importing the necessary libraries and mounting Google Drive to access the dataset file.

### Importing the libraries
`numpy` is imported as `np` for numerical operations.<br>
`pandas` is imported as `pd` for data manipulation and analysis.<br>
`matplotlib.pyplot` is imported as `plt` for data visualization.

### Importing the dataset
The code reads the credit card applications dataset from a CSV file and assigns the feature values to the variable X and the target variable (fraud or not) to the variable y.

## Feature Scaling
The dataset features are then scaled using the `MinMaxScaler` from **sklearn.preprocessing** to bring them to a uniform range between 0 and 1.

## Training the SOM
The SOM is initialized using the `MiniSom` class from the `minisom` library. The SOM is set up with a grid of 10x10 neurons and an input length of 15 (the number of features in the dataset). The initial weights of the SOM are randomly initialized using the dataset. The SOM is then trained using the `train_random` method for a specified number of iterations.

## Visualizing the results
The code visualizes the SOM by creating a grid plot using `bone()` and `pcolor()` from `pylab`. The color intensity of each neuron represents its distance from the neighboring neurons. The fraud and non-fraud customers from the dataset are then plotted on the SOM grid as markers ('o' and 's') using different colors ('r' and 'g').

## Finding the frauds
The code maps each customer from the dataset to the winning neuron on the SOM using the `winner` method. It then identifies the frauds by concatenating the customers mapped to specific fraudulent neurons. The frauds are then inverse transformed to obtain the original attribute values.

## Printing the Fraud Clients
Finally, the code prints the IDs of the fraud customers detected.

Please note that this code seems to be a Jupyter Notebook file (`.ipynb` extension) rather than a typical Python script. If you want to run it, you may need to set it up in an appropriate Jupyter Notebook environment.
