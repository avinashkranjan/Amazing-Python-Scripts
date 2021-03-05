#ATM Machine Using python

print("="*30, "Welcome to Python Bank ATM", "="*30)

restart = ("Y")
chances = 3
balance = 999.99

while chances >= 0:
    pin = int(input("\nPlease enter your 4 Digit pin: "))
    if pin == (1234):
        print("\nCorrect pin!!")

        while restart not in ("n", "no", "N", "NO"):
            print("\nPlease Press 1 For Your Balance.")
            print("Please Press 2 To Make a Withdrawl.")
            print("Please Press 3 To Pay in.")
            print("Please Press 4 To Return Card.")

            option = int(input("\nWhat Would you like to Choose?: "))

            if option == 1:
                print(f"\nYour Balance is: ${balance}")
                restart = input("\nWould You like to do something else? (y or n) ")

                if restart in ("n", "no", "N", "NO"):
                    print("\nThank You\n")
                    break

            elif option == 2:
                option2 = ("y")
                withdrawl = float(input("\nHow Much Would you like to withdraw? 10, 20, 40, 60, 80, 100 for other enter 1: "))

                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print(f"\nYour balance after the withdrawl is ${balance}")
                    restart = input("\nWould You like to do something else? (y or n) ")

                    if restart in ("n", "no", "N", "NO"):
                        print("\nThank You\n")
                        break

                elif withdrawl == 1:
                    withdrawl = float(input("\nPlease Enter Desired amount: "))
                    balance = balance - withdrawl
                    print(f"\nYour balance after the withdrawl is ${balance}")
                    restart = input("\nWould You like to do something else? (y or n) ")

                    if restart in ("n", "no", "N", "NO"):
                        print("\nThank You\n")
                        break

                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print("\nINVALID AMOUNT, Please try Again\n")
                    restart = ("y")

            elif option == 3:
                pay_in = float(input("\nHow Much Would you like to Pay In? "))
                balance = balance + pay_in
                print(f"\nYour balance after the Pay-in is ${balance}")
                restart = input("\nWould You like to do something else? (y or n) ")

                if restart in ("n", "no", "N", "NO"):
                    print("\nThank You\n")
                    break

            elif option == 4:
                print("\nPlease wait whilst your card is Returned....")
                print("\nThank you for your service")
                break

            else:
                print("\nPlease enter a correct number.\n")
                restart = ("y")

    elif  pin != (1234):
        print("\nINCORRECT PIN!!\n")
        chances = chances - 1

        if chances == 0:
            print("Calling the Police...\n")
            break