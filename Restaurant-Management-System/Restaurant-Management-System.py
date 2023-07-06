from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management Systems")

text_input = StringVar()
operator = ""

Tops = Frame(root, width=1600, height=600, bg="white", relief=GROOVE)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, bg="white", relief=GROOVE)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, bg="sky blue", relief=GROOVE)
f2.pack(side=RIGHT)
# =====================TIME========================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Management Systems", fg="Black", bd=10)
lblInfo.grid(row=0, column=0)
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Black", bd=10)
lblInfo.grid(row=1, column=0)
# =========================calculator=================================


def btnclick(numbers):
    global operator
    operator = operator+str(numbers)
    text_input.set(operator)


def btnClearDisplay():
    global operator
    operator = " "
    text_input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


def Ref():
    x = random.randint(12908, 500876)
    randomRef = str(x)
    rand.set(randomRef)


def Exit():
    root.destroy()


def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")


txtdisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_input, bd=30,
                   insertwidth=4, bg="sky blue", justify='right')
txtdisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", bg="sky blue", command=lambda: btnclick(7)).grid(row=2, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", bg="sky blue", command=lambda: btnclick(8)).grid(row=2, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", bg="sky blue", command=lambda: btnclick(9)).grid(row=2, column=2)
Addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="+", bg="sky blue", command=lambda: btnclick("+")).grid(row=2, column=3)
# ========================================================================
btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", bg="sky blue", command=lambda: btnclick(4)).grid(row=3, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", bg="sky blue", command=lambda: btnclick(5)).grid(row=3, column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", bg="sky blue", command=lambda: btnclick(6)).grid(row=3, column=2)
Subtraction = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text="-", bg="sky blue", command=lambda: btnclick("-")).grid(row=3, column=3)
# =========================================================================
btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", bg="sky blue", command=lambda: btnclick(1)).grid(row=4, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", bg="sky blue", command=lambda: btnclick(2)).grid(row=4, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", bg="sky blue", command=lambda: btnclick(3)).grid(row=4, column=2)
Multiply = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="*", bg="sky blue", command=lambda: btnclick("*")).grid(row=4, column=3)
# ===========================================================================
btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", bg="sky blue", command=lambda: btnclick(0)).grid(row=5, column=0)
btnclear = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="C", bg="sky blue", command=btnClearDisplay).grid(row=5, column=1)
btnEquals = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                   text="=", bg="sky blue", command=btnEqualsInput).grid(row=5, column=2)
Division = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="/", bg="sky blue", command=lambda: btnclick("/")).grid(row=5, column=3)
# =====================================Restaurant Info 1=======================================
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()

lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4,
                     bg="sky blue",justify='right')
txtReference.grid(row=0, column=1)

lblFries = Label(f1, font=('arial', 16, 'bold'), text="Large Fries", bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4,
                 bg="sky blue", justify='right')
txtFries.grid(row=1, column=1)

lblBurger = Label(f1, font=('arial', 16, 'bold'), text="Burger Meal", bd=16, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4,
                  bg="sky blue", justify='right')
txtBurger.grid(row=2, column=1)


lblFilet = Label(f1, font=('arial', 16, 'bold'), text="Filet_O_Meal", bd=16, anchor='w')
lblFilet.grid(row=3, column=0)
txtFilet = Entry(f1, font=('arial', 16, 'bold'), textvariable=Filet,
                 bd=10, insertwidth=4, bg="sky blue", justify='right')
txtFilet.grid(row=3, column=1)


lblChicken = Label(f1, font=('arial', 16, 'bold'), text="Chicken Meal", bd=16, anchor='w')
lblChicken.grid(row=4, column=0)
txtChicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken_Burger, bd=10, insertwidth=4,
                   bg="sky blue", justify='right')
txtChicken.grid(row=4, column=1)

lblCheese = Label(f1, font=('arial', 16, 'bold'), text="Cheese Meal", bd=16, anchor='w')
lblCheese.grid(row=5, column=0)
txtCheese = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cheese_Burger,
                  bd=10, insertwidth=4, bg="sky blue", justify='right')
txtCheese.grid(row=5, column=1)

# ===================Restaurant Info 2================================================

lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks,
                  bd=10, insertwidth=4, bg="sky blue", justify='right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor='w')
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost,
                bd=10, insertwidth=4, bg="sky blue", justify='right')
txtCost.grid(row=1, column=3)

lblService = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=2, column=2)
txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4,
                   bg="sky blue", justify='right')
txtService.grid(row=2, column=3)


lblStateTax = Label(f1, font=('arial', 16, 'bold'), text="State Tax",
                    bd=16, anchor='w')
lblStateTax.grid(row=3, column=2)
txtStateTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax,
                    bd=10, insertwidth=4, bg="sky blue", justify='right')
txtStateTax.grid(row=3, column=3)


lblSubTotal = Label(f1, font=('arial', 16, 'bold'),
                    text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal,
                    bd=10, insertwidth=4, bg="sky blue", justify='right')
txtSubTotal.grid(row=4, column=3)


lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="sky blue", justify='right')
txtTotalCost.grid(row=5, column=3)
# =========================================================================================================
btnTotal = Button(f1, padx=10, pady=8, bd=5, fg="black", font=('arial', 20, 'bold'),
                  width=7, text="Total", bg="sky blue", command=Total).grid(row=7, column=1)
btnReset = Button(f1, padx=10, pady=8, bd=10, fg="black", font=('arial', 20, 'bold'),
                  width=7, text="Reset", bg="sky blue", command=Reset).grid(row=7, column=2)
btnExit = Button(f1, padx=10, pady=8, bd=10, fg="black", font=('arial', 20, 'bold'),
                 width=7, text="Exit", bg="sky blue", command=Exit).grid(row=7, column=3)
root.mainloop()

