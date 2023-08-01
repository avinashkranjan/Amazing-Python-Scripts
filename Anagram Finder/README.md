# Anagram Finder

## Description

Anagram Finder is a Python script that helps you find anagrams of a given word from a list of words. Anagrams are words formed by rearranging the letters of another word. This script uses a dictionary of words and groups them based on their sorted letter representations, making it efficient to find anagrams.

## Requirements

- Python
- nltk (Natural Language Toolkit) library

## Installation

1. Install Python from the official website: https://www.python.org/downloads/
2. Install the required nltk library by running the following command:

```bash
pip install nltk
```

## Usage

1. Clone this repository or download the anagram_finder.py file.

2. Run the script using Python:

```bash
python anagram_finder.py
```

The script will display anagrams for some sample search words, as well as additional words retrieved from the nltk library.

## Customization

You can customize the search words and the word list in the anagram_finder.py script. To search for different anagrams, modify the search_words list in the __main__ section of the script. Similarly, you can expand the word_list by adding more words to include in the anagram search.

# Sample search words
search_words = ["silent", "debit card", "funeral", "astronomer"]

# Combine the NLTK word list with the existing word list
word_list = [
    "listen", "silent", "enlist", "tinsel", "hello", "world", "python",
    "astronomer", "moonstarer", "debit card", "bad credit", "punishments", "nine thumps",
    "dormitory", "dirty room", "the eyes", "they see", "a gentleman", "elegant man",
    "funeral", "real fun", "slot machines", "cash lost in me", "eleven plus two", "twelve plus one"
] + nltk_word_list

## Contributing
If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request. We appreciate your contributions!