import pyshorteners
from clipboard import copy
import tkinter as tk


# Function to Shorten Url
def short_url():
    try:
        url = url_input.get()
        gen_url = pyshorteners.Shortener().tinyurl.short(url)
        str_url.set(gen_url)
    except:
        str_url.set("Invalid Url!")


# Function to Copy Generated Url
def copy_url():
    copy(str_url.get())


# creating window
window = tk.Tk()

# window configs
window.geometry('550x250')
window.configure(bg='#333333')
window.title('Url Shortener')
window.resizable(False, False)

# heading
main_label = tk.Label(window,
                      text="Url Shortener",
                      font=("Helvetica", "25"),
                      bg='#333333',
                      fg='white')
main_label.grid(row=0, column=0, padx=20, pady=20)

# Input Section
label = tk.Label(window,
                 text="URL:",
                 font=("Arial", "10"),
                 bg='#333333',
                 fg='white')
label.grid(row=1, column=0, padx=0, pady=0)

url_input = tk.Entry(window)
url_input.grid(row=1, column=1, padx=2, pady=2)

btn = tk.Button(window,
                text="Generate",
                bg="green",
                fg="black",
                command=short_url,
                activebackground="#2e7541")
btn.grid(row=1, column=2, padx=3, pady=3)

# Output Section
out_label = tk.Label(window,
                     text="Shortened link:",
                     font=("Arial", "12"),
                     bg='#333333',
                     fg='yellow')
out_label.grid(row=2, column=0)
str_url = tk.StringVar(window)
shortened_url = tk.Entry(window,
                         font="Arial",
                         textvariable=str_url,
                         fg='black',
                         bg='cyan')
shortened_url.grid(row=2, column=1, padx=5, pady=10)

# copy button
copy_btn = tk.Button(window,
                     text="Copy",
                     command=copy_url,
                     fg='white',
                     bg='grey')
copy_btn.grid(row=3, column=1, padx=5, pady=10)

window.mainloop()
