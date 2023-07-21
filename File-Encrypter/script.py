from cryptography.fernet import Fernet
import os
import sys
import argparse


def generate_key():
    return Fernet.generate_key()


def save_key(key, file_path):
    # save encryption key to a file
    with open(file_path, 'wb') as f:
        f.write(key)


def load_key(file_path):
    with open(file_path, 'rb') as f:
        return f.read()


def encrypt_file(key, file_path):
    f = Fernet(key)
    with open(file_path, 'rb') as f_input:
        data = f_input.read()
    encrypted_data = f.encrypt(data)
    with open(file_path.split(".")[0]+'.encrypted', 'wb') as f_output:
        f_output.write(encrypted_data)
    os.remove(file_path)


def decrypt_file(key, file_path):
    f = Fernet(key)
    with open(file_path, 'rb') as f_enc:
        data = f_enc.read()
    dec_data = f.decrypt(data)
    with open(file_path.split(".")[0]+".txt", 'wb') as f_dec:
        f_dec.write(dec_data)
    os.remove(file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="[*]Encrypt youre files and password protect them")
    parser.add_argument(
        'file_path', help="Add the name of the file to be encrypted")
    parser.add_argument('mode', choices=[
                        'encrypt', 'decrypt'], help="Choose either encrypt or decrypt")
    args = parser.parse_args()

    if args.mode == "encrypt":
        key = generate_key()
        save_key(key, "secret.key")
        encrypt_file(key, args.file_path)
        print("Encrypted")
    else:
        key = load_key("secret.key")

        decrypt_file(key, args.file_path)
        print("Decrypted")
