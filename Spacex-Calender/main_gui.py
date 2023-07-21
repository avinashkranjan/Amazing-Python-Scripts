import notifly
from tkinter import *
from datetime import datetime


def notifly_execute():
    """
    Runs the notifly main script upon button press to update Google Calendar
    """
    for i in range(0, len(update_options)):
        if (update_options[i] == clicked.get()):
            months_to_update = i+1

    for month in range(datetime.today().month, datetime.today().month + months_to_update):
        notifly.button_activated(month)


def notifly_delete():
    """
    Runs the notifly delete scripts upon button press to delete rocket launch events as desired
    """
    if (delete_options[0] == clicked_delete.get()):
        notifly.delete_all()
    else:
        month_to_delete = clicked_delete.get().split()[1]
        notifly.delete_events(month_to_delete)


root = Tk()
root.title("Notifly")
root.geometry("2000x1000")
root.configure(background='black')

update_options = [
    "Input launches for this month",
    "Input launches for this month and next month",
    "Input launches for this month and the next two months"
]

delete_options = [
    "Delete all rocket launches",
    "Delete January rocket launches",
    "Delete February rocket launches",
    "Delete March rocket launches",
    "Delete April rocket launches",
    "Delete May rocket launches",
    "Delete June rocket launches",
    "Delete July rocket launches",
    "Delete August rocket launches",
    "Delete September rocket launches",
    "Delete October rocket launches",
    "Delete November rocket launches",
    "Delete December rocket launches"
]

# label 1
label = Label(text="Select from dropdown:", anchor="w")
label.configure(bg="black", fg="white")
label.grid(sticky="w", row=1, column=1)

# create dropdown
clicked = StringVar()

dropdown = OptionMenu(root, clicked, *update_options)
dropdown.grid(row=2, column=1)

# create button
notifly_button = Button(
    root, text="Add Rocket Launches to Google Calendar", padx="100", pady="100", bg="#FFFD99", command=notifly_execute)
notifly_button.grid(row=4, column=1)

# label 2
label = Label(text="Select from dropdown:", anchor="w")
label.configure(bg="black", fg="white")
label.grid(sticky="w", row=1, column=3)

# delete dropdown
clicked_delete = StringVar()

delete_dropdown = OptionMenu(root, clicked_delete, *delete_options)
delete_dropdown.grid(row=2, column=3)

# delete button
delete_button = Button(
    root, text="Delete Rocket Launches from Google Calendar", padx="100", pady="100", bg="#FFA0A0", command=notifly_delete)
delete_button.grid(row=4, column=3)


root.grid_columnconfigure(0, minsize=110)
root.grid_rowconfigure(0, minsize=80)
root.grid_columnconfigure(2, minsize=200)
root.grid_rowconfigure(3, minsize=300)

root.mainloop()
