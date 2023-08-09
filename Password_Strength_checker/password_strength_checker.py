import re


def is_strong_password(password):
    # Check length (at least 8 characters)
    if len(password) < 8:
        return False

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return False

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return False

    # Check for digits
    if not any(char.isdigit() for char in password):
        return False

    # Check for special characters
    special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if not special_chars.search(password):
        return False

    return True


def main():
    password = input("Enter your password: ")

    if is_strong_password(password):
        print("Strong password! Good job.")
    else:
        print("Weak password. Please make it stronger.")


if __name__ == "__main__":
    main()
