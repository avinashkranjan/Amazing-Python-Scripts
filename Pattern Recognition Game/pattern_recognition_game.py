import random
import time


def generate_pattern():
    colors = ["red", "green", "blue", "yellow", "orange", "purple",
              "pink", "brown", "gray", "black", "white", "cyan", "magenta"]
    patterns = [
        ["red", "green", "blue", "yellow", "orange"],
        ["purple", "pink", "brown", "gray", "black"],
        ["white", "cyan", "magenta", "red", "blue", "green"],
        ["brown", "gray", "pink", "red", "blue"],
        ["yellow", "orange", "red", "purple"],
        ["white", "gray", "black", "pink", "cyan", "blue"],
        ["yellow", "green", "orange", "blue"],
        ["magenta", "purple", "green", "cyan", "yellow"],
        ["red", "green", "blue", "yellow", "orange", "purple", "pink"],
        ["red", "blue", "orange", "yellow", "cyan", "magenta"],
        ["blue", "green", "yellow", "orange", "brown"],
        ["cyan", "magenta", "yellow", "gray", "purple"],
        ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan"],
        ["blue", "red", "green", "yellow", "orange", "purple", "brown", "cyan"],
        ["magenta", "purple", "pink", "yellow", "orange", "green", "red", "gray"]
    ]
    pattern = random.choice(patterns)
    return pattern


def get_next_pattern(pattern):
    colors = set(["red", "green", "blue", "yellow", "orange", "purple",
                 "pink", "brown", "gray", "black", "white", "cyan", "magenta"])
    pattern_set = set(pattern)
    missing_color = list(colors - pattern_set)[0]
    next_pattern = pattern[1:] + [missing_color]
    return next_pattern


def play_game():
    print("Welcome to the Pattern Recognition Game!")
    print("Try to identify the underlying rule of the color patterns.")
    print(
        "For example, if the pattern is ['red', 'green', 'blue', 'yellow', 'orange'], the next pattern will be ['green', 'blue', 'yellow', 'orange', 'purple'] (alphabetical order).\n")

    score = 0
    max_attempts = 3
    hint_limit = 1
    time_limit = 20

    while True:
        pattern = generate_pattern()
        print("Pattern:", pattern)

        for attempt in range(max_attempts):
            user_input = input("Enter the next pattern: ").split()

            if user_input == get_next_pattern(pattern):
                score += 1
                print("Correct!")
                break
            else:
                print(
                    f"Wrong! {max_attempts - attempt - 1} attempts remaining.")

        else:
            print(f"\nGame Over! Your score: {score}\n")
            break

        # Give the player a hint option
        if hint_limit > 0:
            hint_choice = input("Would you like a hint? (yes/no): ").lower()
            if hint_choice == "yes":
                hint_limit -= 1
                print("Hint: The next color is", get_next_pattern(pattern)[-1])

        # Introduce levels based on the score
        if score >= 5:
            max_attempts = 2
        if score >= 10:
            time_limit = 15

        # Timer implementation
        start_time = time.time()
        while time.time() - start_time < time_limit:
            pass
        print("\nTime's up!\n")
        print(f"Your score: {score}\n")


if __name__ == "__main__":
    play_game()
