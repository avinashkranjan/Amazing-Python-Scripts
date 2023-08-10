import random
import string
import time

# Existing code (is_valid_word, is_valid_move, word_list)

# Additional features


def get_word_length_difficulty(difficulty):
    if difficulty == "Easy":
        return 3
    elif difficulty == "Medium":
        return 4
    elif difficulty == "Hard":
        return 5
    else:
        raise ValueError("Invalid difficulty level.")


def get_random_letter():
    return random.choice(string.ascii_lowercase)


def get_hint(prev_word):
    # Simple hint: Suggest a valid word with one letter change from prev_word
    for _ in range(10):  # Try 10 times to find a hint
        new_word = prev_word[:3] + get_random_letter() + prev_word[4:]
        if is_valid_word(new_word) and is_valid_move(prev_word, new_word):
            return new_word
    return None  # Return None if a hint can't be found


def word_chain_game():
    # Existing code

    print("Select Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    level_choice = input("Enter the level number: ")

    if level_choice == "1":
        difficulty = "Easy"
    elif level_choice == "2":
        difficulty = "Medium"
    elif level_choice == "3":
        difficulty = "Hard"
    else:
        print("Invalid choice. Defaulting to Easy difficulty.")
        difficulty = "Easy"

    word_length_required = get_word_length_difficulty(difficulty)

    print(f"Difficulty Level: {difficulty}")

    # Optional: Implement a timer for each turn
    def set_timer():
        return time.time()

    def check_time_elapsed(start_time, max_time):
        return time.time() - start_time > max_time

    max_turn_time = 30  # Maximum time in seconds per turn

    while True:
        # Existing code

        # Optional: Timer
        start_time = set_timer()

        new_word = input("Enter a word: ").strip().lower()

        if check_time_elapsed(start_time, max_turn_time):
            print("Time's up! You took too long to answer. You lose this round.")
            break

        # Optional: Hints
        if new_word.lower() == "hint":
            hint = get_hint(prev_word)
            if hint:
                print(f"Hint: Try using '{hint}'.")
                continue
            else:
                print("Sorry, couldn't find a hint this time.")
                continue

        # Optional: Save and Load
        if new_word.lower() == "save":
            # Implement the save functionality to save the game progress.
            # You can use pickle or JSON to save the state of the game.
            print("Game progress saved.")
            continue
        elif new_word.lower() == "load":
            # Implement the load functionality to resume the saved game.
            # Load the state of the game and continue from there.
            print("Game progress loaded.")
            continue

        # Existing code (validation checks)

        # Calculate points based on word length
        points = len(new_word)

        # Optional: Points for making certain challenging moves
        # For example, bonus points for using certain letters, patterns, etc.

        # Existing code (append new_word to chain, update player_turn)

        # Check if player's word is too short for the difficulty level
        if len(new_word) < word_length_required:
            print(
                f"Word should be at least {word_length_required} letters long for {difficulty} difficulty.")
            print("You lose this round.")
            break

        # Check if the game should end
        if player_turn > 1 and not is_valid_move(chain[-2], chain[-1]):
            print(
                f"Game over! {player_name} cannot find a valid word. {player_name} wins!")
            break


if __name__ == "__main__":
    word_chain_game()
