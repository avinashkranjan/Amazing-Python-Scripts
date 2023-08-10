import random

cryptic_language = {
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T',
    'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P',
    'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G',
    'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z',
    'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N',
    'Z': 'M'
}

messages = [
    "HELLO WORLD",
    "CRYPTIC PUZZLE",
    "PYTHON IS FUN",
    "SOLVE THE CODE",
    "GREAT PUZZLE GAME",
    "LEARNING PYTHON",
    "CHALLENGE ACCEPTED",
    "UNLOCK THE MYSTERY",
    "ENJOY THE PUZZLES",
    "BECOME A MASTER",
    "DISCOVER THE SECRET",
    "EMBRACE THE UNKNOWN",
    "CRACK THE CIPHER",
    "DECODE AND WIN",
    "MASTER THE CODE",
    "UNVEIL THE TRUTH",
    "EXPLORE THE PUZZLE",
    "PUZZLE SOLVER",
    "MIND-BENDING FUN",
    "THINK OUTSIDE THE BOX"
]


def generate_message():
    return random.choice(messages)


def play_game():
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}, to the Cryptic Language Puzzle Game!")
    print("You need to decipher the message to progress.\n")

    score = 0

    while True:
        encrypted_message = generate_message()
        print("Decipher the following message:")
        print(encrypted_message)

        guess = input("Enter your guess: ").upper()

        if guess == encrypted_message:
            score += 1
            print("Congratulations! You deciphered the message.")
            print(f"Current Score: {score}\n")
        else:
            print("Incorrect guess. Try again.\n")

        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again.lower() != "yes":
            print(f"Thank you for playing, {player_name}!")
            print(f"Final Score: {score}")
            break


if __name__ == "__main__":
    play_game()
