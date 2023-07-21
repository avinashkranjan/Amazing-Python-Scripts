import tkinter as tk
from tkinter import ttk


def is_palindrome(word):
    word = word.lower()
    word = ''.join(char for char in word if char.isalnum())
    return word == word[::-1]


def check_palindrome():
    input_text = entry.get()
    result = is_palindrome(input_text)
    if result:
        output_label.config(text="It's a palindrome!",
                            foreground='green', font=('Arial', 14, 'bold'))
    else:
        output_label.config(text="It's not a palindrome.",
                            foreground='red', font=('Arial', 14, 'bold'))


# Create the main window
window = tk.Tk()
window.title("Palindrome Checker")
window.geometry("350x200")
window.configure(bg='white')

# Create style for the interface
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12),
                foreground='black', background='white')
style.configure('TEntry', font=('Arial', 10))
style.configure('TButton', font=('Arial', 10, 'bold'))

# Create GUI elements
display_label = ttk.Label(
    window, text="Enter a word or phrase:", font=('Arial', 14, 'bold'))
display_label.pack(pady=10)

entry = ttk.Entry(window)
entry.pack(padx=10)

check_button = ttk.Button(window, text="Check", command=check_palindrome)
check_button.pack(pady=10)

output_label = ttk.Label(window, text="", font=('Arial', 14, 'bold'))
output_label.pack(pady=10)

window.configure(bg='white')
window.mainloop()
