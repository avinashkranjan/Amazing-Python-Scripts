Package/Script Name: Door Puzzle AI

Short description of package/script: This is a simple Python script that allows the user to play a Door Puzzle game against an AI opponent. The user needs to choose one door out of three, and the AI will reveal a door without the prize. The user then has the option to switch their chosen door or stick with the current choice to win the prize.

Functionalities/Scripts:

generate_doors(num_doors): Generates a list of doors, where one door contains the prize (True) and the others don't (False).
choose_door(num_doors): Allows the user to select a door number from 1 to the total number of doors.
open_door(doors, chosen_door): Reveals a door that does not have the prize, except for the chosen door.
switch_door(chosen_door, num_doors): Allows the user to switch their chosen door.
Setup Instructions:

Make sure you have Python installed on your system.
Download the Door Puzzle AI script from the provided source.
Save the script in a directory of your choice.
Explain how to set up and run your package/script on the user's system:

Open a terminal or command prompt.
Navigate to the directory where you saved the Door Puzzle AI script using the cd command.
Run the script using the command: python door_puzzle_ai.py
The game will start, and the user will be prompted to choose one door out of three.
After choosing, the AI will reveal one door that doesn't have the prize.
The user will then have the option to switch their chosen door or stick with the current choice.
The script will reveal whether the user has won the prize or not.
Detailed Explanation:
The script defines four functions to implement the Door Puzzle AI game. The generate_doors(num_doors) function generates a list of doors, where one door contains the prize (True) and the others don't (False). The choose_door(num_doors) function allows the user to select a door number from 1 to the total number of doors. The open_door(doors, chosen_door) function reveals a door that doesn't have the prize, except for the chosen door. The switch_door(chosen_door, num_doors) function allows the user to switch their chosen door.

Output:
The output of the script will be displayed in the terminal or command prompt. After the user chooses a door and optionally switches their choice, the script will reveal whether the user has won the prize or not. The game outcome will be displayed in the terminal.

Author(s):
Author: Shikhar9425
