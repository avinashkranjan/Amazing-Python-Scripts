"""
AI Calculator using ChatterBot with mathematical evaluation logic.
"""

import os
from chatterbot import ChatBot


def main() -> None:
    """Initialize the calculator chatbot and run the main interactive loop."""
    # Initialize the ChatBot calculator with mathematical evaluation logic
    bot = ChatBot(
        name="Calculator",
        read_only=True,
        logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
    )

    # Clear the screen and start the calculator
    os.system("cls" if os.name == "nt" else "clear")
    print("Hello, I am a calculator. How may I help you?")

    while True:
        # Take input from the user
        user_input = input("me: ")

        # Check if the user wants to exit the program
        if user_input.lower() == "quit":
            print("Exiting")
            break

        # Evaluate the user input or catch errors
        try:
            response = bot.get_response(user_input)
            print(f"Calculator: {response}")
        except Exception:
            print("Calculator: Please enter valid input.")


if __name__ == "__main__":
    main()
