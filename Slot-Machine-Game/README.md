# Slot Machine Game

This is a simple command-line slot machine game written in Python. The game allows you to bet on multiple lines and spin the slot machine. The game has predefined symbols with corresponding values. If the symbols on a line match, you win money based on the symbol's value and your bet amount.

## How to Play

1. Run the `slot_machine.py` script.
2. You will be prompted to deposit an initial amount of money.
3. Enter the number of lines you want to bet on (between 1 and the maximum allowed lines).
4. Specify the bet amount for each line (between the minimum and maximum allowed bets).
5. The slot machine will be displayed, showing the randomized symbols in a 3x3 grid.
6. If you win, the game will display the amount you won and the line(s) on which you won.
7. The game will then prompt you for another spin until you decide to quit by pressing 'q'.
8. Once you quit the game, it will display the final balance you have left.

## Symbols and Values

The slot machine has four predefined symbols: A, B, C, and D. Each symbol has a specific count and value associated with it, which determines the winnings.

Symbol Count:
- A: 2
- B: 4
- C: 6
- D: 8

Symbol Value:
- A: $5
- B: $4
- C: $3
- D: $2

## Betting Rules

- You can bet on a minimum of 1 line and a maximum of 3 lines.
- The bet amount per line must be between $1 and $100.

## Notes

- This is a simple simulation of a slot machine for entertainment purposes only.
- The game uses Python's `random` module to generate random symbols for each spin.

Have fun playing the slot machine game!

## Author 
[Khushi Marothi](https://github.com/khushimarothi)
