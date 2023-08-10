Description:
The primary goal of this project is to develop a machine learning model that can automatically classify emails as either spam or legitimate (ham) based on their content. The LSTM model(Long Short-Term Memory), recurrent neural network (RNN) architecture, is employed to capture sequential patterns in the text data, making it well-suited for natural language processing tasks like this.

Dataset

The project employs a labeled dataset of emails, containing both spam and ham samples. The dataset is preprocessed to tokenize and pad the text data before feeding it into the LSTM model. Please replace `'spam_ham_dataset.csv'` in the code with your actual dataset path.

Model Architecture

The LSTM model architecture involves the following key components:

- `Embedding` Layer: Converts the integer-encoded vocabulary into dense vectors of fixed size.
- First `LSTM` Layer: Captures sequential patterns by returning sequences instead of a single output.
- `Dropout` Layer: Helps prevent overfitting by randomly deactivating a fraction of input units during training.
- Second `LSTM` Layer: Aggregates the output of the previous LSTM layer.
- `Dense` Layer: Produces a single output unit with sigmoid activation for binary classification.

The model is trained using binary cross-entropy loss and the Adam optimizer.


Install required packages:
pip install numpy pandas tensorflow


