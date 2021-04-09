# python program demonstrating
# Combobox widget using tkinter
import tkinter as tk
from tkinter import ttk

# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry('800x850')

# label text for title
ttk.Label(window, text="IPL Statistics",
          background='blue', foreground="white",
          font=("Helvetica", 20)).grid(row=0, column=1)

# label
ttk.Label(window, text="Select category and year :",
          font=("Helvetica", 15)).grid(column=0,
                                       row=5, padx=10, pady=25)


def getSearchvals():
    print(category.get(), year.get())


# Combobox creation
category = ttk.Combobox(
    window, width=27, state='readonly')
year = ttk.Combobox(
    window, width=27, state='readonly')

submit_btn = ttk.Button(window, text="Search", command=getSearchvals)

# Adding combobox drop down list
category['values'] = ('Most Runs', 'Most Fours',
                      'Most Sixes', 'Most Fifties', 'Most Centuries', 'Highest Scores', 'Most Wickets', 'Most Maidens', 'Most Dot Balls', 'Best Bowling Average', 'Best Bowling Economy', 'Best Bowling Strike Rate')

year['values'] = ('2020', '2019',  '2018', '2017',  '2016',
                  '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008')

category.grid(column=1, row=5, padx=10)
category.current(0)

year.grid(column=2, row=5, padx=10)
year.current(0)

submit_btn.grid(row=5, column=3, pady=5, padx=15, ipadx=5)

frame = ttk.Frame(window)
frame.place(relx=0.50, rely=0.12, relwidth=0.98, relheight=0.90, anchor="n")

# global query_label
query_label = ttk.Label(
    frame, anchor="nw", justify="left", text=("The workspace above has a list of tasks/ideas that could serve as utilities for managing OpenAPI specifications eg. cleanup tasks, adding default responses.\n")*50)
query_label.grid(row=7,  columnspan=2)

# query_label['text'] = "The workspace above has a list of tasks/ideas that could serve as utilities for managing OpenAPI specifications eg. cleanup tasks, adding default responses."

window.mainloop()
