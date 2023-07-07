import string
import sys

# Caesar cipher encryption


def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            alphabet = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
            encrypted_char = alphabet[(
                alphabet.index(char) + shift) % len(alphabet)]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Affine cipher encryption


def affine_cipher_encrypt(text, a, b):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            alphabet = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
            encrypted_char = alphabet[(
                a * alphabet.index(char) + b) % len(alphabet)]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Substitution cipher encryption


def substitution_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            alphabet = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
            substitution_alphabet = str.maketrans(alphabet, key.upper(
            )) if char.isupper() else str.maketrans(alphabet, key.lower())
            encrypted_char = char.translate(substitution_alphabet)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Transposition cipher encryption


def transposition_cipher_encrypt(text, key):
    ciphertext = [''] * int(key)
    for column in range(int(key)):
        currentIndex = column
        while currentIndex < len(text):
            ciphertext[column] += text[currentIndex]
            currentIndex += int(key)

    return ''.join(ciphertext)


def main():
    text = input("Enter the text to encrypt: ")

    # Ask user for the encryption method
    print("Choose an encryption method:")
    print("1. Caesar cipher")
    print("2. Affine cipher")
    print("3. Substitution cipher")
    print("4. Transposition cipher")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:  # to handle wrong values
        print("Invlaid selection")
        sys.exit(0)

    if choice == 1:

        try:
            shift = int(input("Enter the shift value for Caesar cipher: "))
            encrypted_text = caesar_cipher_encrypt(text, shift)
            print("Caesar cipher (encryption):", encrypted_text)
        except ValueError:
            print("Invalid Input")

    elif choice == 2:

        try:
            a = int(input("Enter the value for 'a' in Affine cipher: "))
            b = int(input("Enter the value for 'b' in Affine cipher: "))
            encrypted_text = affine_cipher_encrypt(text, a, b)
            print("Affine cipher (encryption):", encrypted_text)

        except ValueError:
            print("Invalid Input")

    elif choice == 3:

        key = input("Enter the substitution key: ")
        if len(key) == 26:
            encrypted_text = substitution_cipher_encrypt(text, key)
            print("Substitution cipher (encryption):", encrypted_text)
        else:
            print(
                "Key must have the same length as the number of characters in the alphabet (26).")

    elif choice == 4:

        try:
            transpose_key = input(
                "Enter the transposition key (make sure its less than length of stirng): ")
            if int(transpose_key) > len(text):
                print("Key must be less than length of string")
            else:
                encrypted_text = transposition_cipher_encrypt(
                    text, transpose_key)
                print("Transposition cipher (encryption):", encrypted_text)

        except ValueError:
            print("Invalid Input")

    else:
        print("Invalid choice. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()
