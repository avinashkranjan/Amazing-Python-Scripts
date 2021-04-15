from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Notebook
from tkcalendar import DateEntry
import sqlite3


def Addexpense():
    x = Edate.get()
    y = Title.get()
    z = Eexpense.get()
    data = [x,y,z]
    TVExpense.insert('','end',values=data)
    with db:
        c = db.cursor()
        c.execute("INSERT INTO expense(Dates, Items, Expense) VALUES(?,?,?)",(x,y,z))
       


def show():
    connt=sqlite3.connect('expense.db')
    cursor=connt.cursor()
    cursor.execute("SELECT * FROM expense")
    for row in cursor.fetchall():
        print(row)

def delete():
    with db:
        c = db.cursor()
        c.execute("DROP table expense")
        db.commit()

db = sqlite3.connect('expense.db')
c = db.cursor()

# uncomment this when running the script for the first time or when deleting it
# and when once the table is created comment it out

#c.execute("""CREATE TABLE expense(
 #   Dates varchar,
  #  Items varchar,
  #  Expense integer
#)""")
db.commit()

gui = Tk()
gui.title('Expense Tracker')
gui.geometry('700x600')


Tab = Notebook(gui)
F1 = Frame(Tab, width=500, height=500)

Tab.add(F1, text="Expense")


Tab.pack(fill=BOTH, expand=1)

ldate = ttk.Label(F1, text="Date", font=(None,18))
ldate.grid(row=0, column=0, padx=5, pady=5, sticky='w')

Edate = DateEntry(F1, width=19, background = 'blue', foreground='white', font=(None,18))
Edate.grid(row=0, column=1, padx=5,pady=5, sticky='w')

ltitle = ttk.Label(F1, text="Items",font=(None,18))
ltitle.grid(row=1, column=0, padx=5, pady=5, sticky='w')

Title = StringVar()

Etitle = ttk.Entry(F1, textvariable=Title,font=(None,18))
Etitle.grid(row=1, column=1, padx=5, pady=5, sticky='w')

lexpense = ttk.Label(F1, text="Expense",font=(None,18))
lexpense.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Expense = StringVar()

Eexpense = ttk.Entry(F1, textvariable=Expense,font=(None,18))
Eexpense.grid(row=2, column=1, padx=5, pady=5, sticky='w')

btn = ttk.Button(F1,text='Add', command=Addexpense)
btn.grid(row=3, column=1, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

btn2 = ttk.Button(F1,text='Delete', command=delete)
btn2.grid(row=3, column=0, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

btn1 = ttk.Button(F1,text='Show', command=show)
btn1.grid(row=3, column=2, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

TVList = ['Date','Item','Expense']
TVExpense = ttk.Treeview(F1, column=TVList, show='headings', height=5)

for i in TVList:
    TVExpense.heading(i, text=i.title())

TVExpense.grid(row=4, column=0, padx=5, pady=5, sticky='w', columnspan=3)

gui.mainloop()
db.close()