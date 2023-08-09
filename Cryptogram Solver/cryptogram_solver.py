import string
import matplotlib.pyplot as plt
import pickle
import os


def load_word_dictionary(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file.readlines())


def get_letter_frequencies(text):
    frequencies = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            frequencies[char_lower] = frequencies.get(char_lower, 0) + 1
    return frequencies


def decrypt_cryptogram(cryptogram, frequency_map, word_dict):
    alphabet = string.ascii_lowercase
    sorted_freq = sorted(frequency_map.items(),
                         key=lambda x: x[1], reverse=True)
    freq_letters = ''.join(letter for letter, _ in sorted_freq)

    def decrypt_letter(letter):
        if letter.isalpha():
            index = freq_letters.find(letter.lower())
            decrypted_letter = alphabet[index] if letter.islower(
            ) else alphabet[index].upper()
            return decrypted_letter
        return letter

    decrypted_text = ''.join(decrypt_letter(char) for char in cryptogram)
    words = decrypted_text.split()
    decrypted_words = [word if word.lower(
    ) not in word_dict else word_dict[word.lower()] for word in words]
    return ' '.join(decrypted_words)


def guess_word_length(cryptogram):
    spaces = cryptogram.count(' ')
    return len(cryptogram) // (spaces + 1)


def manual_decryption(decrypted_text, cryptogram):
    print("\nManual Decryption:")
    while True:
        print("Current decrypted text:", decrypted_text)
        guess = input("Enter a letter to replace or press 'Enter' to finish: ")
        if not guess:
            break
        replacement = input(f"Enter the replacement for '{guess}': ")
        decrypted_text = decrypted_text.replace(guess, replacement)
    return decrypted_text


def visualize_frequency(frequency_map):
    sorted_freq = sorted(frequency_map.items(),
                         key=lambda x: x[1], reverse=True)
    letters, frequencies = zip(*sorted_freq)
    plt.bar(letters, frequencies)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency in the Cryptogram')
    plt.show()


def save_progress(decrypted_text):
    with open('progress.pickle', 'wb') as file:
        pickle.dump(decrypted_text, file)


def load_progress():
    if os.path.exists('progress.pickle'):
        with open('progress.pickle', 'rb') as file:
            return pickle.load(file)
    else:
        return None


if __name__ == '__main__':
    cryptogram = input("Enter the cryptogram: ")
    word_dict_path = input("Enter the path to the word dictionary file: ")

    word_dictionary = load_word_dictionary(word_dict_path)

    letter_frequencies = get_letter_frequencies(cryptogram)
    decrypted_message = load_progress() or decrypt_cryptogram(
        cryptogram, letter_frequencies, word_dictionary)

    print("\nOriginal cryptogram:", cryptogram)
    print("Decrypted message:", decrypted_message)

    word_length_guess = guess_word_length(cryptogram)
    print(f"Guessed word length: {word_length_guess}")

    visualize_frequency(letter_frequencies)

    decrypted_message = manual_decryption(decrypted_message, cryptogram)
    print("\nFinal decrypted message:", decrypted_message)

    save_progress(decrypted_message)
