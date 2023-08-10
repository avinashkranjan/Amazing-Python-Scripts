import tkinter as tk
from itertools import permutations


def find_anagrams():
    a = entry.get().strip().lower()

    if a:
        b = a.split()
        c = []
        for d in b:
            e = ["".join(f) for f in permutations(d)]
            c.extend(e)

        y.set(", ".join(c))
    else:
        y.set("Please enter a valid string.")


app = tk.Tk()
app.title("Anagram Finder")

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Enter a string:")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame)
entry.grid(row=0, column=1, padx=10)

find_button = tk.Button(frame, text="Find Anagrams", command=find_anagrams)
find_button.grid(row=0, column=2, padx=10)

y = tk.StringVar()
result_label = tk.Label(frame, textvariable=y, wraplength=300)
result_label.grid(row=1, columnspan=3, pady=10)

frame.config(bg="#333")
label.config(fg="white")
entry.config(bg="gray", fg="white")
find_button.config(bg="gray", fg="white")
result_label.config(bg="#333", fg="white")
app.mainloop()
