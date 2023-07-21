# Automatic Spelling Checker and Corrector Python Script

This script is a simple Python tool that performs automatic spelling checking and correction on a given text file. It utilizes the `spellchecker` library and `nltk` (Natural Language Toolkit) for tokenization.

## Prerequisites
- Python 3.x
- `spellchecker` library
- `nltk` library

## Usage
1. Ensure that the required libraries are installed by running `pip install spellchecker nltk`.
2. Run the script using the command: `python spelling_checker.py`.
3. You will be prompted to enter the path to the text file you want to check.
4. The script will analyze the text file, identify misspelled words, and suggest corrections.
5. You will be asked if you want to automatically correct the misspelled words.
6. If you choose to correct the errors, the corrected text will be saved in an `output.txt` file in the same directory.
7. Finally, the script will display a message indicating the completion of the process.

## How it Works
1. The script imports the necessary libraries and initializes the spellchecker.
2. The `readTextFile` function reads the input file and tokenizes the text using the `nltk` library.
3. The `findErrors` function checks each word in the text for misspellings using the `spell.correction` method.
4. The `printErrors` function displays the misspelled words and provides suggested corrections using the `spell.candidates` method.
5. The `correctErrors` function replaces the misspelled words in the tokenized text with their corrected versions and writes the corrected text to an output file.
6. The `main` function serves as the entry point of the script, calling the other functions in a sequential manner based on user input.

## Example
```
Enter text file: input.txt
```
This example prompts the user to enter the path to the text file they want to check. After analyzing the file, the script will display any misspelled words and their suggested corrections. The user will be given the option to automatically correct the errors. If chosen, the corrected text will be saved in an `output.txt` file.

## Disclaimer
This spelling checker script relies on the accuracy and coverage of the underlying spellchecker library. It is recommended to review and verify the suggested corrections manually to ensure correctness.