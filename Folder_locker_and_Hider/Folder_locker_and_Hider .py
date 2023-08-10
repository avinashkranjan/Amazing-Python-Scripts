import os

def xor_encrypt_decrypt(data, key):
    return bytes([byte ^ key for byte in data])

def lock_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

        encrypted_data = xor_encrypt_decrypt(data, key)

        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    except Exception as e:
        print(f'Error locking the file: {e}')

def hide_file(file_path):
    try:
        os.rename(file_path, '.' + file_path)
    except Exception as e:
        print(f'Error hiding the file: {e}')

def lock_and_hide_folder(folder_path, key):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                lock_file(file_path, key)
                hide_file(file_path + '.locked')

        os.rename(folder_path, '.' + folder_path)
        print(f'Folder locked and hidden as .{folder_path}')

    except Exception as e:
        print(f'Error locking and hiding the folder: {e}')

def main():
    folder_path = input("Enter the folder path: ")
    key = int(input("Enter the encryption key (an integer): "))

    lock_and_hide_folder(folder_path, key)

if __name__ == "__main__":
    main()