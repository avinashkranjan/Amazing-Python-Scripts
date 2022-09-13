# import libraries
import tkinter as tk
from datetime import date

# GUI App class
class App:
    def __init__(self):
        # initialized window
        self.master = tk.Tk()
        self.master.geometry('280x300')
        self.master.configure(bg="lightblue")
        self.master.resizable(0, 0)
        self.master.title('Age Calculator')
        self.statement = tk.Label(self.master)

    def run(self):
        # creating a label for person's name to display
        self.l1 = tk.Label(text="Name: ", font="courier 10", bg="lightblue")
        self.l1.grid(row=1, column=0)
        nameValue = tk.StringVar()

        # creating a entry box for input
        self.nameEntry = tk.Entry(self.master, textvariable=nameValue, relief="solid")
        self.nameEntry.grid(row=1, column=1, padx=10, pady=10)

        # label for year in which user was born
        self.l2 = tk.Label(text="Year: ", font="courier 10", bg="lightblue")
        self.l2.grid(row=2, column=0)
        yearValue = tk.StringVar()
        self.yearEntry = tk.Entry(self.master, textvariable=yearValue, relief="solid")
        self.yearEntry.grid(row=2, column=1, padx=10, pady=10)

        # label for month in which user was born
        self.l3 = tk.Label(text="Month: ", font="courier 10", bg="lightblue")
        self.l3.grid(row=3, column=0)
        monthValue = tk.StringVar()
        self.monthEntry = tk.Entry(self.master, textvariable=monthValue, relief="solid")
        self.monthEntry.grid(row=3, column=1, padx=10, pady=10)

        # label for day/date on which user was born
        self.l4 = tk.Label(text="Day: ", font="courier 10", bg="lightblue")
        self.l4.grid(row=4, column=0)
        dayValue = tk.StringVar()
        self.dayEntry = tk.Entry(self.master, textvariable=dayValue, relief="solid")
        self.dayEntry.grid(row=4, column=1, padx=10, pady=10)

        # defining the function for calculating age
        def ageCalc():
            self.statement.destroy()
            today = date.today()
            birthDate = date(int(self.yearEntry.get()), int(
                self.monthEntry.get()), int(self.dayEntry.get()))
            age = today.year - birthDate.year
            if today.month < birthDate.month or today.month == birthDate.month and today.day < birthDate.day:
                age -= 1
            self.statement = tk.Label(text=f"{nameValue.get()}'s age is {age}.", font="courier 10", bg="lightblue")
            self.statement.grid(row=6, column=1, pady=15)

        # create a button for calculating age
        self.button = tk.Button(text="Calculate age", font="courier 12 bold", fg="white", bg="dodgerblue", command=ageCalc)
        self.button.grid(row=5, column=1)
        
        # infinite loop to run program
        self.master.mainloop()
        

if __name__ == '__main__':
    age_calc = App()
    age_calc.run()
    
