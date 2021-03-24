from tkinter import *

root = Tk()
root.title("Dictionary")
root.geometry("500x400")


def getMeaning():
    frame1 = Frame(root)
    Label(frame1, text="Meaning:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
    meaning = Label(frame1, text="", font=("Helvetica 10"))
    meaning.pack()
    frame1.pack(pady=10)
    

# Heading Label
heading_label = Label(root, text = "DICTIONARY", font=("Helvetica 21 bold"))
heading_label.config(anchor=CENTER)
heading_label.pack(pady=10)

frame = Frame(root)
Label(frame, text="Enter Word", font=("Helvetica 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))
word.pack(padx=10)
frame.pack()

search_button=Button(root, text="Search Word", font=("Helvetica 15 bold"), command=getMeaning)
search_button.config(anchor=CENTER)
search_button.pack(pady=10)


# Execute Tkinter
root.mainloop()
