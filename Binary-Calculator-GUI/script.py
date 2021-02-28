from tkinter import *
window = Tk()
window.title("Standard Binary Calculator")
window.resizable(0, 0)


def f1():
    s = e1_val.get()
    e1.delete(first=0, last=len(s))


def f2():
    s = e1_val.get()
    e1.insert(END, "1")


def f3():
    s = e1_val.get()
    e1.insert(END, "0")


def f4():
    x = 0
    s = e1_val.get()
    for i in range(0, len(s)):
        if s[i] == '/' or s[i] == 'X' or s[i] == '+' or s[i] == '-':
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

    e1.delete(first=0, last=len(s))
    e1.insert(END, "")
    e1.insert(END, str(x))


def bin_to_dec(n):
    num = n
    dec_value = 0
    base = 1
    temp = num
    while (temp):
        last_digit = temp % 10
        temp = int(temp / 10)

        dec_value += last_digit * base
        base = base * 2
    return dec_value


def add(x, y):
    a = bin_to_dec(x)
    b = bin_to_dec(y)
    c = a + b
    d = bin(c).replace("0b", "")
    return d


def sub(x, y):
    a = bin_to_dec(x)
    b = bin_to_dec(y)
    c = a - b
    d = bin(c).replace("0b", "")
    return d


def f5():
    x = 0
    s = e1_val.get()
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
        e1.delete(first=0, last=len(s))
        e1.insert(END, str(x))
    e1.insert(END, "+")


def f6():
    x = 0
    s = e1_val.get()
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
        e1.delete(first=0, last=len(s))
        e1.insert(END, str(x))
    e1.insert(END, "-")


def f7():
    x = 0
    s = e1_val.get()
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
        e1.delete(first=0, last=len(s))
        e1.insert(END, str(x))
    e1.insert(END, "/")


def f8():
    x = 0
    s = e1_val.get()
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
        e1.delete(first=0, last=len(s))
        e1.insert(END, str(x))
    e1.insert(END, "X")


e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val, width=50)
e1.grid(row=0, column=0, columnspan=4)

b1 = Button(window, text="1", width=8, height=2, command=f2)
b1.grid(row=1, column=0)

b0 = Button(window, text="0", width=8, height=2, command=f3)
b0.grid(row=1, column=1)

clear = Button(window, text="C", width=8, height=2, command=f1)
clear.grid(row=1, column=2)

beq = Button(window, text="=", width=8, height=2, command=f4)
beq.grid(row=1, column=3)

badd = Button(window, text="+", width=8, height=2, command=f5)
badd.grid(row=2, column=0)

bsub = Button(window, text="-", width=8, height=2, command=f6)
bsub.grid(row=2, column=1)

bmul = Button(window, text="X", width=8, height=2, command=f8)
bmul.grid(row=2, column=2)

bdiv = Button(window, text="/", width=8, height=2, command=f7)
bdiv.grid(row=2, column=3)

window.mainloop()
