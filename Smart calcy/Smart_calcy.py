# Authour : Yuvraj Kadale - Gssoc 21

from tkinter import *

""" 
Defining Calculating functions below

"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def lcm(a, b):
    L = a if a > b else b
    while L <= a+b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


def read_from_text(text):
    """ Function to extract key words from the sentence """
    read = []
    for t in text.split(' '):
        try:
            read.append(float(t))
        except ValueError:
            pass
    return read


def Calculate():
    """ Function to calculate the given question """

    text = text_in.get()  # getting input text
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                read = read_from_text(text)  # reading from given text
                r = operations[word.upper()](read[0], read[1])
                Answer_box.delete(0, END)  # clearing answer box
                Answer_box.insert(END, r)
            except:
                Answer_box.delete(0, END)
                # message if there is an input error
                Answer_box.insert(
                    END, "Somthing went worng, Could you pls retype :')")
            finally:
                break
        elif word.upper() not in operations.keys():
            Answer_box.delete(0, END)
            Answer_box.insert(
                END, "Somthing went worng, Could you pls retype :')")


# Creating Dictionary of possible key words to match with matematical operations
operations = {
    'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
    'SUB': sub, 'MINUS': sub, 'DIFFERENCE': sub, 'SUBTRACT': sub,
                'LCM': lcm, 'HCF': hcf, 'PRODUCT': mul, 'MULTIPLICATION': mul, 'MULTIPLY': mul,
                'DIVIDE': div, 'DIVISION': div, 'DIV': div, 'MOD': mod, 'REMINDER': mod, 'MODULUS': mod,
}

''' 
GUI designing begins here with the help of tkinter

'''

win = Tk()                                  # Creating Window
win.geometry('500x330')                     # Defining windows size
win.title("Smart Calcy")                    # title of the window
# Defining Background color of the calcy
win.configure(bg='Sky blue')

title_lable = Label(win, text="I am your Smart Calcy :D",
                    width=30, padx=3)  # Defining the titile lable
title_lable.place(x=160, y=10)
intro_lable = Label(win, text="You can call me 'Genius'",
                    padx=3)  # Defining the intro lable
intro_lable.place(x=200, y=40)
# Defining the asking lable
ask_lable = Label(
    win, text="How may I help you? You can type in below I will read it :)", padx=3)
ask_lable.place(x=110, y=130)

text_in = StringVar()
# Entry to take questions from users
Question_entry = Entry(win, width=30, textvariable=text_in)
Question_entry.place(x=180, y=160)

# Defining button to ask answer
Answer_button = Button(win, text="What do you say?", command=Calculate)
Answer_button.place(x=220, y=190)

Answer_lable = Label(win, text="Genius says ...", padx=3)
Answer_lable.place(x=150, y=240)

# Defining area to answer the given question
Answer_box = Listbox(win, width=40, height=3)
Answer_box.place(x=150, y=260)

win.mainloop()
