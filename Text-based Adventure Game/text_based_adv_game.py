import time


def print_delay(text, delay=1):
    print(text)
    time.sleep(delay)


def intro():
    print_delay("You wake up in a dark, mysterious room.")
    print_delay("You can't remember how you got here.")
    print_delay("As you look around, you see two doors in front of you.")
    print_delay("One door is red, and the other door is blue.")


def choose_door():
    door = ""
    while door != "red" and door != "blue":
        door = input("Which door do you choose? (red/blue): ").lower()
    return door


def red_door_scenario():
    print_delay("You open the red door and find yourself in a fiery cave.")
    print_delay("There's a dragon sleeping in the middle of the cave!")
    print_delay("You can either:")
    print_delay("1. Try to sneak around the dragon.")
    print_delay("2. Grab a nearby sword and fight the dragon.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print_delay("You try to sneak around the dragon.")
        print_delay("Unfortunately, the dragon wakes up and chases you!")
        print_delay("You barely manage to escape through the red door.")
        print_delay("You return to the initial room.")
        play_game()
    elif choice == "2":
        print_delay("You pick up the sword and bravely attack the dragon.")
        print_delay("After an intense battle, you defeat the dragon!")
        print_delay("You find a treasure chest behind the dragon's nest.")
        print_delay("The chest contains valuable gems and gold!")
        print_delay("Congratulations! You win!")
    else:
        print_delay("Invalid choice. Please enter 1 or 2.")
        red_door_scenario()


def blue_door_scenario():
    print_delay("You open the blue door and find yourself in a peaceful garden.")
    print_delay("There's a friendly fairy sitting on a bench.")
    print_delay("The fairy offers you a magical potion.")
    print_delay("You can either:")
    print_delay("1. Drink the potion.")
    print_delay("2. Politely decline the offer.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print_delay("You drink the potion and feel a sudden burst of energy.")
        print_delay("Your memory is restored, and you remember everything!")
        print_delay("The fairy thanks you for accepting her gift.")
        print_delay("You have a new friend now!")
        print_delay("Congratulations! You win!")
    elif choice == "2":
        print_delay("You politely decline the potion.")
        print_delay("The fairy understands and smiles at you.")
        print_delay("You feel a sense of peace in the garden.")
        print_delay(
            "You've chosen a different path, but it's still a happy ending.")
        print_delay("Congratulations! You win!")
    else:
        print_delay("Invalid choice. Please enter 1 or 2.")
        blue_door_scenario()


def secret_room_scenario():
    print_delay("You find a hidden passage behind the bookshelf.")
    print_delay("You enter a mysterious room filled with ancient artifacts.")
    print_delay("In the center of the room, there's a glowing amulet.")
    print_delay("You can either:")
    print_delay("1. Take the amulet.")
    print_delay("2. Leave the room without taking anything.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print_delay(
            "You take the amulet, and it starts to shine even brighter.")
        print_delay("Suddenly, you feel a surge of power flowing through you.")
        print_delay("You've unlocked hidden abilities!")
        print_delay("Congratulations! You win!")
    elif choice == "2":
        print_delay("You decide not to touch anything and leave the room.")
        print_delay("As you exit the secret room, you feel a sense of relief.")
        print_delay(
            "You've chosen a different path, but it's still a happy ending.")
        print_delay("Congratulations! You win!")
    else:
        print_delay("Invalid choice. Please enter 1 or 2.")
        secret_room_scenario()


def play_game():
    intro()
    chosen_door = choose_door()

    if chosen_door == "red":
        red_door_scenario()
    elif chosen_door == "blue":
        blue_door_scenario()

    print_delay(
        "You continue exploring and find a hidden door behind a bookshelf.")
    print_delay("Do you want to open the door?")
    hidden_door_choice = input("Enter 'yes' or 'no': ").lower()

    if hidden_door_choice == "yes":
        secret_room_scenario()
    else:
        print_delay(
            "You decide not to open the hidden door and continue your adventure.")


if __name__ == "__main__":
    play_game()
