import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
        + "Rock vs Scissors -> Rock wins \n"
        + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice: "))

    # looping until the user enters a valid input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please: '))

    # initialize the value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # print the user's choice
    print('User choice is:', choice_name)
    print('Now it\'s the Computer\'s Turn....')

    # Computer chooses randomly any number
    # among 1, 2, and 3 using randint method
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # initialize the value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    # we need to check for a draw
    if choice == comp_choice:
        print('It\'s a Draw', end="")
        result = "DRAW"

    # condition for winning
    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 3) or
            (choice == 3 and comp_choice == 1)):
        print('Computer wins =>', end="")
        result = 'Computer'
    else:
        print('You win =>', end="")
        result = 'User'

    # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== It's a tie ==>")
    elif result == 'User':
        print("<== You win ==>")
    else:
        print("<== Computer wins ==>")

    print("Do you want to play again? (Y/N)")

    # if user input n or N, then the condition is True
    ans = input().lower()
    if ans == 'n':
        break

# after coming out of the while loop
# we print thanks for playing
print("Thanks for playing")
