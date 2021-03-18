# sticky notes application
import tkinter as tk

def display():
    import time
    current_time = time.strftime("%H:%M")
    print("Welcome to Sticky notes. Here you can create sticky notes, easily.")
    time.sleep(2)
    note_input = input("Type your notes ")
    note = ("%s") % note_input
    time.sleep(1)
    # prevents GUI from popping up before it receives input.
    root = tk.Tk()
    root.title("Sticky notes")
    root.geometry("400x400")
    # changes the width and height of the GUI.
    tk.Label(root, text=current_time).pack()
    # prints out the current time.
    tk.Label(root, text=note).pack()
    # prints the inputed text by user.
    root.mainloop()
    # keeps the sticky notes open and display text until the program is closed.

display()
