from tkinter import *
from tkinter import messagebox, simpledialog
import sqlite3
from sqlite3 import Error
import sys

# Store Master password
master_password = sys.argv[1]

# Function to connect to the SQL Database


def sql_connection():
    try:
        con = sqlite3.connect('passwordManager.db')
        return con
    except Error:
        print(Error)

# Function to create table


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS passwords(website text, username text, pass text)")
    con.commit()


# Call functions to connect to database and create table
con = sql_connection()
sql_table(con)

# Create submit function for database


def submit(con):
    cursor = con.cursor()
    # Insert Into Table
    if website.get() != "" and username.get() != "" and password.get() != "":
        cursor.execute("INSERT INTO passwords VALUES (:website, :username, :password)",
                       {
                           'website': website.get(),
                           'username': username.get(),
                           'password': password.get()
                       }
                       )
        con.commit()
        # Message box
        messagebox.showinfo("Info", "Record Added in Database!")

        # After data entry clear the text boxes
        website.delete(0, END)
        username.delete(0, END)
        password.delete(0, END)

    else:
        messagebox.showinfo("Alert", "Please fill all details!")

# Create Query Function


def query(con):

    password = simpledialog.askstring("Password", "Enter Master Password")
    if (password == master_password):
        # set button text
        query_btn.configure(text="Hide Records", command=hide)
        cursor = con.cursor()
        # Query the database
        cursor.execute("SELECT *, oid FROM passwords")
        records = cursor.fetchall()

        p_records = 'ID'.ljust(10) + 'Website'.ljust(40) + \
            'Username'.ljust(70)+'Password'.ljust(100)+'\n'

        for record in records:
            single_record = ""
            single_record += (str(record[3]).ljust(10) +
                              str(record[0]).ljust(40)+str(record[1]).ljust(70)+str(record[2]).ljust(100))
            single_record += '\n'
            # print(single_record)
            p_records += single_record
        query_label['text'] = p_records
        # Commit changes
        con.commit()
        p_records = ""

    else:
        messagebox.showinfo("Failed!", "Authentication failed!")

# Create Function to Hide Records


def hide():
    query_label['text'] = ""
    query_btn.configure(text="Show Records", command=lambda: query(con))


root = Tk()
root.title("Password Manager")
root.geometry("500x400")
root.minsize(600, 400)
root.maxsize(600, 400)

frame = Frame(root, bg="#774A9F", bd=5)
frame.place(relx=0.50, rely=0.50, relwidth=0.98, relheight=0.45, anchor="n")

# Create Text Boxes
website = Entry(root, width=30)
website.grid(row=1, column=1, padx=20, pady=5)
username = Entry(root, width=30)
username.grid(row=2, column=1, padx=20, pady=5)
password = Entry(root, width=30)
password.grid(row=3, column=1, padx=20, pady=5)

# Create Text Box Labels
website_label = Label(root, text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(root, text=" Username:")
username_label.grid(row=2, column=0)
password_label = Label(root, text="Password:")
password_label.grid(row=3, column=0)


# Create Buttons
submit_btn = Button(root, text="Add Password", command=lambda: submit(con))
submit_btn.grid(row=5, column=1, pady=5, padx=15, ipadx=35)
query_btn = Button(root, text="Show All", command=lambda: query(con))
query_btn.grid(row=6, column=1, pady=5, padx=5, ipadx=35)

# Create a Label to show stored passwords
global query_label
query_label = Label(frame, anchor="nw", justify="left")
query_label.place(relwidth=1, relheight=1)


def main():
    root.mainloop()


if __name__ == '__main__':
    main()
