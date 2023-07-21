# linear search visualizer
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import time

# main window
root = Tk()
root.title('Linear Search Visualizer')
# background color
root.config(bg="grey")
# disabling resizing of window
root.resizable(0, 0)

# array of elements / rectangle heights
array = []

# ~30 elements fit in the canvas using below function


def drawRect(array, color):
    canvas.delete("all")
    c_height = 380
    c_width = 1000
    x_width = c_width / (len(array) + 1)
    x_start = 15
    spacing = 10
    normalizedArray = [i / max(array) for i in array]
    for i, height in enumerate(normalizedArray):
        # top left
        x0 = i * x_width + x_start + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + x_start
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(array[i]))

    root.update_idletasks()


# generate random elements for the array and draw their rectangles on the canvas
def Generate():
    global array
    try:
        minVal = int(minEntry.get())
        maxVal = int(maxEntry.get())
        size = int(sizeEntry.get())
    except:
        messagebox.showwarning("Message", "Please enter all parameters")

    array = []
    # generating random list
    color = []
    for _ in range(size):
        array.append(random.randrange(minVal, maxVal + 1))
        color.append('#98AFC7')

    drawRect(array, color)


# search for a given key and change colours of the rectangles
def search():
    global array
    # take input key to search from user
    try:
        key = int(keyEntry.get())
    except:
        messagebox.showwarning("Message", "Please enter a key to search")

    # setting initial colour for the rectangles
    color = ['#98AFC7' for rect in range(len(array))]
    flag = False
    # elements being checked
    for i in range(len(array)):
        color[i] = 'white'
        drawRect(array, color)
        time.sleep(0.2)
        # if key is found
        if array[i] == key:
            color[i] = 'SeaGreen'
            drawRect(array, color)
            flag = True
            time.sleep(0.2)
            break
        # if key not found move on to check next element
        else:
            color[i] = 'Salmon'
            drawRect(array, color)
            time.sleep(0.2)

    # display a final message
    if flag:
        messagebox.showwarning("Success", "Key found")
    else:
        messagebox.showinfo("Failure", "Key not found")


# ---adding frames---
# top name frame
top = Frame(root, width=1300, height=200, bg='#98AFC7', bd=8, relief="groove")
top.grid(row=0, column=0, padx=10, pady=5)

# frame for canvas
canvas = Canvas(root, width=1000, height=380, bg='#C3FDB8')
canvas.grid(row=1, column=0, padx=10, pady=5)

# frame for user entries
entries = Frame(root, width=1300, height=300,
                bg='#98AFC7', bd=8, relief="groove")
entries.grid(row=2, column=0, padx=10, pady=5)


# ---adding widgets---
# top label
greeting = Label(top, text="Linear Search Visualizer", width=62,
                 font=("Courier New", 20, "bold"), background="#98AFC7")
greeting.grid(row=0, column=1, pady=5)


# user entries and buttons
# row 0
Size = Label(entries, text="Size of array : ", bg='#C3FDB8', relief="groove")
Size.grid(row=0, column=0, padx=15, pady=5, sticky=W, ipadx=20, ipady=5)
sizeEntry = Entry(entries, justify="center")
sizeEntry.grid(row=0, column=1, padx=15, pady=5, sticky=W, ipady=5)

minn = Label(entries, text="Minimum element : ",
             bg='#C3FDB8', relief="groove")
minn.grid(row=0, column=2, padx=15, pady=5, sticky=W, ipadx=20, ipady=5)
minEntry = Entry(entries, justify="center")
minEntry.grid(row=0, column=3, padx=15, pady=5, sticky=W, ipady=5)

maxx = Label(entries, text="Maximum element : ",
             bg='#C3FDB8', relief="groove")
maxx.grid(row=0, column=4, padx=15, pady=5, sticky=W, ipadx=20, ipady=5)
maxEntry = Entry(entries, justify="center")
maxEntry.grid(row=0, column=5, padx=15, pady=5, sticky=W, ipady=5)

# row 1
generate = Button(entries, text="Generate", bg='#C3FDB8', command=Generate)
generate.grid(row=1, column=1, padx=15, pady=5, ipadx=20, ipady=5)

keyToSearch = Label(entries, text="Key : ", bg='#C3FDB8', relief="groove")
keyToSearch.grid(row=1, column=2, padx=15, pady=5, ipadx=20, ipady=5)
keyEntry = Entry(entries, justify="center")
keyEntry.grid(row=1, column=3, padx=15, pady=5, ipady=5)

Search = Button(entries, text="Search", bg='#C3FDB8', command=search)
Search.grid(row=1, column=4, padx=15, pady=5, ipadx=20, ipady=5)


root.mainloop()
