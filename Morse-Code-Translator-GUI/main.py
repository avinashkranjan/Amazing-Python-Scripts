# Import Tkinter module
from tkinter import *
from tkinter import messagebox

# Create a window
root = Tk()

# Create global variables
variable1 = StringVar(root)
variable2 = StringVar(root)

# Initialise the variables
variable1.set("Language select")
variable2.set("Language select")

"""
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
"""

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


# Function to clear both the text areas
def clearAll():
    # whole content of text area is deleted
    language1_field.delete(1.0, END)
    language2_field.delete(1.0, END)


# Function to perform conversion from one
# language to another
def convert():
    # get a whole input content from text box
    # ignoring \n from the text box content
    message = language1_field.get("1.0", "end")[:-1]

    # get the content from variable1 and 2, check their values
    if variable1.get() == variable2.get():
        # show the error message
        messagebox.showerror("Can't Be same Language")
        return

    elif variable1.get() == "English" and variable2.get() == "Morse Code":
        # function call
        rslt = encrypt(message)

    elif variable1.get() == "Morse Code" and variable2.get() == "English":
        # function call
        rslt = decrypt(message)

    else:
        # show the error message
        messagebox.showerror("please choose valid language code..")
        return

    # insert content into text area
    # from rslt variable
    language2_field.delete(1.0, END)
    language2_field.insert("end -1 chars", rslt)


# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ""
    for letter in message:
        if letter.isalpha():
            cipher += MORSE_CODE_DICT[letter.upper()] + " "

        elif letter != " ":
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += " "

    return cipher


# Function to decrypt the string
# from morse to english
def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += " "

    decipher = ""
    citext = ""
    for letter in message:
        # checks for space
        if letter != " ":
            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher += " "
            else:
                # accessing the keys using their values
                # (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[
                    list(MORSE_CODE_DICT.values()).index(citext)
                ]
                citext = ""

    return decipher


# Driver code
if __name__ == "__main__":
    # Set the background colour of GUI window
    root.configure()

    # Set the configuration of GUI window (WidthxHeight)
    root.geometry("450x400")

    # set the name of tkinter GUI window
    root.title("Morse Code Translator")

    # Create Welcome to Morse Code Translator label
    headlabel = Label(
        root, text="Welcome to Morse Code Translator", fg="black", justify="center"
    )

    # # Create a "One Language " label
    label1 = Label(root, text="First Language : Input", fg="black")

    # # Create a "From Language " label
    label2 = Label(root, text="Second Language : To Convert", fg="black")

    # # Create a "To Language " label
    # label3 = Label(root, text="To Language ", fg="black", bg="dark green")

    # # Create a "Converted Language " label
    # label4 = Label(root, text="Converted Language ", fg="black", bg="dark green")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    headlabel.grid(row=0, column=1)
    label1.grid(row=2, column=0)
    label2.grid(row=3, column=0)
    # label3.grid(row=3, column=0)
    # label4.grid(row=5, column=0)

    # Create a text area box
    # for filling or typing the information.
    language1_field = Text(root, height=5, width=25, font="lucida 13")
    language2_field = Text(root, height=5, width=25, font="lucida 13")

    # padx keyword argument used to set padding along x-axis .
    language1_field.grid(row=1, column=1, padx=10)
    language2_field.grid(row=5, column=1, padx=10)

    # list of language codes
    languageCode_list = ["English", "Morse Code"]

    # create a drop down menu using OptionMenu function
    # which takes window name, variable and choices as
    # an argument. use * before the name of the list,
    # to unpack the values
    FromLanguage_option = OptionMenu(root, variable1, *languageCode_list)
    ToLanguage_option = OptionMenu(root, variable2, *languageCode_list)

    FromLanguage_option.grid(row=2, column=1, ipadx=10)
    ToLanguage_option.grid(row=3, column=1, ipadx=10)

    # Create a Convert Button and attached
    # with convert function
    button1 = Button(
        root, text="Convert", bg="gray", fg="black", command=convert, cursor="hand2"
    )

    button1.grid(row=4, column=1)

    # Create a Clear Button and attached
    # with clearAll function
    button2 = Button(
        root,
        text="Clear",
        bg="red",
        fg="black",
        command=clearAll,
        padx=10,
        cursor="hand2",
    )

    button2.grid(row=6, column=1)

    # Start the GUI
    root.mainloop()
