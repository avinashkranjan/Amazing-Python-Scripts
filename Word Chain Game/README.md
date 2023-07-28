# Word Chain Game - README

## Description
Word Chain is a word-based puzzle game built in Python. Players take turns adding a single letter to a growing word, with the goal of forming a chain of words, each related to the previous one by changing just one letter. The longer the chain, the higher the score! This game also includes various additional features to enhance gameplay.

## Features
- Difficulty Levels: Choose from Easy, Medium, or Hard difficulty levels, each requiring a minimum word length.
- Time Limit: Players have a time limit to provide a word; otherwise, they lose the round.
- Points System: Earn points based on word length, with bonus points for challenging moves.
- Hints: Request a hint if you're stuck, and the game will provide a related word to help.
- Save and Load: Save your game progress and load it later to continue where you left off.
- Multiplayer Online: Play the game online with friends from different locations.
- Power-ups: Use power-ups for advantages, such as changing a letter in the previous word.
- Custom Word Lists: Choose from different word categories or create your custom word lists.

## Getting Started
1. Install Python 3.x on your computer.
2. Install the required dependencies using the following command:
```bash
pip install nltk
```
3. Run the game by executing the `word_chain_game.py` script.

## How to Play
1. Choose a difficulty level (Easy, Medium, or Hard) at the start of the game.
2. Players take turns providing words that change just one letter from the previous word.
3. Words must be at least three letters long and cannot be repeated in the same chain.
4. Optionally, players can request a hint, save the game progress, or load a saved game.
5. The game continues until a player cannot form a valid word within the time limit or makes an invalid move.

## Acknowledgments
- The word list for this game is obtained from the `nltk` (Natural Language Toolkit) library.
- Special thanks to OpenAI for providing the GPT-3.5 language model that helped generate this README.
