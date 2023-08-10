import random


def choose_random_word():
    words = ["apple", "banana", "cherry", "grape",
             "orange", "watermelon", "kiwi", "mango"]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def guess_the_word():
    print("Welcome to Guess the Word game!")
    secret_word = choose_random_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            if set(guessed_letters) == set(secret_word):
                print("Congratulations! You guessed the word!")
                print(f"The word was: {secret_word}")
                break
            else:
                print("Correct guess!")
        else:
            attempts -= 1
            print("Incorrect guess!")

    else:
        print("Game over! You ran out of attempts.")
        print(f"The word was: {secret_word}")


if __name__ == "__main__":
    guess_the_word()
