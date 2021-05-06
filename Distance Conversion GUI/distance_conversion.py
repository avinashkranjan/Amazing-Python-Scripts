import tkinter as tk
from tkinter import *
from tkinter import messagebox

# main window
root = tk.Tk()
# window size (width x height)
root.geometry("600x350")
# title of window
root.title("Distance Unit Converter")
# disabling resizing of window
root.resizable(0, 0)
# background colour of window
root['bg'] = 'skyblue'

# conversion factors
conv_factors = {
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "feet": 0.3048,
    "miles": 1609.344,
    "inches": 0.0254,
    "yards": 0.9144
}

# function to convert from one unit to other


def convert():
    ip = float(input.get())
    ip_unit = ip_opt.get()
    op_unit = op_opt.get()
    # if user chooses same input & output unit then display warning
    if(ip_unit == op_unit):
        messagebox.showwarning("Warning", "Select different units")
    # else perform conversion
    else:
        output.delete(0, END)
        ans = ip*(conv_factors[ip_unit]/conv_factors[op_unit])
        output.insert(0, round(ans, 4))


# menu default text
ip_opt = StringVar()
ip_opt.set("Select Unit")
op_opt = StringVar()
op_opt.set("Select Unit")

# Adding Widgets
greeting = Label(text="Welcome to Distance Unit Converter !!", bg="lavender",
                 width=40, height=2, bd=2, relief="ridge", font=("Lucida Console", 10, "italic"))
greeting.grid(row=0, column=1, pady=20, padx=12)

# ---input row---
fromlabel = Label(root, text="From", width=10, height=2)
fromlabel.grid(row=2, column=0, padx=20, pady=20)

input = Entry(root, justify="center")
input.grid(row=2, column=1, ipady=8)
input.config(font=8)

ipmenu = OptionMenu(root, ip_opt, "cm", "m", "km",
                    "feet", "miles", "inches", "yards")
ipmenu.grid(row=2, column=2)

# ---output row---
tolabel = Label(root, text="To", width=10, height=2)
tolabel.grid(row=4, column=0, padx=20, pady=20)

output = Entry(root, justify="center")
output.grid(row=4, column=1, ipady=8)
output.config(font=8)

opmenu = OptionMenu(root, op_opt, "cm", "m", "km",
                    "feet", "miles", "inches", "yards")
opmenu.grid(row=4, column=2)

# ---convert Button---
convertbtn = Button(root, text="Convert", justify="center", width=10,
                    height=2, command=convert, bg="lavender", font=("bold", 12))
convertbtn.grid(row=6, column=1)

root.mainloop()
