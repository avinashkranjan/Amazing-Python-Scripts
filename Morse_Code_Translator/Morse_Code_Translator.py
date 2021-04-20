morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'
                   }


def encrypt(message):

    encrypted_text = ""
    for letters in message:
        if letters != " ":
            encrypted_text = encrypted_text + \
                morse_code_dict.get(letters) + " "

        else:
            encrypted_text += " "

    print(encrypted_text)


def decrypt(message):
    message += " "
    key_ = list(morse_code_dict.keys())
    value_ = list(morse_code_dict.values())
    code = ""
    decrypted_text = ""

    for letters in message:
        if letters != " ":
            code = code + letters
            total_space = 0

        else:
            total_space += 1
            if total_space == 2:
                decrypted_text += " "
            else:
                decrypted_text = decrypted_text + key_[value_.index(code)]
                code = ""

    print(decrypted_text)


text = input("Enter the text: \n")
if text.startswith('.') or text.startswith("-"):
    print('---Decrypting The Code---\n')
    decrypt(text)
else:
    print('---Ecrypting The Text---\n')
    encrypt(text.upper())
