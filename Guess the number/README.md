# Guess the Number Game - README

## Introduction

Welcome to the "Guess the Number" game! This Python script allows you to play a simple guessing game where you have to guess a randomly chosen number between 1 and 100. The game will provide you with feedback for each guess you make, helping you determine whether your guess is too low or too high.

## How to Play

1. **Launch the Game**: Run the Python script (guess_the_number.py) in your preferred Python environment.
2. **Game Rules**: The computer will randomly select a secret number between 1 and 100, which you have to guess.
3. **Making a Guess**: You will be prompted to enter your guess. Input an integer between 1 and 100 and press Enter.
4. **Feedback**: After each guess, the game will provide feedback to help you adjust your next guess:
   - If your guess is correct, you will receive a congratulatory message along with the number of attempts it took you to guess correctly.
   - If your guess is too low, the game will inform you to try a higher number.
   - If your guess is too high, the game will suggest trying a lower number.
5. **Invalid Input Handling**: If you input anything other than a valid integer, the game will notify you and prompt for a new guess.
6. **Keep Guessing**: Continue making guesses until you correctly guess the secret number.

## Example

```
Welcome to Guess the Number Game!
I'm thinking of a number between 1 and 100.
Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 65
Too high! Try again.
Enter your guess: 60
Too low! Try again.
Enter your guess: 62
Congratulations! You guessed the number in 5 attempts.
```

## Requirements

This game is written in Python and requires no external libraries. You can run it using any Python 3.x interpreter.

## Contribution

If you have any ideas or suggestions to enhance the game or improve the code, feel free to contribute! Fork the repository, make your changes, and create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact:

Shivansh Jain
shivanshjain3333@gmail.com
