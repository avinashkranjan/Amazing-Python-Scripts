# Checking entered number is a isbn number or not
def valid_ISBN(isbn):
    # Remove hyphens and spaces from the ISBN
    isbn = isbn.replace('-', '').replace(' ', '')

    # Check if the length of the ISBN is valid
    if len(isbn) == 10:
        return valid_ISBN10(isbn)
    elif len(isbn) == 13:
        return valid_ISBN13(isbn)
    else:
        return False

# Checking the entered number is a valid 10-digit isbn number


def valid_ISBN10(isbn):
    # Check if the ISBN is valid according to the ISBN-10 algorithm
    if not isbn[:-1].isdigit() or not isbn[-1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']:
        return False

    # Calculate the check digit
    checkDigit = 0
    weight = 10
    for digit in isbn[:-1]:
        checkDigit += int(digit) * weight
        weight -= 1

    checkDigit %= 11
    if isbn[-1] == 'X':
        checkDigit = 'X'

    # Validate the check digit
    return str(checkDigit) == isbn[-1]

# Checking the entered number is a valid 13-digit isbn number


def valid_ISBN13(isbn):
    # Check if the ISBN is valid according to the ISBN-13 algorithm
    if not isbn.isdigit():
        return False

    # Calculate the check digit
    checkDigit = 0
    weight = [1, 3] * 6
    for digit, w in zip(isbn[:-1], weight):
        checkDigit += int(digit) * w

    checkDigit %= 10
    checkDigit = (10 - checkDigit) % 10

    # Validate the check digit
    return str(checkDigit) == isbn[-1]


# Ask the user to enter an ISBN number
isbnNumber = input("\nEnter an ISBN number: ")

# Validate the ISBN number
if valid_ISBN(isbnNumber):
    print("\nValid ISBN number.\n")
else:
    print("\nInvalid ISBN number.\n")
