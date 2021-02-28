from tkinter import *


def clear_all():
    Player1_field.delete(0, END)
    Player2_field.delete(0, END)
    Status_field.delete(0, END)
    # set focus on the Player1_field entry box
    Player1_field.focus_set()


def tell_status():
    p1 = Player1_field.get()
    p2 = Player2_field.get()
    p1 = p1.replace(" ", "")
    p2 = p2.replace(" ", "")
    p1 = list(p1)
    p2 = list(p2)

    Status_field.insert(10, result_flame(p1, p2))


def result_flame(x, y):
    for i in x[:]:
        if i in y:
            x.remove(i)
            y.remove(i)
    count = len(x) + len(y)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if (split_index >= 0):
            right = result[split_index + 1:]
            left = result[:split_index]
            result = right + left
        else:
            result = result[:len(result) - 1]
    return result


if __name__ == "__main__":
    # Create a GUI window
    root = Tk()
    # Set the background colour of GUI window
    root.configure(background='light pink')
    # Set the configuration of GUI window
    root.geometry("350x125")
    # set the name of tkinter GUI window
    root.title("Flames Game")
    # Create a Player 1 Name: label
    label1 = Label(root, text="Name 1 ", fg='black', bg='light green')
    # Create a Player 2 Name: label
    label2 = Label(root, text="Name 2 ", fg='black', bg='light blue')
    # Create a Relation Status: label
    label3 = Label(root, text="Relationship Status", fg='black', bg='#FFE4C4')
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    label1.grid(row=1, column=0, sticky="E")
    label2.grid(row=2, column=0, sticky="E")
    label3.grid(row=4, column=0, sticky="E")
    # Create a text entry box
    # for filling or typing the information.
    Player1_field = Entry(root)
    Player2_field = Entry(root)
    Status_field = Entry(root)
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    # ipadx keyword argument set width of entry space.
    Player1_field.grid(row=1, column=1, ipadx="50")
    Player2_field.grid(row=2, column=1, ipadx="50")
    Status_field.grid(row=4, column=1, ipadx="50")
    # Create a Submit Button and attached
    # to tell_status function
    button1 = Button(root,
                     text="Flame",
                     bg="#FF7F50",
                     fg="black",
                     command=tell_status)

    # Create a Clear Button and attached
    # to clear_all function
    button2 = Button(root,
                     text="Clear",
                     bg="#CD5C5C",
                     fg="black",
                     command=clear_all)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    button1.grid(row=3, column=1)
    button2.grid(row=5, column=1)

    # Start the GUI
    root.mainloop()
