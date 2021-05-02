import tkinter as tk
import smtplib

import webbrowser
from tkinter import ttk

def sendemail():


    try:
        sender=acct.get()
        recepient=reciv.get()
        msg=msgbody.get()
        passwd=password.get()
        msgtosend="""\
         from: %s \n
         %s 
        """ %(sender,msg)
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.login(sender,passwd)
        print(msgtosend)
        mail.sendmail(sender,recepient,msgtosend)
        mail.close()
        tk.Label(mainframe,text="Email Sent").grid(column=4,row=8,sticky="W")
    except Exception as e:
        tk.Label(mainframe, text=str(e)).grid(column=4, row=9, sticky="W")
        print(e)


def setup():
    webbrowser.open_new(r"https://www.gmail.com")


root=tk.Tk()
root.title("E-mail Sender")


mainframe=ttk.Frame(root,padding="4 4 13 13")
mainframe.grid(column=0,row=0,sticky=("N","W","E","S"))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)


acct=tk.StringVar()
password=tk.StringVar()
reciv=tk.StringVar()
msgbody=tk.StringVar()


lbl=tk.Label(mainframe,text="Login to Gmail",fg="green",cursor="hand2")
lbl.grid(row=0,column=3,columnspan=2,sticky="W")
lbl.bind("<Button-1>",setup)


tk.Label(mainframe,text="E-mail Address").grid(column=0,row=1,sticky="W")
acct_entry=tk.Entry(mainframe,width=30,textvariable=acct)
acct_entry.grid(column=4,row=1,sticky=("W","E"))


tk.Label(mainframe,text="Password").grid(column=0,row=2,sticky="W")
password_entry=tk.Entry(mainframe,show=" ",width=30,textvariable=password)
password_entry.grid(column=4,row=2,sticky=("W","E"))


tk.Label(mainframe,text="Reciver E-mail Address").grid(column=0,row=3,sticky="W")
reciv_entry=tk.Entry(mainframe,width=30,textvariable=reciv)
reciv_entry.grid(column=4,row=3,sticky=("W","E"))


tk.Label(mainframe,text="E-mail Contents").grid(column=0,row=5,sticky="W")
msg_entry=tk.Entry(mainframe,width=30,textvariable=msgbody)
msg_entry.grid(column=4,row=5,sticky=("W","E"))


tk.Button(mainframe,text="Send Email ",command=sendemail).grid(column=4,row=7,sticky="E")
for child in mainframe.winfo_children(): child.grid_configure(padx=5,pady=5)


acct_entry.focus()
root.mainloop()