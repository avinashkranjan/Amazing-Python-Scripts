# Encryption Script

This script allows you to encrypt text using various encryption methods.

## Installation

1. Make sure you have Python installed on your system.
2. Clone this repository or download the script file.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the following command: python script.py

Follow the prompts to enter the text and choose an encryption method.
Encryption Methods

Caesar Cipher
The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down the alphabet.
To choose the Caesar cipher, enter 1 when prompted.

Affine Cipher
The Affine cipher is a substitution cipher that combines the Caesar cipher with multiplication and addition.
To choose the Affine cipher, enter 2 when prompted.

Substitution Cipher
The Substitution cipher is a method of encryption where each letter in the plaintext is replaced by another letter according to a fixed key.
To choose the Substitution cipher, enter 3 when prompted. Note that the key must have the same length as the number of characters in the alphabet (26).

Transposition Cipher
The Transposition cipher is a method of encryption that rearranges the letters of the plaintext to form the ciphertext.
To choose the Transposition cipher, enter 4 when prompted. You will also be asked to enter a transposition key, which should be less than the length of the text.
Note: If you enter an invalid choice or provide incorrect input, appropriate error messages will be displayed.

Example
Here is an example of running the script:
Enter the text to encrypt: Hello, World!
Choose an encryption method:
1. Caesar cipher
2. Affine cipher
3. Substitution cipher
4. Transposition cipher
Enter your choice (1-4): 3
Enter the substitution key: QWERTYUIOPASDFGHJKLZXCVBNM
Substitution cipher (encryption): ITSSG, KTSSG!