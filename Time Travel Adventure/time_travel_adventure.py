import time
import random


def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


def get_choice(prompt, options):
    while True:
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            choice = int(
                input("Enter your choice (1-{}): ".format(len(options))))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid input. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def time_travel_adventure():
    print_slow("Welcome to the Time Travel Adventure!\n")
    print_slow("You find a mysterious time machine and decide to give it a try.")

    inventory = []
    health_points = 100

    # Starting point - Present
    print_slow("\nYou are in the present time.")
    choice = get_choice("Where would you like to travel?", [
                        "Go to the past", "Go to the future", "Go to the Medieval Era", "Go to the Space Age"])

    if choice == 1:
        print_slow("\nYou traveled to the past.")
        # Past storyline and choices here
        print_slow("You encountered dinosaurs in the past.")
        choice = get_choice("What do you do?", [
                            "Try to befriend them", "Run away"])
        if choice == 1:
            print_slow(
                "You manage to befriend a baby dinosaur. It's a heartwarming moment!")
            inventory.append("Dinosaur Egg")
        else:
            print_slow(
                "You ran away from the dinosaurs and found yourself back in the present.")
    elif choice == 2:
        print_slow("\nYou traveled to the future.")
        # Future storyline and choices here
        print_slow("You arrived in a futuristic city.")
        choice = get_choice("What do you do?", [
                            "Explore the city", "Seek help from locals"])
        if choice == 1:
            print_slow(
                "You explored the city and had a fascinating experience in the future.")
            health_points -= 20
        else:
            print_slow(
                "The locals are friendly and offer you a tour of their advanced technology.")
            inventory.append("Futuristic Device")
    elif choice == 3:
        print_slow("\nYou traveled to the Medieval Era.")
        # Medieval storyline and choices here
        print_slow("You find yourself in a medieval kingdom.")
        choice = get_choice("What do you do?", [
                            "Attend a royal feast", "Help a poor villager"])
        if choice == 1:
            print_slow(
                "You attended a grand feast at the castle. The king was impressed by your presence.")
            inventory.append("Royal Medal")
        else:
            print_slow(
                "You helped the villager, who turned out to be a powerful sorcerer. He grants you a magical amulet.")
            inventory.append("Amulet of Power")
    else:
        print_slow("\nYou traveled to the Space Age.")
        # Space Age storyline and choices here
        print_slow("You are on a space station orbiting a distant planet.")
        choice = get_choice("What do you do?", [
                            "Investigate the planet", "Repair the space station"])
        if choice == 1:
            print_slow(
                "You embarked on a planetary exploration mission and made significant scientific discoveries.")
            inventory.append("Alien Artifact")
        else:
            print_slow(
                "You successfully repaired the space station and gained the respect of the space crew.")
            inventory.append("Space Suit")

    if health_points <= 0:
        print_slow("\nYour health is too low to continue the journey. Game Over!")
    else:
        # Random event during time travel
        if random.random() < 0.3:
            print_slow(
                "\nDuring your time travel, you encounter a time vortex!")
            print_slow("You got disoriented but managed to find your way back.")
            health_points -= 10

        print_slow("\nYou are back in the present time.")
        choice = get_choice("What would you like to do?", [
                            "End the game", "Continue the adventure"])
        if choice == 1:
            print_slow("\nThanks for playing the Time Travel Adventure!")
        else:
            print_slow("You decide to embark on another time travel adventure!")
            time_travel_adventure()


if __name__ == "__main__":
    time_travel_adventure()
