import random

# Define a list of brain teasers as tuples (question, answer)
brain_teasers = [
    ("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "an echo"),
    ("What comes once in a minute, twice in a moment, but never in a thousand years?", "the letter 'm'"),
    ("The more you take, the more you leave behind. What am I?", "footsteps"),
    ("What has keys but can't open locks?", "a piano"),
    ("You see a boat filled with people. It has not sunk, but when you look again you don’t see a single person on the boat. Why?",
     "all the people were married"),
]


def play_game():
    score = 0
    # Shuffle the brain teasers for a random order
    random.shuffle(brain_teasers)

    print("Welcome to the Brain Teaser Game!")
    print("Try to answer the following brain teasers:\n")

    for question, answer in brain_teasers:
        print("Question:", question)
        player_answer = input("Your Answer: ").lower()

        if player_answer == answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer is '{answer}'.\n")

    print("Game Over! Your final score:", score)


if __name__ == "__main__":
    play_game()
