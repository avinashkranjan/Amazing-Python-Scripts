#!/usr/bin/env python
# coding: utf-8

# Imports
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

# Enter the File path
file_name = input("Enter the Source File: ")
print("This script requires 'stopwords' from NLTK, see README"
      "Quick Download Command: ```python -m nltk.downloader stopwords```")


def read_article(file_name):
    """
    Reads the Text file, and coverts them into sentences.
    :param file_name: Path of text file (line 12)
    :return: sentences
    """
    file = open(file_name, 'r', encoding="utf-8")
    filedata = file.readlines()
    article = filedata[0].split(". ")
    sentences = []

    for sentence in article:
        # Uncomment if you want to print the whole file on screen.
        # print(sentence)
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences


def sentence_similarity(sent1, sent2, stopwords=None):
    """
    To determine the Cosine Similarity between sentences
    :param sent1: Vector of sentence 1
    :param sent2: Vector of sentence 2
    :param stopwords: Words to be ignored in Vectors (Read README.md)
    :return: Cosine Similarity score
    """
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stop_words):
    """
    Build the similarity index of words in sentences
    :param sentences: Clean sentences
    :param stop_words: Words to be ignored in Vectors (Read README.md)
    :return: Similarity index (Tokenized words)
    """
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:  # ignore if both are same sentences
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(
                sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


def generate_summary(file_name, top_n=5):
    """
    Generate Summary of the text file
    :param file_name: Path of text file (line 12)
    :param top_n: Number of Sentence to be vectorized (tokenized)
    :return: Summary of text
    """
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 1 - Read text anc split it
    sentences = read_article(file_name)

    # Step 2 - Generate Similarity Matrix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity matrix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)),
                             reverse=True)

    # Print the index of the statements
    # print("Indexes of top ranked_sentence order are ", ranked_sentence)

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))

    # Step 5 - Output of the text file
    filepath_index = file_name.find('.txt')
    outputpath = file_name[:filepath_index] + '_textRank.txt'

    with open(outputpath, 'w') as w:
        for sentence in summarize_text:
            w.write(str(sentence) + '\n')


generate_summary(file_name, 5)
