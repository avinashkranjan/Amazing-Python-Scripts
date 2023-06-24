# Cipher Buster: Brute Force Decryption for Caesar and Transposition Ciphers

Cipher Buster is a Python script that performs a brute force attack on Caesar Cipher and Transposition Cipher encryption. It allows you to analyze the security of these encryption methods by attempting to crack them through an exhaustive search of all possible keys.

## Features

- Decrypt ciphertext encrypted using the Caesar Cipher.
- Decrypt ciphertext encrypted using the Transposition Cipher.
- Perform automatic brute force decryption by trying all possible shift values for Caesar Cipher or key values for Transposition Cipher.
- User-friendly command-line interface for input and interaction.

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Clone this repository or download the `cipher_buster.py` file.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script using the following command: python cipher_buster.py
5. Follow the prompts to select the encryption method (Caesar or Transposition) and provide the ciphertext.
6. If you know the shift value or key, enter it when prompted. Otherwise, leave it blank to try all possible combinations.
7. The script will display the decrypted plaintext for each potential key or shift value.

## Examples

### Decrypting Caesar Cipher

Which encryption method would you like to decrypt?
Choose number:
1) Caesar
2) Transposition
> 1

Enter the ciphertext to decrypt: VQREQFGT

Enter the shift value used in the Caesar cipher:
[If you don't know the shift/key, just press enter; the script will try all possible combinations then]
> 2

TOPSECRET

## Decrypting Transposition Cipher

Which encryption method would you like to decrypt?
Choose number:
1) Caesar
2) Transposition
> 2

Enter the ciphertext to decrypt: AEIMNORTUAYOBCEFHLPET

Enter the key used in the transposition cipher:
[If you don't know the shift/key, just press enter; the script will try all possible combinations then]
> 

IMAHIDDENMESSAGEFORYOU