import time
import random


def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()


def intro():
    print_slow("Welcome to the Haunted House!")
    print_slow(
        "You find yourself standing in front of a spooky old house on a dark, stormy night.")
    print_slow(
        "Legend has it that the house is haunted, but you are determined to uncover the mystery.")
    print_slow("You decide to enter the house.")


def show_inventory(inventory):
    print_slow("Inventory:")
    if not inventory:
        print_slow("Your inventory is empty.")
    else:
        for item in inventory:
            print_slow(f"- {item}")


def ask_riddle():
    riddles = [
        {
            'question': "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            'answer': "an echo"
        },
        {
            'question': "The more you take, the more you leave behind. What am I?",
            'answer': "footsteps"
        },
        {
            'question': "What has keys but can't open locks?",
            'answer': "a piano"
        }
    ]

    riddle = random.choice(riddles)
    print_slow(riddle['question'])
    attempts = 3
    while attempts > 0:
        answer = input("Enter your answer: ").lower()
        if answer == riddle['answer']:
            print_slow("Correct! The ghost is pleased and vanishes.")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print_slow(
                    f"Incorrect! You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
            else:
                print_slow(
                    "Incorrect! The ghost becomes angry and attacks you.")
                print_slow(
                    "You wake up outside the haunted house with all your progress reset.")
                main()
                return False


def left_door(inventory):
    print_slow("You enter a dusty library with cobwebs everywhere.")
    print_slow("You notice a book lying on the table.")
    print_slow("Do you want to read the book? (yes/no)")
    choice = input("Enter your choice: ").lower()
    if choice == 'yes':
        print_slow("You open the book and a ghostly figure appears!")
        print_slow("The ghost challenges you to a riddle.")
        if ask_riddle():
            inventory.append('Book')
        else:
            return
    elif choice == 'no':
        print_slow("You decide not to read the book and leave the library.")
    else:
        print_slow("Invalid choice. Please enter 'yes' or 'no'.")
        left_door(inventory)
    choose_path(inventory)


def hide_and_seek():
    hiding_spots = ['under the bed', 'behind the curtains',
                    'inside the wardrobe', 'under the table']
    hidden_spot = random.choice(hiding_spots)

    print_slow(
        "The creepy doll disappears, and you hear eerie giggles echoing in the room.")
    print_slow("You realize the doll is playing hide-and-seek with you!")
    print_slow("You have 3 attempts to find where the doll is hiding.")

    for attempt in range(3):
        print_slow(f"Attempt {attempt + 1}: Where do you want to search?")
        print_slow(
            "Choose from: under the bed, behind the curtains, inside the wardrobe, under the table")
        guess = input("Enter your choice: ").lower()

        if guess == hidden_spot:
            print_slow("Congratulations! You found the doll!")
            print_slow("The doll rewards you with a key.")
            return True
        else:
            print_slow("Nope, the doll isn't there.")

    print_slow(
        "You couldn't find the doll, and it reappears with a mischievous grin.")
    print_slow("You leave the room empty-handed.")
    return False


def right_door(inventory):
    print_slow(
        "You enter a dimly lit room with a creepy doll sitting in a rocking chair.")
    print_slow("The doll suddenly comes to life and speaks to you.")
    print_slow("It asks you to play a game of hide-and-seek.")

    if hide_and_seek():
        inventory.append('Key')


def choose_path(inventory):
    print_slow("You step into the entrance hall and see two doors.")
    print_slow("Do you want to go through the 'left' door or the 'right' door?")
    choice = input("Enter your choice: ").lower()
    if choice == 'left':
        left_door(inventory)
    elif choice == 'right':
        right_door(inventory)
    else:
        print_slow("Invalid choice. Please enter 'left' or 'right'.")
        choose_path(inventory)


def main():
    intro()
    inventory = []
    choose_path(inventory)
    show_inventory(inventory)


if __name__ == "__main__":
    main()
