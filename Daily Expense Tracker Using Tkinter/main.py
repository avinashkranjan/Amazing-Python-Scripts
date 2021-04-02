
from tkinter import *
from tkinter import ttk

import sqlite3  as db

from tkcalendar import DateEntry

def init():
    connectionObjn = db.connect("budgets.db")       #creating and connecting to a database in sqlite---
    curr = connectionObjn.cursor()
    query = '''
    create table if not exists expenses (
        Date string,
        User string,
        Material string,
        expense number
        )
    '''                                               #created the table we would use to store the information---
    curr.execute(query)
    connectionObjn.commit()

def submitexpense():
    values=[dateEntry.get(),User.get(),Material.get(),Expense.get()]
    print(values)
    Etable.insert('','end',values=values)

    connectionObjn = db.connect("budgets.db")
    curr = connectionObjn.cursor()
    query = '''
    INSERT INTO expenses VALUES 
    (?, ?, ?, ?)
    '''
    curr.execute(query,(dateEntry.get(),User.get(),Material.get(),Expense.get()))
    connectionObjn.commit()

def viewexpense():
    connectionObjn = db.connect("budgets.db")
    curr = connectionObjn.cursor()
    query = '''
     select * from expenses
    '''
    total='''
    select sum(expense) from expenses
    '''
    curr.execute(query)
    rows=curr.fetchall()
    curr.execute(total)
    amount=curr.fetchall()[0]
    print(rows)
    print(amount)
    
    l=Label(root,text="Date  User  Material  Expense",font=('comic sans',15,'bold'),bg="green",fg="cyan")
    l.grid(row=7,column=0,padx=7,pady=7)

    st=""
    for i in rows:
        for j in i:
            st+=str(j)+'\t'
        st+='\n'
    print(st)
    l=Label(root,text=st,font=('comic sans',12))
    l.grid(row=8,column=0,padx=7,pady=7)


init()
root=Tk()
root.title("Daily Expense tracker:Manage your daily finances well!")
root.geometry('800x800')

dateLabel=Label(root,text="Date",font=('comic sans',15,'bold'),bg="green",fg="cyan",width=12)
dateLabel.grid(row=1,column=0,padx=7,pady=7)

dateEntry=DateEntry(root,width=12,font=('comic sans',15,'bold'))
dateEntry.grid(row=1,column=1,padx=7,pady=7)

User=StringVar()
userLabel=Label(root, text="User",font=('comic sans',15,'bold'),bg="green",fg="cyan",width=12)
userLabel.grid(row=2,column=0,padx=7,pady=7)

userEntry=Entry(root,textvariable=User,font=('comic sans',15,'bold'))
userEntry.grid(row=2,column=1,padx=7,pady=7)



Material=StringVar()
materialLabel=Label(root, text="Material",font=('comic sans',15,'bold'),bg="green",fg="cyan",width=12)
materialLabel.grid(row=3,column=0,padx=7,pady=7)

materialEntry=Entry(root,textvariable=Material,font=('comic sans',15,'bold'))
materialEntry.grid(row=3,column=1,padx=7,pady=7)

Expense=IntVar()
expenseLabel=Label(root,text="Expense",font=('comic sans',15,'bold'),bg="green",fg="cyan",width=12)
expenseLabel.grid(row=4,column=0,padx=7,pady=7)

expenseEntry=Entry(root,textvariable=Expense,font=('comic sans',15,'bold'))
expenseEntry.grid(row=4,column=1,padx=7,pady=7)

submitbtn=Button(root,command=submitexpense,text="Submit",font=('comic sans',15,'bold'),bg="green",fg="cyan",width=12 )
submitbtn.grid(row=5,column=0,padx=13,pady=13)

viewtn=Button(root,command=viewexpense,text="View expenses",font=('comic sans',15,'bold'),bg="green",fg="cyan",width=12 )
viewtn.grid(row=5,column=1,padx=13,pady=13)

# expenses----
Elist=['Date','User','Material','Expense']



Etable=ttk.Treeview(root,column=Elist,show='headings',height=7)

for c in Elist:
    Etable.heading(c,text=c.title())
Etable.grid(row=6,column=0,padx=7,pady=7,columnspan=3)         #view the input table---

mainloop()                              #printing the data stored in the database memory---
