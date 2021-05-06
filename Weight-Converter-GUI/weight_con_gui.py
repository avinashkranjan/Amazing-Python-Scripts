# import libraries
from tkinter import *

# initialized window
root = Tk()
root.geometry('480x350')
root.resizable(0, 0)
root.title('Weight Converter')

# defining the function for converting weights


def WeightConv():

    # making textbox user-friendly that is editable
    t1.configure(state='normal')
    t1.delete("1.0", END)

    t2.configure(state='normal')
    t2.delete("1.0", END)

    t3.configure(state='normal')
    t3.delete("1.0", END)

    t4.configure(state='normal')
    t4.delete("1.0", END)

    t5.configure(state='normal')
    t5.delete("1.0", END)

    t6.configure(state='normal')
    t6.delete("1.0", END)

    # exception handling
    try:
        kilograms = float(e1.get())

        # insert the output in textboxes correct upto 2 places after decimal
        t1.insert(END, "%.2f" % (kilograms * 5000))
        t2.insert(END, "%.2f" % (kilograms * 1000))
        t3.insert(END, "%.2f" % (kilograms * 35.274))
        t4.insert(END, "%.2f" % (kilograms * 2.20462))
        t5.insert(END, "%.2f" % (kilograms * 0.01))
        t6.insert(END, "%.2f" % (kilograms * 0.001))

    # if blank or invalid input is given then exception is thrown
    except ValueError:
        t1.insert(END, "  ~ Invalid input ~  ")
        t2.insert(END, "  ~ Invalid input ~  ")
        t3.insert(END, "  ~ Invalid input ~  ")
        t4.insert(END, "  ~ Invalid input ~  ")
        t5.insert(END, "  ~ Invalid input ~  ")
        t6.insert(END, "  ~ Invalid input ~  ")

    # making textbox uneditable
    t1.configure(state='disabled')
    t2.configure(state='disabled')
    t3.configure(state='disabled')
    t4.configure(state='disabled')
    t5.configure(state='disabled')
    t6.configure(state='disabled')


# creating a label to display
l1 = Label(root, text="Enter the weight in kilograms (kg) : ")
l1.grid(row=1, column=1, columnspan=2)
value = StringVar()

# creating a entry box for input
e1 = Entry(root, textvariable=value)
e1.grid(row=1, column=3, columnspan=2)

# create a button for conversion
button = Button(root, text="Convert", command=WeightConv)
button.grid(row=2, column=2, columnspan=2, rowspan=2)

# make labels for textbox
t1l1 = Label(root, text="kg to ct : ")
t1l1.grid(row=4, column=1, columnspan=1)

t2l2 = Label(root, text="kg to g : ")
t2l2.grid(row=5, column=1, columnspan=1)

t3l3 = Label(root, text="kg to oz : ")
t3l3.grid(row=6, column=1, columnspan=1)

t4l4 = Label(root, text="kg to lb : ")
t4l4.grid(row=7, column=1, columnspan=1)

t5l5 = Label(root, text="kg to q : ")
t5l5.grid(row=8, column=1, columnspan=1)

t6l6 = Label(root, text="kg to t : ")
t6l6.grid(row=9, column=1, columnspan=1)

t1r1 = Label(root, text="Carat")
t1r1.grid(row=4, column=4, columnspan=1)

t2r2 = Label(root, text="Gram")
t2r2.grid(row=5, column=4, columnspan=1)

t3r3 = Label(root, text="Ounce")
t3r3.grid(row=6, column=4, columnspan=1)

t4r4 = Label(root, text="Pound")
t4r4.grid(row=7, column=4, columnspan=1)

t5r5 = Label(root, text="Quintal")
t5r5.grid(row=8, column=4, columnspan=1)

t6r6 = Label(root, text="Tonne")
t6r6.grid(row=9, column=4, columnspan=1)

# creating textbox and defining grid to show output
t1 = Text(root, height=1, width=20)
t1.grid(row=4, column=2, columnspan=2)

t2 = Text(root, height=1, width=20)
t2.grid(row=5, column=2, columnspan=2)

t3 = Text(root, height=1, width=20)
t3.grid(row=6, column=2, columnspan=2)

t4 = Text(root, height=1, width=20)
t4.grid(row=7, column=2, columnspan=2)

t5 = Text(root, height=1, width=20)
t5.grid(row=8, column=2, columnspan=2)

t6 = Text(root, height=1, width=20)
t6.grid(row=9, column=2, columnspan=2)

# making blank spaces in GUI
for r in range(10):
    root.grid_rowconfigure(r, minsize=30)
for c in range(6):
    root.grid_columnconfigure(c, minsize=50)

# infinite loop to run program
root.mainloop()
