Package/Script Name: Game of Fifteen (15-puzzle)

Short Description: This is a simple Python script for playing the classic Game of Fifteen, also known as the 15-puzzle. The script generates a 4x4 grid with numbers from 1 to 15 randomly shuffled, leaving one empty space. The player's objective is to rearrange the numbers in numerical order by sliding the tiles into the empty space.

Functionalities:

Create and shuffle the initial 4x4 board with numbers from 1 to 15 and an empty space.
Display the current state of the board in the terminal.
Allow the player to make valid moves by sliding tiles to the empty space.
Check for a win condition when the numbers are arranged in numerical order, and the empty space is in the bottom-right corner.
Allow the player to quit the game at any time.
Setup Instructions:

Make sure you have Python installed on your system. If you don't have it, you can download it from the official website: https://www.python.org/downloads/
Copy and paste the provided script into a new file named game_of_fifteen.py or any desired name.
Save the file in the desired directory.
How to Run the Script:

Open a terminal or command prompt.
Navigate to the directory where you saved the game_of_fifteen.py file using the cd command.
Run the script by entering the following command:
Copy code
python game_of_fifteen.py
Detailed Explanation:
The script begins by defining functions for creating the initial board, displaying the board, checking valid moves, and checking for a win condition. The create_board function generates a shuffled 4x4 board, and the display_board function prints the current state of the board in the terminal.

The main game_of_fifteen function runs the game loop until the player wins or quits. It prompts the player to enter a number to move, validates the input, and slides the selected tile to the empty space if the move is valid. The game continues until the player solves the puzzle or quits.

Output:
When running the script, the output will be text-based, displaying the current state of the Game of Fifteen board and messages for the player's moves and the game's progress. The script will print the board after each player's move.

As this is a text-based game, there are no images, gifs, or videos to display for the output.

Author:
Shikhar9425
