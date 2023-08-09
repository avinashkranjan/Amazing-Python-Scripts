**Package/Script Name:** Gomoku (Connect Five) Game

**Short Description:** This is a simple Python script for playing the classic Gomoku (Connect Five) game in a text-based format. Two players take turns placing their pieces (X or O) on the board, and the first player to connect five pieces in a row horizontally, vertically, or diagonally wins the game.

**Functionalities:**
- Create a Gomoku board of a specified size.
- Display the Gomoku board with player pieces.
- Check for a win condition (five in a row) for each player.
- Handle player moves and validate the moves.
- Determine a draw when the board is full.
- Play the game until a player wins or the board is full.

**Setup Instructions:**
1. Make sure you have Python installed on your system. If you don't have it, you can download it from the official website: https://www.python.org/downloads/
2. Copy and paste the provided script into a new file named `gomoku.py` or any desired name.
3. Save the file in the desired directory.

**How to Run the Script:**
1. Open a terminal or command prompt.
2. Navigate to the directory where you saved the `gomoku.py` file using the `cd` command.
3. Run the script by entering the following command:

```
python gomoku.py
```

**Detailed Explanation:**
The script begins by defining the `create_board` function, which initializes a Gomoku board with empty spaces. The `display_board` function is used to print the current state of the board with player pieces. The `check_win` function checks whether a player has won the game by connecting five pieces in a row.

In the `gomoku` function, the game loop runs until a player wins or the board is full. The players take turns making moves, and each move is validated to ensure it falls within the board boundaries and does not overlap with an existing piece. The script also checks for a draw when the board is full.

**Output:**
When running the script, the output will be text-based, displaying the current state of the Gomoku board, player moves, and messages for the game's progress. The script will print the board after each player's move. If a player wins, the script will display a congratulatory message. If the board is full without a winner, it will announce a draw.

As this is a text-based game, there are no images, gifs, or videos to display for the output.

**Author:**
Shikhar9425
