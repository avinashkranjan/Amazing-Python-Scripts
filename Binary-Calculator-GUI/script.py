from tkinter import Tk, Entry, Button, StringVar

def clear_entry():
    e1.delete(0, 'end')

def add_digit(digit):
    current_expression = e1.get()
    e1.delete(0, 'end')
    e1.insert('end', current_expression + digit)

def evaluate_expression():
    expression = e1.get()
    try:
        result = str(eval(expression))
    except (SyntaxError, NameError, ZeroDivisionError):
        result = "Error"
    e1.delete(0, 'end')
    e1.insert('end', result)

def convert_binary_to_decimal():
    binary = e1.get()
    try:
        decimal = str(int(binary, 2))
    except ValueError:
        decimal = "Error"
    e1.delete(0, 'end')
    e1.insert('end', decimal)

def convert_decimal_to_binary():
    decimal = e1.get()
    try:
        binary = bin(int(decimal))[2:]
    except ValueError:
        binary = "Error"
    e1.delete(0, 'end')
    e1.insert('end', binary)

window = Tk()
window.title("Standard Binary Calculator")
window.resizable(0, 0)

e1 = Entry(window, width=50)
e1.grid(row=0, column=0, columnspan=4)

button_values = [
    ("1", lambda: add_digit("1")),
    ("0", lambda: add_digit("0")),
    ("C", clear_entry),
    ("=", evaluate_expression),
    ("+", lambda: add_digit("+")),
    ("-", lambda: add_digit("-")),
    ("X", lambda: add_digit("*")),
    ("/", lambda: add_digit("/")),
    ("+/-", lambda: e1.insert('0', '-')),
    ("⌫", lambda: e1.delete(len(e1.get()) - 1)),
    ("Bin to Dec", convert_binary_to_decimal),
    ("Dec to Bin", convert_decimal_to_binary),
]

row = 1
col = 0

for text, command in button_values:
    button = Button(window, text=text, width=8, height=2, command=command)
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
