import random


def generate_puzzle(difficulty):
    if difficulty == "easy":
        return generate_easy_puzzle()
    elif difficulty == "medium":
        return generate_medium_puzzle()
    elif difficulty == "hard":
        return generate_hard_puzzle()
    else:
        raise ValueError(
            "Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")


def generate_easy_puzzle():
    puzzle_type = random.choice(["arithmetic", "string"])
    if puzzle_type == "arithmetic":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-"])
        puzzle = f"{num1} {operator} {num2}"
        solution = eval(puzzle)
        hint = "This is an arithmetic puzzle."
    else:  # puzzle_type == "string"
        word = random.choice(["hello", "python", "coding", "challenge"])
        shuffle_word = "".join(random.sample(word, len(word)))
        puzzle = shuffle_word
        solution = word
        hint = "Rearrange the letters to form a meaningful word."

    return puzzle, solution, hint


def generate_medium_puzzle():
    puzzle_type = random.choice(["arithmetic", "string", "logical"])
    if puzzle_type == "arithmetic":
        num1 = random.randint(10, 50)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
        puzzle = f"{num1} {operator} {num2}"
        solution = eval(puzzle)
        hint = "This is an arithmetic puzzle."
    elif puzzle_type == "string":
        word = random.choice(["apple", "banana", "orange", "grape"])
        num_chars_to_remove = random.randint(1, len(word) - 1)
        indices_to_remove = random.sample(
            range(len(word)), num_chars_to_remove)
        puzzle = "".join(
            c if i not in indices_to_remove else "_" for i, c in enumerate(word))
        solution = word
        hint = f"Remove {num_chars_to_remove} letter(s) to reveal the original word."
    else:  # puzzle_type == "logical"
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["and", "or"])
        puzzle = f"{num1} {operator} {num2}"
        solution = eval(puzzle.capitalize())
        hint = "This is a logical puzzle."

    return puzzle, solution, hint


def generate_hard_puzzle():
    puzzle_type = random.choice(["arithmetic", "string", "logical"])
    if puzzle_type == "arithmetic":
        num1 = random.randint(50, 100)
        num2 = random.randint(10, 20)
        operator = random.choice(["+", "-", "*", "/"])
        puzzle = f"{num1} {operator} {num2}"
        solution = eval(puzzle)
        hint = "This is an arithmetic puzzle."
    elif puzzle_type == "string":
        word = random.choice(["python", "programming", "challenge"])
        num_chars_to_replace = random.randint(1, len(word) - 1)
        indices_to_replace = random.sample(
            range(len(word)), num_chars_to_replace)
        replacement_chars = "".join(random.choices(
            "abcdefghijklmnopqrstuvwxyz", k=num_chars_to_replace))
        puzzle = "".join(c if i not in indices_to_replace else replacement_chars[idx]
                         for idx, c in enumerate(word))
        solution = word
        hint = f"Replace {num_chars_to_replace} letter(s) with {replacement_chars} to reveal the original word."
    else:  # puzzle_type == "logical"
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["and", "or", "not"])
        puzzle = f"{operator.capitalize()} {num1} == {num2}"
        solution = eval(f"{num1} {operator} {num2}")
        hint = "This is a logical puzzle."

    return puzzle, solution, hint


def main():
    print("Welcome to the Coding Puzzle Generator!")
    difficulty_level = input(
        "Choose difficulty level (easy, medium, hard): ").lower()

    try:
        puzzle, solution, hint = generate_puzzle(difficulty_level)
        print("\nSolve the puzzle:")
        print(f"Question: {puzzle}")

        attempts = 3
        while attempts > 0:
            user_answer = input("Your answer: ").strip()
            if user_answer.lower() == "hint":
                print(f"HINT: {hint}")
            else:
                try:
                    # Convert to float for numeric puzzles
                    user_answer = float(user_answer)
                    if user_answer == solution:
                        print("Congratulations! Your answer is correct.")
                        break
                    else:
                        attempts -= 1
                        if attempts > 0:
                            print(
                                f"Sorry, that's incorrect. You have {attempts} {'attempts' if attempts > 1 else 'attempt'} remaining.")
                        else:
                            print(f"Sorry, the correct answer is: {solution}")
                except ValueError:
                    print("Invalid input. Please enter a numeric answer.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
