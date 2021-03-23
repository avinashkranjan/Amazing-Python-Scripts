from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Password Manager")
root.geometry("500x400")
root.minsize(600, 400)
root.maxsize(600, 400)

frame = Frame(root, bg="#774A9F", bd=5)
frame.place(relx=0.50, rely=0.50, relwidth=0.98, relheight=0.45, anchor = "n")

#Create Text Boxes
website = Entry(root, width=30)
website.grid(row=1, column=1, padx=20,pady=5)
username = Entry(root, width=30)
username.grid(row=2, column=1, padx=20,pady=5)
password = Entry(root, width=30)
password.grid(row=3, column=1, padx=20,pady=5)

#Create Text Box Labels
website_label = Label(root, text = "Website:")
website_label.grid(row=1, column=0)
username_label = Label(root, text = " Username:")
username_label.grid(row=2, column=0)
password_label = Label(root, text = "Password:")
password_label.grid(row=3, column=0)


#Create Buttons
submit_btn = Button(root, text = "Add Password")
submit_btn.grid(row = 5, column=1, pady=5, padx=15, ipadx=35)
query_btn = Button(root, text = "Show All")
query_btn.grid(row=6, column=1, pady=5, padx=5, ipadx=35)

#Create a Label to show stored passwords
global query_label
query_label = Label(frame, anchor="nw", justify="left")
query_label.place(relwidth=1, relheight=1)

def main():
    root.mainloop()

if __name__ == '__main__':
    main()