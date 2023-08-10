import random


def generate_code(length):
    return [random.randint(1, 6) for _ in range(length)]


def evaluate_guess(secret, guess):
    correct_positions = sum(1 for i in range(
        len(secret)) if secret[i] == guess[i])
    correct_numbers = len(set(secret) & set(guess)) - correct_positions
    return correct_positions, correct_numbers


def ai_brute_force(secret, code_length):
    possible_codes = [[i, j, k, l] for i in range(1, 7) for j in range(1, 7)
                      for k in range(1, 7) for l in range(1, 7)]
    attempts = 0
    while True:
        guess = possible_codes.pop(0)
        attempts += 1
        print(f"AI guess #{attempts}: {guess}")
        correct_positions, correct_numbers = evaluate_guess(secret, guess)

        if correct_positions == code_length:
            print(f"AI cracked the code in {attempts} attempts!")
            break

        possible_codes = [code for code in possible_codes if evaluate_guess(
            code, guess) == (correct_positions, correct_numbers)]


def main():
    code_length = 4
    max_attempts = 10
    secret_code = generate_code(code_length)

    print("Welcome to the Codebreaker Game!")
    print("Try to guess the AI's secret code.")
    print(
        f"The secret code consists of {code_length} numbers between 1 and 6.")

    player_code = []
    for attempt in range(1, max_attempts + 1):
        while True:
            try:
                player_code = [int(num) for num in input(
                    f"Attempt #{attempt}: Enter your code (space-separated): ").split()]
                if len(player_code) != code_length or any(num < 1 or num > 6 for num in player_code):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Enter a valid code.")

        correct_positions, correct_numbers = evaluate_guess(
            secret_code, player_code)
        print(
            f"Result: {correct_positions} in correct position, {correct_numbers} correct numbers but in wrong position.")

        if correct_positions == code_length:
            print(
                f"Congratulations! You cracked the code in {attempt} attempts!")
            break
    else:
        print(
            f"Sorry, you couldn't crack the code. The AI's secret code was: {secret_code}")


if __name__ == "__main__":
    main()
