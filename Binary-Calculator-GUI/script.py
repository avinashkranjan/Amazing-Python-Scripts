from tkinter import *

window = Tk()
window.title("Standard Binary Calculator")
window.resizable(0, 0)

# Function to clear the entry field


def f1():
    s = e1_val.get()
    e1.delete(first=0, last=len(s))

# Function to add "1" to the entry field


def f2():
    s = e1_val.get()
    e1.insert(END, "1")

# Function to add "0" to the entry field


def f3():
    s = e1_val.get()
    e1.insert(END, "0")

# Function to evaluate the expression and display the result


def f4():
    s = e1_val.get()
    result = evaluate_expression(s)
    e1.delete(first=0, last=len(s))
    e1.insert(END, result)

# Function to add "+" operator to the entry field


def f5():
    e1.insert(END, "+")

# Function to add "-" operator to the entry field


def f6():
    e1.insert(END, "-")

# Function to add "/" operator to the entry field


def f7():
    e1.insert(END, "/")

# Function to add "X" operator to the entry field


def f8():
    e1.insert(END, "X")

# Function to negate the sign of the number in the entry field


def negate():
    s = e1_val.get()
    if s.startswith("-"):
        e1_val.set(s[1:])
    else:
        e1_val.set("-" + s)

# Function to delete the last character in the entry field


def backspace():
    s = e1_val.get()
    e1_val.set(s[:-1])

# Function to convert binary to decimal


def binary_to_decimal(n):
    num = n
    dec_value = 0
    base = 1
    temp = num
    while temp:
        last_digit = temp % 10
        temp = temp // 10
        dec_value += last_digit * base
        base = base * 2
    return dec_value

# Function to convert decimal to binary


def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Function to evaluate the expression


def evaluate_expression(expression):
    x = 0
    s = expression
    flag = 1
    for i in range(0, len(s)):
        if s[i] == '/' or s[i] == 'X' or s[i] == '+' or s[i] == '-':
            flag = 0
            a = s[0:i]
            b = s[i + 1:len(s)]
            if s[i] == '-':
                x = sub(int(a), int(b))
            elif s[i] == '/':
                x = int(int(a) / int(b))
            elif s[i] == 'X':
                x = int(int(a) * int(b))
            elif s[i] == '+':
                x = int(add(int(a), int(b)))
    if flag == 0:
        return str(x)
    return ""

# Function to perform binary addition


def add(x, y):
    a = binary_to_decimal(x)
    b = binary_to_decimal(y)
    c = a + b
    d = decimal_to_binary(c)
    return d

# Function to perform binary subtraction


def sub(x, y):
    a = binary_to_decimal(x)
    b = binary_to_decimal(y)
    c = a - b
    d = decimal_to_binary(c)
    return d


# Creating a StringVar to store the value of the entry field
e1_val = StringVar()

# Creating the entry field
e1 = Entry(window, textvariable=e1_val, width=50)
e1.grid(row=0, column=0, columnspan=4)

# Creating number buttons
b1 = Button(window, text="1", width=8, height=2, command=f2)
b1.grid(row=1, column=0)

b0 = Button(window, text="0", width=8, height=2, command=f3)
b0.grid(row=1, column=1)

# Creating clear button
clear = Button(window, text="C", width=8, height=2, command=f1)
clear.grid(row=1, column=2)

# Creating equals button
beq = Button(window, text="=", width=8, height=2, command=f4)
beq.grid(row=1, column=3)

# Creating operator buttons
badd = Button(window, text="+", width=8, height=2, command=f5)
badd.grid(row=2, column=0)

bsub = Button(window, text="-", width=8, height=2, command=f6)
bsub.grid(row=2, column=1)

bmul = Button(window, text="X", width=8, height=2, command=f8)
bmul.grid(row=2, column=2)

bdiv = Button(window, text="/", width=8, height=2, command=f7)
bdiv.grid(row=2, column=3)

# Creating additional buttons
bnegate = Button(window, text="+/-", width=8, height=2, command=negate)
bnegate.grid(row=3, column=0)

bbackspace = Button(window, text="⌫", width=8, height=2, command=backspace)
bbackspace.grid(row=3, column=1)

bbinary = Button(window, text="Bin to Dec", width=12,
                 height=2, command=on_binary)
bbinary.grid(row=3, column=2)

bdecimal = Button(window, text="Dec to Bin", width=12,
                  height=2, command=on_decimal)
bdecimal.grid(row=3, column=3)

# Function to convert binary to decimal and update entry field


def on_binary():
    s = e1_val.get()
    decimal = binary_to_decimal(s)
    e1_val.set(decimal_to_binary(decimal))

# Function to convert decimal to binary and update entry field


def on_decimal():
    s = e1_val.get()
    binary = decimal_to_binary(int(s))
    e1_val.set(binary)


window.mainloop()
