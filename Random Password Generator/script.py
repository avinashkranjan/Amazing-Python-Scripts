import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

# main window
root = tk.Tk()
# title of the window
root.title("Random Password Generator")
# disabling resizing of window
root.resizable(0, 0)

# variables for Password
upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
punc = string.punctuation

pass_str = StringVar()
pass_wrd = StringVar()

# function to create a random password


def create_pass():
    password.delete(0, END)
    Len = len.get()
    strn = opt.get()
    pass_wrd = ""
    # password of low strength
    if (strn == 1):
        for i in range(0, Len):
            pass_wrd = pass_wrd + random.choice(lower + num)
        return pass_wrd
    # password of medium strength
    elif (strn == 2):
        for i in range(0, Len):
            pass_wrd = pass_wrd + random.choice(lower + upper + num)
        return pass_wrd
    # password of high strength
    elif (strn == 3):
        for i in range(0, Len):
            pass_wrd = pass_wrd + random.choice(lower + upper + num + punc)
        return pass_wrd
    else:
        messagebox.showwarning("Warning", "Select all parameters")

# function to generate the password


def gen():
    pass_str = create_pass()
    password.insert(0, pass_str)

# function to copy password to clipboard


def cpy():
    random_pass = password.get()
    pyperclip.copy(random_pass)
    messagebox.showinfo("Message", "Copied to clipboard !")

# Adding frames


# ---frame for top name---
top = Frame(root, width=700, height=50, bd=8, relief="raise")
top.pack(side=TOP)

# ---frame for length of password---
Length = Frame(root, width=700, height=50, bd=8, relief="raise")
Length.pack(side=TOP)

# ---frame for strength of password---
strength = Frame(root, width=300, height=450, bd=8,
                 relief="raise", padx=100, pady=20)
strength.pack(side=LEFT)

# ---frame for output---
output = Frame(root, width=450, height=450, bd=8, relief="raise")
output.pack(side=RIGHT)


# Adding widgets
greeting = Label(top, text="Random Password Generator", width=40,
                 height=2, font=("Lucida Console", 20, "italic"))
greeting.grid(padx=18)

# ---length of password---
lengthlabel = Label(Length, text="Length of Password",
                    width=20, height=5, font=("Arial", 10, "bold"))
lengthlabel.grid(row=5, column=1, padx=3, pady=10)

len = IntVar()
scale = Scale(Length, orient=HORIZONTAL, from_=6, to=24,
              tickinterval=1, length=500, variable=len)
scale.grid(row=5, column=2)


# ---strength of password---
strengthlabel = Label(strength, text="Strength", justify="center",
                      width=6, height=2, font=("Arial", 12, "bold"))
strengthlabel.grid(row=10, column=2, pady=10)

opt = IntVar()
c1 = Radiobutton(strength, text="Low", width=6, height=2,
                 variable=opt, value=1, font=("Arial", 12))
c1.grid(row=12, column=2, ipadx=2, ipady=2, sticky='E', pady=5, padx=5)

c2 = Radiobutton(strength, text="Medium", width=6, height=2,
                 variable=opt, value=2, font=("Arial", 12))
c2.grid(row=14, column=2, ipadx=2, ipady=2,  sticky='E', pady=5, padx=5)

c3 = Radiobutton(strength, text="High", width=6, height=2,
                 variable=opt, value=3, font=("Arial", 12))
c3.grid(row=16, column=2, ipadx=2, ipady=2,  sticky='E', pady=5, padx=5)


# ---output---
genbtn = Button(output, text="Generate Password", justify="center",
                width=20, height=3, command=gen, font=("Arial", 12, "bold"))
genbtn.grid(row=1, column=4, padx=30, pady=17)

password = Entry(output, justify="center", width=50, textvariable=pass_str)
password.grid(row=2, column=4, padx=30, pady=20, ipady=8)

copybtn = Button(output, text="Copy", justify="center", width=20,
                 height=3, font=("Arial", 12, "bold"), command=cpy)
copybtn.grid(row=3, column=4, padx=30, pady=17)

root.mainloop()
