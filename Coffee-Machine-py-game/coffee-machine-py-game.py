class CoffeeMachine:
    def __init__(self):
        self.water = 500
        self.milk = 500
        self.coffee_beans = 200
        self.cups = 10
        self.money = 0

    def check_resources(self, water_needed, milk_needed, coffee_beans_needed, cups_needed):
        if self.water < water_needed:
            return "Sorry, not enough water."
        elif self.milk < milk_needed:
            return "Sorry, not enough milk."
        elif self.coffee_beans < coffee_beans_needed:
            return "Sorry, not enough coffee beans."
        elif self.cups < cups_needed:
            return "Sorry, not enough cups."
        else:
            return "Enough resources. Enjoy your coffee!"

    def buy_coffee(self, choice):
        if choice == "espresso":
            water_needed = 50
            milk_needed = 0
            coffee_beans_needed = 18
            cups_needed = 1
            price = 1.50
            coffee_type = "Espresso"
        elif choice == "latte":
            water_needed = 200
            milk_needed = 150
            coffee_beans_needed = 24
            cups_needed = 1
            price = 2.50
            coffee_type = "Latte"
        elif choice == "cappuccino":
            water_needed = 250
            milk_needed = 100
            coffee_beans_needed = 24
            cups_needed = 1
            price = 3.00
            coffee_type = "Cappuccino"
        else:
            message = "Invalid choice. Please try again."
            return message

        message = self.check_resources(water_needed, milk_needed, coffee_beans_needed, cups_needed)
        if message == "Enough resources. Enjoy your coffee!":
            print(f"Please insert coins for {coffee_type} (${price}):")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            total_amount = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
            if total_amount < price:
                return "Insufficient amount. Money refunded."
            else:
                change = round(total_amount - price, 2)
                self.money += price
                self.water -= water_needed
                self.milk -= milk_needed
                self.coffee_beans -= coffee_beans_needed
                self.cups -= cups_needed
                return f"Here is ${change} in change. Here is your {coffee_type}. Enjoy!"

        return message


def main():
    coffee_machine = CoffeeMachine()

    while True:
        print("============================================")
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice in ["espresso", "latte", "cappuccino"]:
            print(coffee_machine.buy_coffee(choice))
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
