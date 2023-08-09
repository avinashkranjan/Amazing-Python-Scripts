# SCRABBLE

## Definition
This project is the Scrabble game which can be played between many players.

### Project structure :

- scrabble.py
- requirements.txt
- README.md

## Libraries
### PyDictionary:
Returns meaning, synonyms, antonyms for a word (scraping dictionary.com) limit the no of results also get meaning, synonyms and antonyms in different color..[seemore](https://pypi.org/project/Py-Dictionary/)

## Installing Libraries
The requirements.txt file that has the library used which simply can be used to install the libraries through the package manager [pip](https://pip.pypa.io/en/stable/).

```bash
pip install -r requirements.txt
```
## Usage
```bash
python scrabble.py
```
The players can exit the game by typing Y or else continue the game by Enter.
```python
**********Welcome to the Scrabble game**********
Let's start playing!!

How many players? 2
Player 1: A
Player 2: B
****************************************

A | Type a word: hat
B | Type a word: pot
If exit, type Y:
```

## Functioning
The project.py contains 6 functions including the main function.
Main function prints out the user interface of the game.

### valid(word) function :
This function takes a word and check its validity by looking for its availability in the PyDictionary. If it is available, returns True else it returns False

### compute_score(word) function :
This function computes and outputs the score of a word. If the word is not alphabetic or if the word is not valid, exceptions are arisen.

### player_count() function :
This function prompt the user for an input of number of players. Until a valid integer is typed, the function is called. Finally the count is returned.

### get_input(score_board) function :
This function takes an empty scoreboard dictionary, prompts the players to type their words in number of rounds until the exit term Y is typed and the scores are added simultaneously. Whenever a player types an invalid format of word, the player will be requested again. The function returns a dictionary scoreboard of the players with their score

### winner(score_board) function :
This function takes the scoreboard and finds the winner or winners, then output the result announcement accordingly.

## Author: Nashira
