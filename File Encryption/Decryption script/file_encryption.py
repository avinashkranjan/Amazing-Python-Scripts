from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key


def encrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)


# Generate a new key (run this only once)
# generate_key()

# Load the key
key = load_key()

# Encrypt a file
file_to_encrypt = "example.txt"
encrypt_file(file_to_encrypt, key)
print("File encrypted successfully!")

# Decrypt the file
file_to_decrypt = "example.txt"
decrypt_file(file_to_decrypt, key)
print("File decrypted successfully!")
