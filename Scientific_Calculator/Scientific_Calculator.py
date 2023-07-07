################################################### Scientific Calculator ###################################################
################################################## Made By Avdhesh Varshney #################################################
############################################ (https://github.com/Avdhesh-Varshney) ##########################################

# Importing Modules
from tkinter import *
import tkinter.messagebox as tmsg
import math as m

# Initialising Tkinter module
root = Tk()

# Fixing the size of the calculator screen
root.minsize(520, 340)
root.maxsize(520, 340)

# Title of the calculator
root.title("Scientific Calculator")
root.wm_iconbitmap("calculator.ico")

sc = StringVar()
sc = Entry(root, width=31, textvariable=sc,
           relief=SUNKEN, font="cosmicsansms 20")
sc.grid(row=0, column=0, columnspan=10, padx=11, pady=12)

# Helping messages


def helper():
    help = '''1. For the following functions please enter the number first and then press the required function:
sin, cos, tan, log, ln, √, !, rad, degree, 1/x, π, e 

2. For multiplication with float numbers, say 5*0.4 multiply like 5*4/10'''
    # Adding message into the menu bar of the calculator
    tmsg.showinfo("Help", help)


# About section of the header
def abt():
    abt_text = "This calculator was developed using Tkinter, by Avdhesh Varshney.\n\n"
    abt_text += "A student of Dr. B R Ambedkar National Institute of Technology, Jalandhar.\n\n"
    abt_text += "Click the link below to access the GitHub account:\n\n"
    abt_text += "https://github.com/Avdhesh-Varshney"

    # Appending the link to the message in the about section of the menu bar
    tmsg.showinfo("About", abt_text)


# Suggestion to the user of the scientific calculator
def const():
    msg = '''If you press constants like:  π and e, 2 times, the result will be square of that constant. 
That means number of times you press the constant, the result will be constant to the power that number. '''
    tmsg.showinfo("Help", msg)


# Initialising main screen/root of the calculator
mainmenu = Menu(root)

# Adding menu bar in the calculator
submenu = Menu(mainmenu, tearoff=0)
submenu.add_command(label="General", command=helper)
submenu.add_command(label="Constants", command=const)
mainmenu.add_cascade(label="Help", menu=submenu)

# Append the author details
mainmenu.add_command(label="About", command=abt)

# Append the exit button
mainmenu.add_command(label="Exit", command=quit)

# Finally set the configuration in the screen of the calculator made by Tkinter library
root.config(menu=mainmenu)


# Creating a function which helps to calculate the different function in scientific calculator
def scientificCalc(event):
    # After event is triggered, performing different operation according to the command of the user
    key = event.widget
    text = key['text']
    val = sc.get()
    sc.delete(0, END)

    # Checking the function i.e., which function is triggered by the user

    # Trigonometric functions
    if text == "sin":
        sc.insert(0, m.sin(float(val)))

    elif text == "cos":
        sc.insert(0, m.cos(float(val)))

    elif text == "tan":
        sc.insert(0, m.tan(float(val)))

    # Logarithmic functions
    elif text == "log":
        if (float(val) <= 0.00):
            sc.insert(0, "Not Possible")
        else:
            sc.insert(0, m.log10(float(val)))

    elif text == "ln":
        if (float(val) <= 0.00):
            sc.insert(0, "Not Possible")
        else:
            sc.insert(0, m.log(float(val)))

    # Exponential functions
    elif text == "√":
        sc.insert(0, m.sqrt(float(val)))

    elif text == "!":
        sc.insert(0, m.factorial(int(val)))

    # Angular functions
    elif text == "rad":
        sc.insert(0, m.radians(float(val)))

    elif text == "deg":
        sc.insert(0, m.degrees(float(val)))

    # Constants functions
    elif text == "π":
        if val == "":
            ans = str(m.pi)
            sc.insert(0, ans)
        else:
            ans = str(float(val) * (m.pi))
            sc.insert(0, ans)

    elif text == "1/x":
        if (val == "0"):
            sc.insert(0, "ꝏ")
        else:
            sc.insert(0, 1/float(val))

    elif text == "e":
        if val == "":
            sc.insert(0, str(m.e))
        else:
            sc.insert(0, str(float(val) * (m.e)))


# Function to check click events
def click(event):
    key = event.widget
    text = key['text']
    oldValue = sc.get()
    sc.delete(0, END)
    newValue = oldValue + text
    sc.insert(0, newValue)


# Clear the calculator screen
def clr(event):
    sc.delete(0, END)


# Delete the entered text or number one by one
def backspace(event):
    entered = sc.get()
    length = len(entered) - 1
    sc.delete(length, END)


# Calculate function is triggered
def calculate(event):
    answer = sc.get()
    if "^" in answer:
        answer = answer.replace("^", "**")
    answer = eval(answer)
    sc.delete(0, END)
    sc.insert(0, answer)


# Initialising the user interface of the calculator
class Calculator:
    def __init__(self, txt, r, c, funcName, color="black"):
        self.var = Button(root, text=txt, padx=3, pady=5,
                          fg="white", bg=color, width=10, font="cosmicsansms 12")
        self.var.bind("<Button-1>", funcName)
        self.var.grid(row=r, column=c)


# Adding labels on the different buttons with name, color, function, and indexes

# Trignometric fuctions

btn0 = Calculator("sin", 1, 0, scientificCalc, "grey")

btn1 = Calculator("cos", 1, 1, scientificCalc, "grey")

btn2 = Calculator("tan", 1, 2, scientificCalc, "grey")


# Logarithmic functions

btn3 = Calculator("log", 1, 3, scientificCalc)

btn4 = Calculator("ln", 1, 4, scientificCalc)


# Brackets

btn5 = Calculator("(", 2, 0, click)

btn6 = Calculator(")", 2, 1, click)


# Exponential functions

btn7 = Calculator("^", 2, 2, click)

btn8 = Calculator("√", 2, 3, scientificCalc)

btn9 = Calculator("!", 2, 4, scientificCalc)


# Constant and Angular functions

btn10 = Calculator("π", 3, 0, scientificCalc, "blue")

btn11 = Calculator("1/x", 3, 1, scientificCalc)

btn12 = Calculator("deg", 3, 2, scientificCalc)

btn13 = Calculator("rad", 3, 3, scientificCalc)

btn14 = Calculator("e", 3, 4, scientificCalc, "blue")


# Basic Arithmetic operators

btn15 = Calculator("/", 4, 0, click, "#DBA800")

btn16 = Calculator("*", 4, 1, click, "#DBA800")

btn17 = Calculator("-", 4, 2, click, "#DBA800")

btn18 = Calculator("+", 4, 3, click, "#DBA800")

btn19 = Calculator("%", 4, 4, click, "#DBA800")


# Numbering Buttons

btn20 = Calculator("9", 5, 0, click)

btn21 = Calculator("8", 5, 1, click)

btn22 = Calculator("7", 5, 2, click)

btn23 = Calculator("6", 5, 3, click)

btn24 = Calculator("5", 5, 4, click)

btn25 = Calculator("4", 6, 0, click)

btn26 = Calculator("3", 6, 1, click)

btn27 = Calculator("2", 6, 2, click)

btn28 = Calculator("1", 6, 3, click)

btn29 = Calculator("0", 6, 4, click)


# Some special buttons

btn30 = Calculator("C", 7, 0, clr, "red")

btn31 = Calculator("⌦", 7, 1, backspace, "red")

btn32 = Calculator("00", 7, 2, click)

btn33 = Calculator(".", 7, 3, click)

btn34 = Calculator("=", 7, 4, calculate)

# Program Starts
root.mainloop()
