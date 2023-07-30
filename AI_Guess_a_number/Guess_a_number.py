
import random


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    print("Press 'y' if my guess is correct, 'l' if your number is lower, or 'h' if your number is higher.")

    low = 1
    high = 100
    guess_count = 0
    correct_guess = False

    while not correct_guess:
        guess = random.randint(low, high)
        print("Is your number", guess, "?")
        user_input = input("Enter 'y', 'l', or 'h': ")

        if user_input == "y":
            print("I guessed it! Your number is", guess)
            print("I made", guess_count, "guesses.")
            correct_guess = True
        elif user_input == "l":
            high = guess - 1
            guess_count += 1
        elif user_input == "h":
            low = guess + 1
            guess_count += 1
        else:
            print("Invalid input. Please try again.")


play_game()
