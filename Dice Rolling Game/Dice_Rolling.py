import random


def roll_dice():
    return random.randint(1, 6)


def ai_roll():
    return roll_dice()


def main():
    print("Welcome to Dice Rolling AI!")

    while True:
        user_input = input("Press 'Enter' to roll the dice or 'q' to quit: ")
        if user_input.lower() == 'q':
            print("Thanks for playing!")
            break

        user_roll = roll_dice()
        ai_roll_result = ai_roll()

        print(f"You rolled: {user_roll}")
        print(f"AI rolled: {ai_roll_result}")

        if user_roll > ai_roll_result:
            print("Congratulations! You won!")
        elif user_roll < ai_roll_result:
            print("AI wins! Better luck next time.")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    main()
