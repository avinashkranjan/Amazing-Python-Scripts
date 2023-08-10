import random


def generate_doors(num_doors):
    doors = [False] * num_doors
    prize_door = random.randint(0, num_doors - 1)
    doors[prize_door] = True
    return doors


def choose_door(num_doors):
    return random.randint(0, num_doors - 1)


def open_door(doors, chosen_door):
    reveal_door = random.choice(
        [i for i in range(len(doors)) if i != chosen_door and not doors[i]])
    print(f"Door {reveal_door + 1} has no prize.")


def switch_door(chosen_door, num_doors):
    return random.choice([i for i in range(num_doors) if i != chosen_door])


def main():
    num_doors = 3
    doors = generate_doors(num_doors)

    print("Welcome to the Door Puzzle AI!")
    print("There are three doors. Behind one of the doors is a prize.")
    print("You need to choose a door, and then we will reveal one door that does not have the prize.")
    print("You will then have the option to switch your chosen door or stick with the current choice.")
    print("Let's get started!")

    chosen_door = choose_door(num_doors)
    print(f"\nYou have chosen Door {chosen_door + 1}.")

    open_door(doors, chosen_door)

    switch_choice = input(
        "Do you want to switch your chosen door? (yes/no): ").lower()

    if switch_choice == "yes":
        chosen_door = switch_door(chosen_door, num_doors)

    if doors[chosen_door]:
        print("Congratulations! You have won the prize!")
    else:
        print("Sorry, you did not win this time. Better luck next time!")


if __name__ == "__main__":
    main()
