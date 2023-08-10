import random
import time


dice_faces = [
    [' ------- ',
     '|       |',
     '|   O   |',
     '|       |',
     ' ------- '],

    [' ------- ',
     '| O     |',
     '|       |',
     '|     O |',
     ' ------- '],

    [' ------- ',
     '| O     |',
     '|   O   |',
     '|     O |',
     ' ------- '],

    [' ------- ',
     '| O   O |',
     '|       |',
     '| O   O |',
     ' ------- '],

    [' ------- ',
     '| O   O |',
     '|   O   |',
     '| O   O |',
     ' ------- '],

    [' ------- ',
     '| O   O |',
     '| O   O |',
     '| O   O |',
     ' ------- ']


]


def roll_dice():
    return random.randint(1, 6)


def print_dice(dice_value):
    for line in dice_faces[dice_value - 1]:
        print(line)


def print_two_dice(dice_values):
    for i in range(5):
        print(dice_faces[dice_values[0] - 1][i],
              "   ", dice_faces[dice_values[1] - 1][i])


def play_game():
    level = input("Select level (easy/difficult): ").lower()

    if level == "easy":
        actual_roll = roll_dice()
        print("Guess the outcome of a dice roll (1 to 6).")
    elif level == "difficult":
        actual_rolls = [roll_dice(), roll_dice()]
        actual_roll = sum(actual_rolls)
        print("Guess the sum of two dice rolls (2 to 12).")
    else:
        print("Invalid level choice.")
        return

    try:
        user_guess = int(input())
        if (1 <= user_guess <= 6 and level == "easy") or (2 <= user_guess <= 12 and level == "difficult"):
            print("\nRolling the dice...")
            time.sleep(1)

            if level == "difficult":
                print_two_dice(actual_rolls)
            else:
                print_dice(actual_roll)

            if user_guess == actual_roll:
                print("Congratulations! You win!")
            else:
                print("Oops! You lose.")
        else:
            print("Invalid guess. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    print("Welcome to the Dice Roll Guessing Game!")
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thank you for playing!")
