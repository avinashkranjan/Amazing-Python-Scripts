# Sentiment Analyser

This is a sentiment analyser that takes in a sentence and returns the sentiment of the sentence.
It gives rating to the emotions present in the sentence, from 0 to 1.
It uses NLP and ML algroithms to do so.
This is trained on word2vec dataset using IMDB movie reviews.
And the test model is based on RNN.



## Setup instructions
- Install python 3.6 or above
- Install the required packages using the following command
```bash
pip install -r requirements.txt
```
- First execute the word2vec.ipynb file to train the model
- Then execute the RNN(w2v).ipynb file to test the model
- Change the epochs batch size based on your system configuration and the accuracy you want.
- It will then create a csv file with the sentiment of the sentence.

## Output
Check the screenshot in this folder for the output.

## Author(s)

- [Aditya Jethani](https://github.com/okaditya84)

