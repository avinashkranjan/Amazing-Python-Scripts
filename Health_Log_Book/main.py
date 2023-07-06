# importing the modules
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
import database


# creating a function to return date and time
def getdate():
    return datetime.datetime.now()


# Creating the connection
connection = database.connect()
database.create_table1(connection)
database.create_table2(connection)


def store_exercise():
    date = getdate()
    data = exercise_entry.get("1.0", 'end-1c')
    if data != "":
        exercise_entry.delete("1.0", "end")
        database.add_exercise(connection, date, data)
        messagebox.showinfo("Success", "Log is inserted")
    else:
        messagebox.showerror("Error", "Enter Something")


def store_food():
    date = getdate()
    data = food_entry.get("1.0", "end-1c")
    if data != "":
        food_entry.delete("1.0", "end")
        database.add_food(connection, date, data)
        messagebox.showinfo("Success", "Log is inserted")
    else:
        messagebox.showerror("Error", "Enter Something")


def show_exercise():
    con = database.connect()
    cor = con.cursor()
    try:
        cor.execute('''SELECT * from exercise''')
        rows = cor.fetchall()
        new = tk.Tk()
        new.title("Exercise Log")
        new.geometry("650x500")

        frm = tk.Frame(new)
        frm.pack(side=tk.LEFT, padx=20)

        tv = ttk.Treeview(frm, selectmode='browse')
        tv.pack()
        verscrlbar = ttk.Scrollbar(new,
                                   orient="vertical",
                                   command=tv.yview)

        verscrlbar.pack(side='right', fill='x')

        tv.configure(xscrollcommand=verscrlbar.set)

        tv["columns"] = ("1", "2", "3")
        tv['show'] = 'headings'

        tv.column("1", width=50, anchor='c')
        tv.column("2", width=250, anchor='c')
        tv.column("3", width=400, anchor='w')

        tv.heading("1", text="Sl.No")
        tv.heading("2", text="Time")
        tv.heading("3", text="Data")

        for i in rows:
            tv.insert("", "end", values=i)

        new.mainloop()
    except:
        messagebox.showerror("Error", "Some Error Occurred")


def show_food():
    con = database.connect()
    cor = con.cursor()
    try:
        cor.execute('''SELECT * from food''')
        rows = cor.fetchall()
        new = tk.Tk()
        new.title("Food Log")
        new.geometry("650x500")

        frm = tk.Frame(new)
        frm.pack(side=tk.LEFT, padx=20)

        tv = ttk.Treeview(frm, selectmode='browse')
        tv.pack()
        verscrlbar = ttk.Scrollbar(new,
                                   orient="vertical",
                                   command=tv.yview)

        verscrlbar.pack(side='right', fill='x')

        tv.configure(xscrollcommand=verscrlbar.set)

        tv["columns"] = ("1", "2", "3")
        tv['show'] = 'headings'

        tv.column("1", width=50, anchor='c')
        tv.column("2", width=250, anchor='c')
        tv.column("3", width=400, anchor='w')

        tv.heading("1", text="Sl.No")
        tv.heading("2", text="Time")
        tv.heading("3", text="Data")

        for i in rows:
            tv.insert("", "end", values=i)

        new.mainloop()
    except:
        messagebox.showerror("Error", "Some Error Occurred")


def delete_exercise_log():
    messagebox.showinfo("Delete", "The Exercise Log is deleted")
    database.delete_exercise(connection)


def delete_food_log():
    messagebox.showinfo("Delete", "The Food Log is deleted")
    database.delete_food(connection)


# Making the GUI
root = tk.Tk()

root.title("main")
root.geometry("500x500")

heading = tk.Label(root, text="Health Log book",
                   font=('Helvetica', 18, 'bold'))
heading.pack()

exercise_heading = tk.Label(
    root, text=" 1) Enter each exercise separated with commas", font=('Helvetica', 11, 'bold'))
exercise_heading.place(x=30, y=40)

exercise_entry = tk.Text(root, height=5, width=42)
exercise_entry.pack(pady=30)

exercise_submit = tk.Button(root, text="Submit", command=store_exercise)
exercise_submit.place(x=210, y=160)

food_heading = tk.Label(root, text="2) Enter each food separated with commas", font=(
    'Helvetica', 11, 'bold'))
food_heading.place(x=30, y=200)

food_entry = tk.Text(root, height=5, width=42)
food_entry.pack(pady=40)

food_submit = tk.Button(root, text="Submit", command=store_food)
food_submit.place(x=210, y=330)

retrieve_exercise = tk.Button(
    root, text="Show Exercise Log", command=show_exercise)
retrieve_exercise.place(x=50, y=400)

retrieve_food = tk.Button(root, text="Show food Log", command=show_food)
retrieve_food.place(x=300, y=400)

delete_exercise = tk.Button(
    root, text="Delete Exercise Log", command=delete_exercise_log)
delete_exercise.place(x=50, y=450)

delete_food = tk.Button(root, text="Delete food Log", command=delete_food_log)
delete_food.place(x=300, y=450)

root.mainloop()
