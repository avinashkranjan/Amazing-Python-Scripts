import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)                                                                                    # Randomly choose a word for the given list 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()                                                                                            # Return the word in uppercase


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)                                                                                       # Alphabets in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()                                                                                           # Letters guessed by the user 

    lives = 7

    # Get user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left, and you have used these letters: ', ' '.join(used_letters))          # Join the used letters from the list

        # Display what current word is for each guess
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()                                                            # Add the letter entered to the list 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1                                                                                 # Decrease number of lives by 1 
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used this letter. Guess another letter.')

        else:
            print('\nInvalid letter. Enter a valid letter.')

    # When number of lives is 0 or if the word is guessed 
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word correctly', word, '!!')


if __name__ == '__main__':
    hangman()