Package/Script Name: Drawing Guess AI

Short description of package/script: This is a simple Python script that allows the user to play a Drawing Guess game against an AI opponent. The user draws an object on the screen, and the AI attempts to guess the object based on a predefined list of objects.

Functionalities/Scripts:

choose_word(): Selects a random word from a predefined list of objects.
draw_object(word): Instructs the user to draw the chosen word on the screen (in a complete game, this could be replaced with a graphical user interface).
guess_object(): Prompts the user to enter their guess for the drawn object and returns the guess in lowercase for comparison.
main(): Implements the main game loop, where the user draws an object, and the AI repeatedly guesses the object until it's correct.
Setup Instructions:

Make sure you have Python installed on your system.
Download the Drawing Guess AI script from the provided source.
Save the script in a directory of your choice.
Explain how to set up and run your package/script on the user's system:

Open a terminal or command prompt.
Navigate to the directory where you saved the Drawing Guess AI script using the cd command.
Run the script using the command: python drawing_guess_ai.py
The game will start, and the user will be prompted to draw an object based on the chosen word.
After drawing, the user can enter their guess for the object drawn, and the AI will respond if it's correct or not.
Detailed Explanation:
The script defines four functions to implement the Drawing Guess AI game. The choose_word() function selects a random word from the predefined list of objects, and the draw_object(word) function instructs the user to draw the chosen word (this part could be enhanced with a GUI for drawing in a complete game). The guess_object() function prompts the user to enter their guess for the drawn object and returns the guess in lowercase for case-insensitive comparison. The main() function implements the main game loop, where the user draws an object, and the AI repeatedly guesses the object until it's correct.

Output:
The output of the script will be displayed in the terminal or command prompt. After the user draws an object and enters their guess, the AI will respond if the guess is correct or not. If the guess is correct, the game will congratulate the user, and if not, it will prompt the user to try again until the correct object is guessed.

Author(s):
Author: Shikhar9425
