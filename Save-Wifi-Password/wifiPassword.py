from tkinter import Label, Button, Tk
from tkinter.filedialog import askdirectory
from backend import Pass


class Gui:
    def __init__(self):
        window = Tk()
        wifi = Pass()
        window.geometry("600x300")
        window.resizable(False, False)
        window.configure(bg='white')
        window.title('Save Wi-Fi Password')
        Label(window,
              text="Save Wi-Fi Password",
              font=("Helvetica", "25"),
              bg='white',
              fg='black').grid(row=0, padx=10, pady=3)
        Label(window, text="Find Saved Passwords:", fg='black',
              bg='white').grid(row=1, padx=10, pady=2, rowspan=2)
        Button(window,
               text="Generate",
               bg="green",
               fg="black",
               width=20,
               height=2,
               command=lambda: wifi.genPassword(),
               activebackground="#2e7541").grid(row=3,
                                                column=0,
                                                pady=10,
                                                columnspan=2)
        Button(window,
               text="Browse",
               bg="#e8e8e8",
               fg="black",
               height="2",
               width="20",
               command=lambda: wifi.chdir(askdirectory()),
               activebackground="#bababa").grid(row=3,
                                                column=1,
                                                pady=10,
                                                rowspan=2)

        window.mainloop()


start = Gui()
