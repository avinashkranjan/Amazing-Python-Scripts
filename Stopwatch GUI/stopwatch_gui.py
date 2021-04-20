import tkinter as tk
import tkinter.font as TkFont
from datetime import datetime


def timer():
    global work
    if work:
        now = str(txt_var.get())
        m, s = map(int, now.split(":"))
        m = int(m)
        s = int(s)
        if(s < 59):
            s += 1
        elif(s == 59):
            s = 0
            if(m < 59):
                m += 1
            elif(m == 59):
                m = 0
        if(m < 10):
            m = str(0)+str(m)
        else:
            m = str(m)
        if(s < 10):
            s = str(0)+str(s)
        else:
            s = str(s)
        now = m+":"+s

        txt_var.set(now)
        if work:
            root.after(1000, timer)
# start function


def start():
    global work
    if not work:
        work = True
        timer()

# stop function


def pause():
    global work
    work = False

# reset function


def reset():
    global work
    if not work:
        txt_var.set('0:00')


if __name__ == "__main__":
    work = False

    root = tk.Tk()
    root.geometry("500x221")  # width x height
    root.title("My StopWatch")

    txt_var = tk.StringVar()
    txt_var.set('0:00')  # initial display of string
    root.config(background="lavender")

    fontstyle = TkFont.Font(family="Helvetica", size=60,)
    tk.Label(root, textvariable=txt_var, font=fontstyle,).pack()

    # creating the buttons for start,stop and reset
    T = tk.Text(root, height=0.7, width=9)
    T.pack()
    T.insert(tk.END, " mm : ss ")
    tk.Button(root, text="Start", command=start,
              bg='misty rose').pack(fill='x')
    tk.Button(root, text='Pause', command=pause,
              bg='misty rose').pack(fill='x')
    tk.Button(root, text='Reset', command=reset,
              bg='misty rose').pack(fill='x')
    tk.Button(root, text='Exit', command=root.destroy,
              bg='misty rose').pack(fill='x')
    root.mainloop()
