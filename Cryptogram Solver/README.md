# Cryptogram Solver

## Description
Cryptogram Solver is a Python script that automatically decrypts cryptograms. Cryptograms are word puzzles where each letter in the original word is replaced with another letter, and your task is to find the original word. This script uses frequency analysis techniques and a dictionary of words to solve the cryptogram.

## Features
1. **Letter Frequency Visualization**: The script displays a bar chart to visualize the letter frequency in the cryptogram.
2. **Letter Substitution Game**: You can manually guess the letter substitutions to solve the cryptogram.
3. **Hint System**: The script provides frequency analysis of letters to help you make educated guesses.
4. **Save/Load Progress**: Your progress is saved and loaded for future sessions.

## How to Use
1. Install Python on your computer (Python 3.x is recommended).
2. Download the script `cryptogram_solver.py` and the word dictionary file `english.words.txt` (or use your own word dictionary).
3. Run the script using the command `python cryptogram_solver.py`.
4. Enter the cryptogram when prompted.
5. Optionally, enter the path to your word dictionary file.
6. The script will automatically attempt to decrypt the cryptogram using frequency analysis and the word dictionary.
7. After decryption, you can play the letter substitution game, view frequency analysis, and manually modify the decrypted message.

## Requirements
- Python 3.x
- Matplotlib (for letter frequency visualization)
- nltk

## File Structure
- `cryptogram_solver.py`: The main Python script for solving cryptograms.
- `english.words.txt`: A text file containing a list of English words, one word per line, to use as a word dictionary.
- `progress.pickle`: A binary file that stores your progress during decryption.

## Notes
- The success of the decryption depends on the quality of the word dictionary used and the length of the cryptogram.
- The letter frequency analysis may not be perfect for very short cryptograms.
- Have fun and enjoy solving cryptograms!


