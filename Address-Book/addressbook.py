'''
importing all the required libraries
'''
import sqlite3
from sqlite3 import Error
from tkinter import *
import tkinter.messagebox
root = Tk()
root.geometry('600x370')
list_of_names = []
root.title('AddressBook')
Name = StringVar()
Number = StringVar()

""" creating a database connection to the SQLite database
    specified by db_file
    return: Connection object or None
    """


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        r_set = conn.execute('''SELECT * from tasks''')
        for student in r_set:
            list_of_names.append(student[1])
        return conn
    except Error as e:
        print(e)
    return conn


""" create a table from the create_table_sql statement
    conn: Connection object
    create_table_sql: a CREATE TABLE statement
    """


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    return


'''
displaying added/deleted message
'''


def onClickAdded():
    tkinter.messagebox.showinfo(" ", Name.get()+" got added")


def onClickDeleted():
    tkinter.messagebox.showinfo(" ", Name.get()+" got deleted")


""" Create a new task (ie creating new row) for the given Name  taking care of all conditions such as  Name,phone no
cannot be empty ,phone no should be 10 digits and also if  Name already exist,then it cannot be inerted
"""


def create_task():
    sql = ''' INSERT INTO tasks(name,status_id)
              VALUES(?,?) '''
    if (Name.get() not in list_of_names):

        if ((Name.get() == '') | (Number.get() == '') | (len(Number.get()) != 10)):
            top = Toplevel(root)
            top.geometry('180x100')
            if ((Number.get() == '') | (len(Number.get()) != 10)):
                myLabel = Label(top, text="Phone no should be 10  digits\n")
            else:
                myLabel = Label(top, text="NAME IS EMPTY\n")
            myLabel.pack()
            mySubmitButton = Button(top, text=' Back ', command=top.destroy)
            mySubmitButton.pack()
            return
        onClickAdded()
        cur = conn.cursor()
        cur.execute(sql, (Name.get(), Number.get()))
        conn.commit()
        return cur.lastrowid
    else:
        top = Toplevel(root)
        top.geometry('180x100')
        if (Name.get() == ''):
            myLabel = Label(top, text="NAME IS EMPTY\n")
        elif ((Number.get() == '') | (len(Number.get()) != 10)):
            myLabel = Label(top, text="Phone no should be 10  digits\n")
        else:
            myLabel = Label(top, text=Name.get()+"  Already Exist\n")
        myLabel.pack()
        mySubmitButton = Button(top, text=' Back ', command=top.destroy)
        mySubmitButton.pack()


"""
Query tasks by Name, if name not found then it gives a warning saying "NOT Found"
"""


def select_task_by_name():
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE name=?", (Name.get(),))
    rows = cur.fetchall()
    if (len(rows) == 0):
        inputDialog = MyDialog(root)
        root.wait_window(inputDialog.top)
    else:
        Number.set(rows[0][2])


"""
Editing phone no, if name not found then it gives a warning saying "NOT Found"
"""


def update_task():
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET status_id = ?   
              WHERE name = ?'''
    if ((Name.get() not in list_of_names) | (Name.get() == '')):
        inputDialog = MyDialog(root)
        root.wait_window(inputDialog.top)
        return
    cur = conn.cursor()
    cur.execute(sql, (Number.get(), Name.get()))
    conn.commit()


"""
Delete a task by name.if not found ,gives a warning!!!
"""


def delete_task():
    if ((Name.get() not in list_of_names) | (Name.get() == '')):
        inputDialog = MyDialog(root)
        root.wait_window(inputDialog.top)
        return
    onClickDeleted()
    sql = 'DELETE FROM tasks WHERE name=?'
    cur = conn.cursor()
    cur.execute(sql, (Name.get(),))
    conn.commit()


"""
Get all rows in the tasks table
"""


def select_all_tasks():
    r_set = conn.execute('''SELECT * from tasks''')
    i = 0
    j = 0
    top = Toplevel(root)
    for student in r_set:
        list_of_names.append(student[1])
        for j in range(len(student)):
            e = Entry(top, width=11, fg='Gray20')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i+1
    okButton = Button(top, text=' ok ', command=top.destroy)
    if (j == 0):
        j = 1
    okButton.grid(row=i+3, column=j-1)


'''
Getting the path of database and defining the table to be created
'''
database = r"./Address-Book/addressbook.db"
sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    status_id integer NOT NULL
                                  
                                );"""

'''
Creating connection and gives error message if connection failed
'''
conn = create_connection(database)
if conn is not None:
    create_table(conn, sql_create_tasks_table)
else:
    print("Error! cannot create the database connection.")

'''
creating dialog box for warnings!
'''


class MyDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.myLabel = Label(top, text=Name.get().upper()+" NOT FOUND!")
        self.myLabel.pack()
        self.mySubmitButton = Button(top, text='Exit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        self.top.destroy()


'''
Exiting from the application
'''


def EXIT():
    root.destroy()


'''
Resetting Name and phone no field
'''


def RESET():
    Name.set('')
    Number.set('')


'''
Creating UI for whole application
'''
Label(root, text='NAME', font='Times 15 bold').place(x=130, y=20)
Entry(root, textvariable=Name, width=42).place(x=200, y=25)
Label(root, text='PHONE NO ', font='Times 15 bold').place(x=130, y=70)
Entry(root, textvariable=Number, width=35).place(x=242, y=73)
Button(root, text=" ADD", font='Times 14 bold', bg='dark gray',
       command=create_task, width=8).place(x=130, y=110)
Button(root, text="EDIT", font='Times 14 bold', bg='dark gray',
       command=update_task, width=8).place(x=260, y=108)
Button(root, text="DELETE", font='Times 14 bold', bg='dark gray',
       command=delete_task, width=8).place(x=390, y=107.5)
Button(root, text="VIEW ALL", font='Times 14 bold', bg='dark gray',
       command=select_all_tasks, width=12).place(x=160, y=191)
Button(root, text="VIEW BY NAME", font='Times 14 bold', bg='dark gray',
       command=select_task_by_name, width=13).place(x=330, y=190)
Button(root, text="EXIT", font='Times 14 bold', bg='dark gray',
       command=EXIT, width=8).place(x=200, y=280)
Button(root, text="RESET", font='Times 14 bold', bg='dark gray',
       command=RESET, width=8).place(x=320, y=280)
root.mainloop()
