import pyperclip
# Required constants
normal_word = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
               "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
              "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]


def option_menu():
    option = int(input("Choose 1.For Encoding and 2.For Decoding:"))
    if (option == 1):
        word = input("Enter the sentence that you want to encode:").upper()
        coded_form = ""
        for letter in word:
            if letter == " ":
                coded_form += "/ "
            else:
                ind = normal_word.index(letter)
                coded_form += morse_code[ind]
                coded_form += " "
        print(f"{word} in morse code is {coded_form}")
        pyperclip.copy(coded_form)
        print("Copied it to clipboard 😉")
        print("\n")
        option_menu()

    if (option == 2):
        decoded_form = ""
        encode_word = input("Enter the sentence that you want to decode:")
        encoded_word = encode_word.split(" ")
        for item in encoded_word:
            if item.isalnum() or item.isalpha():
                print("Please enter valid morse code 😀")
                option_menu()
            if item == "/":
                decoded_form += " "
                continue
            if item == "":
                continue
            else:
                ind = morse_code.index(item)
                decoded_form += normal_word[ind]
        print(f"{encode_word} in decoded form is {decoded_form}")
        pyperclip.copy(decoded_form)
        print("Copied it to clipboard 😉")
        print("\n")
        option_menu()


option_menu()
