import random


def round(n):
    pgm = 0
    usr = 0
    for i in range(n):
        ip = int(
            input(
                str(i + 1) +
                ". Enter a number(1-3) \n1. Stone\t2. Paper\t3. Scissors : "))
        cp = random.randint(1, 3)
        print(a[cp - 1])
        if ip == cp:
            print("Draw")
        elif ip + 1 == cp or (ip == 3 and cp == 1):
            pgm += 1
            print("Computer Scored a point")

        elif (ip - 1 == cp or (cp == 3 and ip == 1)):
            usr += 1
            print("You Scored a point")
        else:
            print("You entered a wrong Number")
            i = i - 1
    print("Your score :" + str(usr) + "\nComputer Score :" + str(pgm))
    print("-----Game Over-----")


a = ["stone", "paper", "scissors"]
n = int(input("how many turns you want in a round?"))
while (True):
    round(n)
    s = input("Do you want to play again?(Y/N) : ")
    if s == 'N' or s == 'n':
        break
print("-----Thank you-----")
