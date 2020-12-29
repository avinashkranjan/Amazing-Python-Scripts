import tkinter
import threading
from tkinter import messagebox
import sys

tasks = []
timer = threading
real_timer = threading
ok_thread = True


def get_entry(event=""):
    text = todo.get()
    hour = int(time.get())
    todo.delete(0, tkinter.END)
    time.delete(0, tkinter.END)
    todo.focus_set()
    add_list(text, hour)
    if 0 < hour < 999:
        update_list()


def add_list(text, hour):
    tasks.append([text, hour])
    timer = threading.Timer(hour, time_passed, [text])
    timer.start()


def update_list():
    if todolist.size() > 0:
        todolist.delete(0, "end")
    for task in tasks:
        todolist.insert("end", "[" + task[0] + "] Time left: " + str(task[1]) + " secondes")


def time_passed(task):
    tkinter.messagebox.showinfo("Notification", "Time for : " + task)


def real_time():
    if ok_thread:
        real_timer = threading.Timer(1.0, real_time)
        real_timer.start()
    for task in tasks:
        if task[1] == 0:
            tasks.remove(task)
        task[1] -= 1
    update_list()


if __name__ == '__main__':
    # application
    app = tkinter.Tk()
    app.geometry("480x680")
    app.title("Todolist Remainder")
    app.rowconfigure(0, weight=1)

    # fenetre
    frame = tkinter.Frame(app)
    frame.pack()

    # widgets
    label = tkinter.Label(app, text="Enter work to do:",
                          wraplength = 200,
                          justify = tkinter.LEFT)
    label_hour = tkinter.Label(app, text="Enter time (secondes)",
                               wraplength = 200,
                               justify = tkinter.LEFT)
    todo = tkinter.Entry(app, width=30)
    time = tkinter.Entry(app, width=15)
    send = tkinter.Button(app, text='Add task', fg="#ffffff", bg='#6186AC', height=3, width=30, command=get_entry)
    quit = tkinter.Button(app, text='Exit', fg="#ffffff", bg='#EB6464', height=3, width=30, command=app.destroy)
    todolist = tkinter.Listbox(app)
    if tasks != "":
        real_time()

    # binding
    app.bind('<Return>', get_entry)
    
    # widgets placement
    label.place(x=0, y=10, width=200, height=25)
    label_hour.place(x=235, y=10, width=200, height=25)
    todo.place(x=62, y=30, width=200, height=25)
    time.place(x=275, y=30, width=50, height=25)
    send.place(x=62, y=60, width=50, height=25)
    quit.place(x=302, y=60, width=50, height=25)
    todolist.place(x=60, y = 100, width=300, height=300)

    app.mainloop()
    ok_thread = False
    sys.exit("FINISHED")
