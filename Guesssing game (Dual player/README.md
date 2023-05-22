# Number Guessing Game

This is a simple number guessing game implemented in Python. The game randomly selects a number between 1 and 100, and the players take turns guessing the number. The player who guesses the correct number wins the game.

## Prerequisites

- Python 3.x

## Getting Started

1. Clone the repository or download the Python script file.
2. Run the script using a Python interpreter.

```shell
python number_guessing_game.py
```

## Instructions

1. Enter the names of the two players when prompted.
2. The game starts with a coin toss to determine the first player.
3. Each player takes turns guessing the number.
4. If the guessed number is equal to the random number, the player wins the game.
5. If the guessed number is higher or lower than the random number, the player receives a hint to adjust their guess accordingly.
6. The game continues until one of the players guesses the correct number.
7. The winner's name is displayed along with the number of steps taken to guess the correct number.
8. The game ends, and the result is shown.

## Example

```
-----------GAME START------------

Enter your name: Player 1
Enter your name: Player 2

Player 1 won the toss!

Enter Player 1's guess: 50
Enter a smaller number

Enter Player 2's guess: 25
Enter a bigger number

Enter Player 1's guess: 35
Congratulations! Player 1 guessed the correct number in 3 steps.

-----------GAME OVER--------------

Winner: Player 1
Number of steps: 3

----------------------------------
```

## Acknowledgments

- This game was created as a learning exercise in Python programming.
- The code is intended for educational purposes and can be customized and enhanced as needed.

Feel free to customize and modify the code according to your preferences. Happy gaming!
