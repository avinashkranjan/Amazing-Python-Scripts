import random


def choose_word():
    words = ["apple", "banana", "car", "dog", "elephant",
             "flower", "guitar", "house", "ice cream", "jacket"]
    return random.choice(words)


def draw_object(word):
    print(f"Draw a {word} on the screen.")


def guess_object():
    guess = input("Enter your guess: ").lower()
    return guess


def main():
    print("Welcome to Drawing Guess AI!")
    word_to_draw = choose_word()
    draw_object(word_to_draw)

    while True:
        user_guess = guess_object()

        if user_guess == word_to_draw:
            print("Congratulations! You guessed it correctly.")
            break
        else:
            print("Oops! That's not the right guess. Try again!")


if __name__ == "__main__":
    main()
