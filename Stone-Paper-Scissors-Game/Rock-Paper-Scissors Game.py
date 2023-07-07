import random


def get_user_input():
    while True:
        try:
            ip = int(
                input("Enter a number (1-3):\n1. Stone\t2. Paper\t3. Scissors: "))
            if ip in [1, 2, 3]:
                return ip
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif user_choice + 1 == computer_choice or (user_choice == 3 and computer_choice == 1):
        return "Computer"
    else:
        return "User"


def round(n):
    pgm = 0
    usr = 0

    for i in range(n):
        ip = get_user_input()
        cp = random.randint(1, 3)
        print(a[cp - 1])

        winner = determine_winner(ip, cp)
        if winner == "Draw":
            print("Draw")
        elif winner == "Computer":
            pgm += 1
            print("Computer scored a point")
        else:
            usr += 1
            print("You scored a point")

    print("Your score: {}\nComputer Score: {}".format(usr, pgm))
    print("-----Game Over-----")


a = ["stone", "paper", "scissors"]
n = int(input("How many turns do you want in a round?"))

while True:
    round(n)
    s = input("Do you want to play again? (Y/N): ")
    if s.upper() == 'N' or s == '0' or s[0] == '-':
        break

print("-----Thank you-----")
