from tkinter import *

root = Tk()
root.geometry("1350x650+0+0")
root.resizable(0, 0)
root.title("BMI CALCULATOR")


def calculate_bmi():
    Bheight = float(var2.get())
    Bweight = float(var1.get())
    BMI = Bweight / (Bheight * Bheight)

    for range_, (category, interpretation) in categories.items():
        if range_[0] <= BMI <= range_[1]:
            labelBMIResult.config(text=f"BMI: {BMI:.2f}\n\nCategory: {category}\n\nInterpretation: {interpretation}")
            break
    else:
        labelBMIResult.config(text="BMI: N/A\n\nCategory: N/A\n\nInterpretation: N/A")


var1 = DoubleVar()
var2 = DoubleVar()

categories = {
    (0, 18.5): ("Underweight", "You are underweight."),
    (18.5, 24.9): ("Normal Weight", "You have a normal."),
    (25, 29.9): ("Overweight", "You are overweight."),
    (30, 34.9): ("Obesity Level I", " Seek professional advice."),
    (35, 39.9): ("Obesity Level II", "Seek professional advice."),
    (40, float('inf')): ("Obesity Level III", " Seek immediate professional advice.")
}

Tops = Frame(root, width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=600, height=600, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width=600, height=200, bd=20, relief="raise")
f1a.pack(side=TOP)
f1b = Frame(f1, width=600, height=300, bd=20, relief='raise')
f1b.pack(side=TOP)

label1Title = Label(Tops,
                    text="          BODY MASS INDEX          ",
                    padx=16,
                    pady=16,
                    bd=16,
                    fg='#000000',
                    font=("arial", 54, 'bold'),
                    bg="powder blue",
                    relief='raise',
                    width=32,
                    height=1)
label1Title.pack()

labelweight = Label(f1a,
                    text="Select Weight in Kilograms",
                    font=('arial', 20, 'bold'),
                    bd=20).grid(row=0, column=0)
Bodyweight = Scale(f1a,
                   variable=var1,
                   from_=1,
                   to=500,
                   length=880,
                   tickinterval=30,
                   orient=HORIZONTAL)
Bodyweight.grid(row=1, column=0)

labelheight = Label(f1b,
                    text="Enter Height in Meters Square",
                    font=('arial', 20, 'bold'),
                    bd=20).grid(row=0, column=0)
textheight = Entry(f1b,
                   textvariable=var2,
                   font=('arial', 16, 'bold'),
                   bd=16,
                   width=22,
                   justify='center')
textheight.grid(row=1, column=0)

labelBMIResult = Label(f1b,
                       padx=16,
                       pady=16,
                       bd=16,
                       fg='#000000',
                       font=('arial', 14, 'bold'),  # Adjust the font size here
                       bg='sky blue',
                       relief='sunk',
                       width=34,
                       height=4,
                       justify='center')
labelBMIResult.grid(row=2, column=0)


labelBMITable = Label(f2, font=("arial", 20, 'bold'),
                      text='BMI Table').grid(row=0, column=0)
txtlabelBMITable = Text(f2,
                        height=12,
                        width=38,
                        bd=16,
                        font=("arial", 11, 'bold'))
txtlabelBMITable.grid(row=1, column=0)

txtlabelBMITable.insert(END, 'Range \t\t' + 'Category \t\t' + 'Interpretation\n\n')
for range_, (category, interpretation) in categories.items():
    txtlabelBMITable.insert(END, f'{range_[0]}-{range_[1]} \t\t{category} \t\t{interpretation}\n')

btnBMI = Button(f2,
                text="Click to \nCheck Your \nBMI",
                padx=8,
                pady=8,
                bd=12,
                width=21,
                font=("arial", 20, 'bold'),
                height=3,
                command=calculate_bmi)
btnBMI.grid(row=2, column=0)

root.mainloop()
