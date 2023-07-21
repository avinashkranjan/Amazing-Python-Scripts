from tkinter import *  # import everything from tkinter module
from time import strftime  # import strftime from time module for getting the time

root = Tk()  # create a GUI with tkinter
root.title('Clock_Python')  # title of the window
lbl = Label(root, font=('callibri', 45, 'bold'),  # specify the font, font size, and others like bold,italics,underlined,etc..
            background='black',  # background color
            foreground='white')  # foreground color


def time():  # call this function to display the time
    string = strftime('%H:%M:%S %p')  # specify the format of the time
    lbl.config(text=string)  # get the time in the specified format
    lbl.after(1000, time)


lbl.pack(anchor='center')  # centre align the text
time()  # show the time

mainloop()  # loop the program

# now you can make it a standalone desktop app (.exe) with pyinstaller or auto-py-to-exe
