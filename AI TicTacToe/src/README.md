# TicTacToe Game

A simple implementation of the Tic Tac Toe game in Python.

## Rules of the Game
Tic Tac Toe is a classic game played on a 3x3 grid. Two players take turns placing their markers (X or O) on the board, aiming to get three of their marks in a row (horizontally, vertically, or diagonally) before the opponent does. If all the positions on the board are filled and no player has won, the game ends in a tie.

## How to Play
1. Run the `play_tic_tac_toe()` function in a Python environment.
2. Player 1 will be prompted to choose either X or O.
3. The players will take turns entering their positions on the board, ranging from 1 to 9. The board is displayed after each move.
4. The game continues until one player wins or the board is full.
5. After the game ends, players are given the option to play again.

## Functions
- `display_board(board)`: Prints the current state of the Tic Tac Toe board.
- `player_input()`: Prompts the first player to choose X or O and assigns the markers to player 1 and player 2 accordingly.
- `place_marker(board, marker, position)`: Places the given marker (X or O) at the specified position on the board.
- `win_check(board, mark)`: Checks if the given mark (X or O) has won the game.
- `choose_first()`: Randomly selects which player goes first.
- `space_check(board, position)`: Checks if a particular position on the board is empty.
- `full_board_check(board)`: Checks if the board is full.
- `player_choice(board)`: Asks the current player to choose a position to place their marker and returns the chosen position.
- `replay()`: Asks the players if they want to play again.

## Usage
1. Clone the repository or download the `tic_tac_toe.py` file.
2. Open the file in a Python environment (e.g., IDLE, Jupyter Notebook, or any text editor with Python support).
3. Run the script to start the game.
4. Follow the prompts and enter your choices accordingly.
5. Enjoy playing Tic Tac Toe!
