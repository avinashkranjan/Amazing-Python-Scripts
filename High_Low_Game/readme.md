Celebrity Social Media Follower Comparison Game

This is a simple Python program that allows users to play a game where they compare the number of followers of two celebrities. The game presents two celebrities and asks the user to guess which one has more followers on a social media platform.

Getting Started

1) Clone the repository or download the code files to your local machine.
2) Make sure you have Python installed on your system (version 3 or above).
3) Install the required dependencies 

How to Play

1) When you run the script, the game will start and display two celebrities along with their descriptions and countries.
2) You will be prompted to enter your guess by typing 'A' or 'B', representing the respective celebrities.
3) If your guess is correct, the program will update your score and present the next pair of celebrities.
4) If your guess is incorrect, the program will display your final score and end the game.

Customization

You can customize the game by modifying the game_data.py file. The file contains a list of dictionaries, where each dictionary represents a celebrity and includes the following information:

name: The name of the celebrity
description: A brief description of the celebrity
country: The country the celebrity is from
follower_count: The number of followers the celebrity has on a social media platform
You can add or remove celebrities from the list or modify their information to create your own version of the game.

Dependencies
random: Used for randomly selecting celebrities from the game_data list.
art: Used for displaying ASCII art in the game interface.