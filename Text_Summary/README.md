# Text_Summary (Text Rank Approach)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Text Summarization is an advanced project and comes under the umbrella of Natural Language Processing.
There are multiple methods people use in order to summarize text.

They can be affectively clubbed under 2 methods:

- Abstractive: Understand the true context of text before summarization (like a human).
- Extractive: Rank the text within the file and identify the impactful terms.

While both these approaches are under research, extractive summarization is presently used across multiple platform.
There are multiple methods by which text is summarized under extractive approach as well.

In this script we will use Text Rank approach for text summarization.

## Dependencies

- nltk
- numpy
- networkx

## NLTK models

- `stopwords` - Stopwords are the English words which does not add much meaning to a sentence.

## Setup

- Setup a `python 3.x` virtual environment.
- `Activate` the environment
- Install the dependencies using 
  
```bash
pip3 install -r requiremnts.txt
```

- Set up the models by running the following commands,

```bash
$ python -m nltk.downloader stopwords
```

- Run the `text_summary.py` file
- Enter the source path.

## Results

The code generates the tokens (same as weights) of set of words, it shows the relative importance of words according to 
the summarizer, just uncomment the _l-112_

Results can be found [here](assets).

## Author(s)

Made by [Vybhav Chaturvedi](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/)
