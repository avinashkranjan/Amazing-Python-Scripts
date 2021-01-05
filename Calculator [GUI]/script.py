from tkinter import *
window=Tk()
window.title("Standard Calculator")
window.resizable(900,500)
window.geometry("600x400")

def func1():
    s=e1_val.get()
    e1.delete(first=0,last=len(s))

def func2():
    s=e1_val.get()
    e1.insert(END,"7")

def func3():
    s=e1_val.get()
    e1.insert(END,"8")

def func4():
    s=e1_val.get()
    e1.insert(END,"9")

def func5():
    x=0.0
    flag=1
    s=e1_val.get()
    for i in range (0,len(s)):
        if s[i]=='/' or s[i]=='X' or s[i]=='+' or s=='-':
            a=s[0:i]
            b=s[i+1:len(s)]
            flag=0
            if s[i]=='/':
                x=float(a)/float(b)
            elif s[i]=='X':
                x=float(a)*float(b)
            elif s[i]=='+':
                x=float(a)+float(b)
            elif s[i]=='-':
                x=float(a)-float(b)
    if flag==0:
        e1.delete(first=0,last=len(s))
        e1.insert(END,"")
        e1.insert(END,str(x))
    e1.insert(END,"/")

def func6():
    s=e1_val.get()
    e1.insert(END,"4")

def func7():
    s=e1_val.get()
    e1.insert(END,"5")

def func8():
    s=e1_val.get()
    e1.insert(END,"6")

def func9():
    x=0.0
    flag=1
    s=e1_val.get()
    for i in range (0,len(s)):
        if s[i]=='/' or s[i]=='X' or s[i]=='+' or s=='-':
            a=s[0:i]
            b=s[i+1:len(s)]
            flag=0
            if s[i]=='/':
                x=float(a)/float(b)
            elif s[i]=='X':
                x=float(a)*float(b)
            elif s[i]=='+':
                x=float(a)+float(b)
            elif s[i]=='-':
                x=float(a)-float(b)
    if flag==0:
        e1.delete(first=0,last=len(s))
        e1.insert(END,"")
        e1.insert(END,str(x))
    e1.insert(END,"X")

def func10():
    s=e1_val.get()
    e1.insert(END,"1")

def func11():
    s=e1_val.get()
    e1.insert(END,"2")

def func12():
    s=e1_val.get()
    e1.insert(END,"3")

def func13():
    x=0.0
    flag=1
    s=e1_val.get()
    for i in range (0,len(s)):
        if s[i]=='/' or s[i]=='X' or s[i]=='+' or s=='-':
            a=s[0:i]
            b=s[i+1:len(s)]
            flag=0
            if s[i]=='/':
                x=float(a)/float(b)
            elif s[i]=='X':
                x=float(a)*float(b)
            elif s[i]=='+':
                x=float(a)+float(b)
            elif s[i]=='-':
                x=float(a)-float(b)
    if flag==0:
        e1.delete(first=0,last=len(s))
        e1.insert(END,"")
        e1.insert(END,str(x))
    e1.insert(END,"-")

def func14():
    s=e1_val.get()
    e1.insert(END,"0")

def func15():
    s=e1_val.get()
    e1.insert(END,".")
    
def func16():
    x=0.0
    s=e1_val.get()
    for i in range (0,len(s)):
        if s[i]=='/' or s[i]=='X' or s[i]=='+' or s=='-':
            a=s[0:i]
            b=s[i+1:len(s)]
            if s[i]=='/':
                x=float(a)/float(b)
            elif s[i]=='X':
                x=float(a)*float(b)
            elif s[i]=='+':
                x=float(a)+float(b)
            elif s[i]=='-':
                x=float(a)-float(b)
    e1.delete(first=0,last=len(s))
    e1.insert(END,"")
    e1.insert(END,str(x))

def func17():
    x=0.0
    flag=1
    s=e1_val.get()
    for i in range (0,len(s)):
        if s[i]=='/' or s[i]=='X' or s[i]=='+' or s=='-':
            a=s[0:i]
            b=s[i+1:len(s)]
            flag=0
            if s[i]=='/':
                x=float(a)/float(b)
            elif s[i]=='X':
                x=float(a)*float(b)
            elif s[i]=='+':
                x=float(a)+float(b)
            elif s[i]=='-':
                x=float(a)-float(b)
    if flag==0:
        e1.delete(first=0,last=len(s))
        e1.insert(END,"")
        e1.insert(END,str(x))
    e1.insert(END,"+")

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val,width=80)
e1.grid(row=0,column=0,columnspan=3)

clear=Button(window,text="Clear",width=5,height=2,command=func1,fg='black', bg='yellow')
clear.grid(row=0,column=3)

b2=Button(window,text="7",width=18,height=4,command=func2,fg='black', bg='yellow')
b2.grid(row=1,column=0)

b2=Button(window,text="8",width=18,height=4,command=func3,fg='black', bg='yellow')
b2.grid(row=1,column=1)

b2=Button(window,text="9",width=18,height=4,command=func4,fg='black', bg='yellow')
b2.grid(row=1,column=2)

b2=Button(window,text="/",width=5,height=4,command=func5,fg='black', bg='yellow')
b2.grid(row=1,column=3)

b2=Button(window,text="4",width=18,height=4,command=func6,fg='black', bg='yellow')
b2.grid(row=2,column=0)

b2=Button(window,text="5",width=18,height=4,command=func7,fg='black', bg='yellow')
b2.grid(row=2,column=1)

b2=Button(window,text="6",width=18,height=4,command=func8,fg='black', bg='yellow')
b2.grid(row=2,column=2)

b2=Button(window,text="X",width=5,height=4,command=func9,fg='black', bg='yellow')
b2.grid(row=2,column=3)

b2=Button(window,text="1",width=18,height=4,command=func10,fg='black', bg='yellow')
b2.grid(row=3,column=0)

b2=Button(window,text="2",width=18,height=4,command=func11,fg='black', bg='yellow')
b2.grid(row=3,column=1)

b2=Button(window,text="3",width=18,height=4,command=func12,fg='black', bg='yellow')
b2.grid(row=3,column=2)

b2=Button(window,text="-",width=5,height=4,command=func13,fg='black', bg='yellow')
b2.grid(row=3,column=3)

b2=Button(window,text="0",width=18,height=4,command=func14,fg='black', bg='yellow')
b2.grid(row=4,column=0)

b2=Button(window,text=".",width=18,height=4,command=func15,fg='black', bg='yellow')
b2.grid(row=4,column=1)

b2=Button(window,text="=",width=18,height=4,command=func16,fg='black', bg='yellow')
b2.grid(row=4,column=2)

b2=Button(window,text="+",width=5,height=4,command=func17,fg='black', bg='yellow')
b2.grid(row=4,column=3)

window.mainloop()
