import random
import pyperclip
from tkinter import *
from tkinter.ttk import *


def getStrength():
    entry.delete(0, END)
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    # if strength selected is low
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    # if strength selected is medium
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    # if strength selected is strong
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")


# Function for generation of password
def generate():
    password1 = getStrength()
    entry.insert(10, password1)


# Function for copying password to clipboard
def copy():
    random_password = entry.get()
    pyperclip.copy(random_password)


# create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()


# Title of the GUI window
root.title("Password Generator")

# create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=0)
copy_button = Button(root, text="Copy", command=copy)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=0)
Random_password = Label(root, text="Generated password", padding=5)
Random_password.grid(row=1)
entry = Entry(root)
entry.grid(row=1, column=1)


# run the GUI continuously
root.mainloop()
