# Importing required libraries
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import random

# function to create screen for the game


def board():
    global value, w
    # initialising screen
    root = Tk()
    root.geometry("320x335")
    root.title("MineSweeper")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    # creating label
    w = Label(root, text="Start Playing!", bg='yellow', fg='red')
    # creating buttons
    but11 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but11, root))
    but12 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but12, root))
    but13 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but13, root))
    but14 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but14, root))
    but15 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but15, root))
    but21 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but21, root))
    but22 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but22, root))
    but23 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but23, root))
    but24 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but24, root))
    but25 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but25, root))
    but31 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but31, root))
    but32 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but32, root))
    but33 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but33, root))
    but34 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but34, root))
    but35 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but35, root))
    but41 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but41, root))
    but42 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but42, root))
    but43 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but43, root))
    but44 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but44, root))
    but45 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but45, root))
    but51 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but51, root))
    but52 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but52, root))
    but53 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but53, root))
    but54 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but54, root))
    but55 = Button(root, bg="grey", text="", padx=7.5, pady=5, bd=4,
                   font="digifacewide 18", height=1, width=2, command=lambda: game(but55, root))
    # adding buttons to the screen
    but11.grid(row=1, column=1)
    but12.grid(row=1, column=2)
    but13.grid(row=1, column=3)
    but14.grid(row=1, column=4)
    but15.grid(row=1, column=5)
    but21.grid(row=2, column=1)
    but22.grid(row=2, column=2)
    but23.grid(row=2, column=3)
    but24.grid(row=2, column=4)
    but25.grid(row=2, column=5)
    but31.grid(row=3, column=1)
    but32.grid(row=3, column=2)
    but33.grid(row=3, column=3)
    but34.grid(row=3, column=4)
    but35.grid(row=3, column=5)
    but41.grid(row=4, column=1)
    but42.grid(row=4, column=2)
    but43.grid(row=4, column=3)
    but44.grid(row=4, column=4)
    but45.grid(row=4, column=5)
    but51.grid(row=5, column=1)
    but52.grid(row=5, column=2)
    but53.grid(row=5, column=3)
    but54.grid(row=5, column=4)
    but55.grid(row=5, column=5)
    # adding label to the screen
    w.grid(row=0, column=0, columnspan=6)
    # creating values for each cell from 1-5 and "b" for bomb
    butlist = [but11, but12, but13, but14, but15, but21, but22, but23, but24, but25,
               but31, but32, but33, but34, but35, but41, but42, but43, but44, but45,
               but51, but52, but53, but54, but55]
    vallist = ['1', '2', '3', '4', '1', '2', '3', '4', '1', '2', '3', '4', '1', '2', '3', '4',
               '1', '2', '3', '4', 'b', 'b', 'b', 'b', 'b']
    value = {}
    random.shuffle(vallist)  # shuffle for randomness
    for i in range(25):
        value[butlist[i]] = vallist[i]  # assining values to buttons
    root.mainloop()


def game(b, tk):
    if value[b] == 'b':  # if bomb is clicked
        bomb_clicked(b, tk)
    else:  # if number is clicked
        number_clicked(b, int(value[b]), tk)


total = 0

# function when bomb is clicked


def bomb_clicked(b, tk):
    # making changes to cell
    b['text'] = "\U0001f600"
    b['relief'] = SUNKEN
    b['bg'] = "orange"
    global value, total
    # displaying message and asking for replay
    a = mb.askquestion("YOU LOSE", "       Your score : " +
                       str(total) + "\nDo you want to play again??")

    tk.destroy()  # exiting current board
    if a == 'yes':
        total = 0
        board()


def number_clicked(b, n, tk):
    global value, total
    if n != 0 and b['text'] == "":
        # making changes to cell and updating score
        b['text'] = n
        total += n
        value[b] = '0'
        w['text'] = "Your Score : " + str(total)
        if total >= 50:  # if player reached score of 50 he won
            b['text'] = "\U0001f600"
            b['relief'] = SUNKEN
            b['bg'] = "orange"
            # displaying message and asking for replay
            a = mb.askquestion("YOU WON", "       Your score : " +
                               str(total) + "\nDo you want to play again??")
            tk.destroy()  # exiting current board
            if a == 'yes':
                total = 0
                board()
            # showinfo("YOU WON", "YOUR SCORE : " + str(total))
            tk.destroy()


board()
