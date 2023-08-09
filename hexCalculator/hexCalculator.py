import tkinter as tk


def hex_add():
    try:
        num1 = int(entry1.get(), 16)
        num2 = int(entry2.get(), 16)
        result = hex(num1 + num2)
        output.config(text="Result: " + result.upper())
    except ValueError:
        output.config(text="Invalid Input")


def hex_subtract():
    try:
        num1 = int(entry1.get(), 16)
        num2 = int(entry2.get(), 16)
        result = hex(num1 - num2)
        output.config(text="Result: " + result.upper())
    except ValueError:
        output.config(text="Invalid Input")


def hex_multiply():
    try:
        num1 = int(entry1.get(), 16)
        num2 = int(entry2.get(), 16)
        result = hex(num1 * num2)
        output.config(text="Result: " + result.upper())
    except ValueError:
        output.config(text="Invalid Input")


def hex_divide():
    try:
        num1 = int(entry1.get(), 16)
        num2 = int(entry2.get(), 16)
        result = hex(num1 // num2)
        output.config(text="Result: " + result.upper())
    except (ValueError, ZeroDivisionError):
        output.config(text="Invalid Input")


# Main tkinter window
root = tk.Tk()
root.title("Hex Calculator")

# Entry fields
entry1 = tk.Entry(root, width=15)
entry1.grid(row=0, column=0, padx=10, pady=5)
entry2 = tk.Entry(root, width=15)
entry2.grid(row=0, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(root, text="Add", command=hex_add)
add_button.grid(row=1, column=0, padx=10, pady=5)
subtract_button = tk.Button(root, text="Subtract", command=hex_subtract)
subtract_button.grid(row=1, column=1, padx=10, pady=5)
multiply_button = tk.Button(root, text="Multiply", command=hex_multiply)
multiply_button.grid(row=2, column=0, padx=10, pady=5)
divide_button = tk.Button(root, text="Divide", command=hex_divide)
divide_button.grid(row=2, column=1, padx=10, pady=5)

# Output Label
output = tk.Label(root, text="Result: ")
output.grid(row=3, columnspan=2)

root.mainloop()
