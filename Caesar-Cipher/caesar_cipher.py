import string as st

letter_list = st.ascii_lowercase
alphabet = [letter for letter in letter_list]*2


def caesar(text1, shift1, direction1):
    end_text = ''
    if direction == 'decode':
        shift1 *= -1

    for char in text1:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift1
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {direction1}d text is: {end_text}.')


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25

    caesar(text, shift, direction)
    choice = input("Type 'yes' to continue otherwise type 'no'.\n")
    if choice == 'no':
        should_continue = False
