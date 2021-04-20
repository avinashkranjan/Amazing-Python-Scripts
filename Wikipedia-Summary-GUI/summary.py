from tkinter import Tk, Frame, Toplevel, Entry, Button, Text, Scrollbar, END, INSERT
from tkinter.messagebox import showerror
from mediawiki import MediaWiki
wikipedia = MediaWiki()

# Function to get summary using wikipedia module and display it


def get_summary():
    try:
        # clear text area
        answer.delete(1.0, END)
        # show summary in text area
        topic = keyword_entry.get()
        p = wikipedia.page(topic)
        answer.insert(INSERT, p.summary)
    except Exception as error:
        showerror("Error", error)


# create a GUI window and configure it
root = Tk()
root.title("Wikipedia Summary")
root.geometry("770x650")
root.resizable(False, False)
root.configure(bg="dark grey")

# create a frame for entry and button
top_frame = Frame(root, bg="dark grey")
top_frame.pack(side="top", fill="x", padx=50, pady=10)

# create a frame for text area where summary will be displayed
bottom_frame = Frame(root, bg="dark grey")
bottom_frame.pack(side="top", fill="x", padx=10, pady=10)

# create a entry box where user can enter a keyword
keyword_entry = Entry(top_frame, font=("Arial", 20, "bold"), width=25, bd=4)
keyword_entry.pack(side="left", ipady=6)

# create a search button
search_button = Button(top_frame, text="Get Summary", font=(
    "Arial", 16, "bold"), width=15, bd=4, command=get_summary)
search_button.pack(side="right")

# create a scroll bar for text area
scroll = Scrollbar(bottom_frame)

# create a text area where summary will be displayed
answer = Text(bottom_frame, font=("Arial", 18), fg="black",
              width=55, height=20, bd=5, yscrollcommand=scroll.set)
answer.pack(side="left", fill="y")
scroll.pack(side="left", fill="y")

# start the GUI
root.mainloop()
