import random

def generate_secret_code(colors, code_length):
    return [random.choice(colors) for _ in range(code_length)]

def evaluate_guess(secret_code, guess):
    correct_color_and_position = 0
    correct_color_only = 0
    
    for i in range(len(secret_code)):
        if secret_code[i] == guess[i]:
            correct_color_and_position += 1
        elif guess[i] in secret_code:
            correct_color_only += 1
    
    return correct_color_and_position, correct_color_only

def display_colors(colors):
    color_str = "  ".join(colors)
    print(f"Available colors: {color_str}")

def main():
    difficulty_levels = {
        "easy": {"colors": ['R', 'G', 'B', 'Y'], "code_length": 4, "max_attempts": 12},
        "medium": {"colors": ['R', 'G', 'B', 'Y', 'O', 'P'], "code_length": 5, "max_attempts": 10},
        "hard": {"colors": ['R', 'G', 'B', 'Y', 'O', 'P', 'C', 'M'], "code_length": 6, "max_attempts": 8}
    }
    
    print("Welcome to Mastermind!")
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    level_choice = input("Enter the number of your choice: ")
    if level_choice == "1":
        level = "easy"
    elif level_choice == "2":
        level = "medium"
    elif level_choice == "3":
        level = "hard"
    else:
        print("Invalid choice. Defaulting to medium difficulty.")
        level = "medium"
    
    chosen_level = difficulty_levels[level]
    colors = chosen_level["colors"]
    code_length = chosen_level["code_length"]
    max_attempts = chosen_level["max_attempts"]
    
    secret_code = generate_secret_code(colors, code_length)
    
    print(f"\nYou have chosen {level} difficulty.")
    display_colors(colors)
    print(f"Try to guess the {code_length}-color code in {max_attempts} attempts.")
    
    for attempt in range(max_attempts):
        print(f"\nAttempt {attempt + 1}/{max_attempts}")
        guess = input("Enter your guess: ").upper()
        
        if len(guess) != code_length or not all(color in colors for color in guess):
            print("Invalid input. Make sure your guess consists of the correct number of valid colors.")
            continue
        
        correct_color_and_position, correct_color_only = evaluate_guess(secret_code, guess)
        
        if correct_color_and_position == code_length:
            print("Congratulations! You've guessed the correct code!")
            break
        else:
            print(f"Correct color and position: {correct_color_and_position}")
            print(f"Correct color only: {correct_color_only}")
    
    print(f"\nThe secret code was: {''.join(secret_code)}")

if __name__ == "__main__":
    main()
