from tkinter import*
import random
import time;
import datetime
import tkinter.messagebox

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")
root.configure(background = 'Cadet Blue')

Tops = Frame(root,bg="Cadet Blue",bd=20,pady=5 ,relief=RIDGE)
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=( 'arial' ,58, 'bold' ),text="RESTAURANT MANAGEMENT SYSTEM",fg="Cornsilk",bg="Cadet Blue",bd=21,justify=CENTER)
lblTitle.grid(row=0,column=0)


ReceiptCal_F = Frame(root,bg="Powder Blue",bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F = Frame(ReceiptCal_F,bg="Powder Blue",bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F = Frame(ReceiptCal_F,bg="Powder Blue",bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F = Frame(ReceiptCal_F,bg="Powder Blue",bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg="Cadet Blue",bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Pizza_F = Frame(MenuFrame,bg='Cadet Blue',bd=10)
Pizza_F.pack(side=TOP)
Cost_F = Frame(MenuFrame,bg='Powder Blue',bd=4)
Cost_F.pack(side=BOTTOM)

Pizza_F = Frame(MenuFrame,bg='Powder Blue',bd=10,relief=RIDGE)
Pizza_F.pack(side=LEFT)
Drinks_F = Frame(MenuFrame,bg='Powder Blue',bd=10,relief=RIDGE)
Drinks_F.pack(side=RIGHT)

#=========================================================VARIABLES===============================================================#

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
Subtotal = StringVar()
Totalcost = StringVar()
CostofPizza = StringVar()
CostofMocktail = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator=""

E_Chicken_Pepper_Crunch = StringVar()
E_CornCheese = StringVar()
E_Double_Chicken_Sausage=StringVar()
E_Italian_Chicken_Feast=StringVar()
E_Veggie_Supreme=StringVar()
E_Tandoori_Paneer=StringVar()
E_Veg_Exotica=StringVar()
E_Malai_Chicken_Tikka=StringVar()



E_Virgin_Mojito=StringVar()
E_Blue_Lagoon=StringVar()
E_Mint_Lime_Soda=StringVar()
E_Peach_Lite=StringVar()
E_Strawberry_Punch=StringVar()
E_Guava_Splitzer=StringVar()
E_Litchi_Fantasy=StringVar()
E_Green_Apple_Mojito=StringVar()

E_Chicken_Pepper_Crunch.set("0")
E_CornCheese.set("0")
E_Double_Chicken_Sausage.set("0")
E_Italian_Chicken_Feast.set("0")
E_Veggie_Supreme.set("0")
E_Tandoori_Paneer.set("0")
E_Veg_Exotica.set("0")
E_Malai_Chicken_Tikka.set("0")

E_Virgin_Mojito.set("0")
E_Blue_Lagoon.set("0")
E_Mint_Lime_Soda.set("0")
E_Peach_Lite.set("0")
E_Strawberry_Punch.set("0")
E_Guava_Splitzer.set("0")
E_Litchi_Fantasy.set("0")
E_Green_Apple_Mojito.set("0")

DateofOrder.set(time.strftime("%d%m%y"))

#===========================================================FUNCTION=================================================================#

def iExit():
    iExit = tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return
    
def Reset():
    PaidTax.set("")
    Subtotal.set("")
    Totalcost.set("")
    CostofPizza.set("")
    CostofMocktail.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)
    
    E_Chicken_Pepper_Crunch.set("0")
    E_CornCheese.set("0")
    E_Double_Chicken_Sausage.set("0")
    E_Italian_Chicken_Feast.set("0")
    E_Veggie_Supreme.set("0")
    E_Tandoori_Paneer.set("0")
    E_Veg_Exotica.set("0")
    E_Malai_Chicken_Tikka.set("0")

    E_Virgin_Mojito.set("0")
    E_Blue_Lagoon.set("0")
    E_Mint_Lime_Soda.set("0")
    E_Peach_Lite.set("0")
    E_Strawberry_Punch.set("0")
    E_Guava_Splitzer.set("0")
    E_Litchi_Fantasy.set("0")
    E_Green_Apple_Mojito.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)



def CostofItem():
    Item1= float(E_Chicken_Pepper_Crunch.get())
    Item2= float(E_CornCheese.get())
    Item3= float(E_Double_Chicken_Sausage.get())
    Item4= float(E_Italian_Chicken_Feast.get())
    Item5= float(E_Veggie_Supreme.get())
    Item6= float(E_Tandoori_Paneer.get())
    Item7= float(E_Veg_Exotica.get())
    Item8= float(E_Malai_Chicken_Tikka.get())
    
    Item9= float(E_Virgin_Mojito.get())
    Item10= float(E_Blue_Lagoon.get())
    Item11= float(E_Mint_Lime_Soda.get())
    Item12= float(E_Peach_Lite.get())
    Item13= float(E_Strawberry_Punch.get())
    Item14= float(E_Guava_Splitzer.get())
    Item15= float(E_Litchi_Fantasy.get())
    Item16= float(E_Green_Apple_Mojito.get())

    PriceofPizza = ( Item1 * 180.0 )+ ( Item2 * 150.0 ) +( Item3 * 180.0 ) + ( Item4 * 200.0 ) \
                    + ( Item5 * 160.0 ) + ( Item6 * 170.0 ) + ( Item7 * 160.0 ) + ( Item8 * 200.0 )

    PriceofMocktail = ( Item9 * 90.0 )+ ( Item10 * 90.0 ) +( Item11 * 80.0 ) + ( Item12 * 100.0 ) \
                    + ( Item13 * 100.0 ) + ( Item14 * 100.0 ) + ( Item15 * 100.0 ) + ( Item16 * 100.0 )

    PizzaPrice= "Rs.", str('%.2f'%(PriceofPizza))
    MocktailPrice= "Rs.", str('%.2f'%(PriceofMocktail))
    CostofPizza.set(PizzaPrice)
    CostofMocktail.set(MocktailPrice)
    SC="Rs.", str('%.2f'%(15.9))
    ServiceCharge.set(SC)

    SubTotalofITEMS= "Rs.", str('%.2f'%(PriceofPizza + PriceofMocktail + 15.9))
    Subtotal.set(SubTotalofITEMS)

    Tax= "Rs.", str('%.2f'% ((PriceofPizza + PriceofMocktail + 15.9)*0.15))
    PaidTax.set(Tax)
    TT = ((PriceofPizza + PriceofMocktail + 15.9)*0.15)
    TC = "Rs.", str('%.2f'% (PriceofPizza + PriceofMocktail + 15.9 + TT))
    Totalcost.set(TC)





def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10903,609235)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + '\t' + DateofOrder.get() + "\n")
    txtReceipt.insert(END, 'Items\t\t\t\t' + "Cost of Items \n")
    txtReceipt.insert(END, 'Chicken Pepper Crunch:\t\t\t\t' + E_Chicken_Pepper_Crunch.get() + "\n")
    txtReceipt.insert(END, 'Corn & Cheese:\t\t\t\t' + E_CornCheese.get() + "\n")
    txtReceipt.insert(END, 'Double Chicken Sausage:\t\t\t\t' + E_Double_Chicken_Sausage.get() + "\n")
    txtReceipt.insert(END, 'Italian Chicken Feast:\t\t\t\t' + E_Italian_Chicken_Feast.get() + "\n")
    txtReceipt.insert(END, 'Veggie Supreme:\t\t\t\t' + E_Veggie_Supreme.get() + "\n")
    txtReceipt.insert(END, 'Tandoori Paneer:\t\t\t\t' + E_Tandoori_Paneer.get() + "\n")
    txtReceipt.insert(END, 'Veg Exotica:\t\t\t\t' + E_Veg_Exotica .get() + "\n")
    txtReceipt.insert(END, 'Malai Chicken Tikka:\t\t\t\t' + E_Malai_Chicken_Tikka.get() + "\n")
    txtReceipt.insert(END, 'Virgin Mojito:\t\t\t\t' + E_Virgin_Mojito.get() + "\n")
    txtReceipt.insert(END, 'Blue Lagoon:\t\t\t\t' + E_Blue_Lagoon.get() + "\n")
    txtReceipt.insert(END, 'Mint Lime Soda:\t\t\t\t' + E_Mint_Lime_Soda.get() + "\n")
    txtReceipt.insert(END, 'Peach Lite:\t\t\t\t' + E_Peach_Lite.get() + "\n")
    txtReceipt.insert(END, 'Strawberry Punch:\t\t\t\t' + E_Strawberry_Punch.get() + "\n")
    txtReceipt.insert(END, 'Guava Splitzer:\t\t\t\t' + E_Guava_Splitzer.get() + "\n")
    txtReceipt.insert(END, 'Litchi Fantasy:\t\t\t\t' + E_Litchi_Fantasy.get() + "\n")
    txtReceipt.insert(END, 'Green Apple Mojito:\t\t\t\t' + E_Green_Apple_Mojito.get() + "\n")
    txtReceipt.insert(END, 'Cost of Pizza:\t\t\t\t' + CostofPizza.get() + '\nTax Paid:\t\t\t\t' + PaidTax.get() + "\n")
    txtReceipt.insert(END, 'Cost of Mocktail:\t\t\t\t' + CostofMocktail.get() + '\nSubTotal :\t\t\t\t' + str(Subtotal.get()) + "\n")
    txtReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get() + '\nTotal Cost:\t\t\t\t' + str(Totalcost.get()))

#=======================================================PIZZA==================================================================#

lblSubTitle = Label(Pizza_F, font=( 'arial' ,30, 'bold','underline' ),text="PIZZA",bg="Powder Blue",bd=21,justify=LEFT)
lblSubTitle.grid(row=0)

Chicken_Pepper_Crunch = Checkbutton(Pizza_F,text="Chicken Pepper Crunch",variable=var1,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=1,sticky=W)
CornCheese = Checkbutton(Pizza_F,text="Corn & Cheese",variable=var2,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=2,sticky=W)
Double_Chicken_Sausage = Checkbutton(Pizza_F,text="Double Chicken Sausage",variable=var3,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=3,sticky=W)
Italian_Chicken_Feast = Checkbutton(Pizza_F,text="Italian Chicken Feast",variable=var4,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=4,sticky=W)
Veggie_Supreme = Checkbutton(Pizza_F,text="Veggie Supreme",variable=var5,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=5,sticky=W)
Tandoori_Paneer = Checkbutton(Pizza_F,text="Tandoori Paneer",variable=var6,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=6,sticky=W)
Veg_Exotica = Checkbutton(Pizza_F,text="Veg Exotica",variable=var7,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=7,sticky=W)
Malai_Chicken_Tikka = Checkbutton(Pizza_F,text="Malai Chicken Tikka",variable=var8,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=8,sticky=W)


txt_Chicken_Pepper_Crunch = Entry(Pizza_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                                  ,textvariable=E_Chicken_Pepper_Crunch).grid(row=1,column=1)

txt_CornCheese= Entry(Pizza_F,font =( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                      ,textvariable=E_CornCheese).grid(row=2,column=1)

txt_Double_Chicken_Sausage = Entry(Pizza_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                                   ,textvariable=E_Double_Chicken_Sausage).grid(row=3,column=1)

txt_Italian_Chicken_Feast = Entry(Pizza_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                                  ,textvariable=E_Italian_Chicken_Feast).grid(row=4,column=1)

txt_Veggie_Supreme = Entry(Pizza_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                           ,textvariable=E_Veggie_Supreme).grid(row=5,column=1)

txt_Tandoori_Paneer = Entry(Pizza_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                            ,textvariable= E_Tandoori_Paneer).grid(row=6,column=1)

txt_Veg_Exotica = Entry(Pizza_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                        ,textvariable= E_Veg_Exotica).grid(row=7,column=1)

txt_Malai_Chicken_Tikka = Entry(Pizza_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                               ,textvariable=E_Malai_Chicken_Tikka).grid(row=8,column=1)


#====================================================MOCKTAIL===================================================================#


lblSubTitle1 = Label(Drinks_F, font=( 'arial' ,30, 'bold','underline' ),text="MOCKTAILS",bg="Powder Blue",bd=21,justify=RIGHT)
lblSubTitle1.grid(row=0)

Virgin_Mojito = Checkbutton(Drinks_F,text="Virgin Mojito",variable=var9,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=1,sticky=W)
Blue_Lagoon = Checkbutton(Drinks_F,text="Blue Lagoon",variable=var10,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=2,sticky=W)
Mint_Lime_Soda = Checkbutton(Drinks_F,text="Mint Lime Soda",variable=var11,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=3,sticky=W)
Peach_Lite = Checkbutton(Drinks_F,text="Peach Lite",variable=var4,onvalue=12,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=4,sticky=W)
Strawberry_Punch = Checkbutton(Drinks_F,text="Strawberry Punch",variable=var13,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=5,sticky=W)
Guava_Splitzer = Checkbutton(Drinks_F,text="Guava Splitzer ",variable=var14,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=6,sticky=W)
Litchi_Fantasy = Checkbutton(Drinks_F,text="Litchi Fantasy",variable=var15,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=7,sticky=W)
Green_Apple_Mojito = Checkbutton(Drinks_F,text="Green Apple Mojito",variable=var16,onvalue=1,offvalue=0,font=( 'arial' ,18, 'bold' ),
                  bg="Powder Blue").grid(row=8,sticky=W)




txt_Virgin_Mojito = Entry(Drinks_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                         ,textvariable=E_Virgin_Mojito).grid(row=1,column=1)

txt_Blue_Lagoon=Entry(Drinks_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                      ,textvariable=E_Blue_Lagoon).grid(row=2,column=1)

txt_Mint_Lime_Soda =Entry(Drinks_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                          ,textvariable=E_Mint_Lime_Soda).grid(row=3,column=1)

txt_Peach_Lite=Entry(Drinks_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                     ,textvariable=E_Peach_Lite).grid(row=4,column=1)

txt_Strawberry_Punch=Entry(Drinks_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                           ,textvariable=E_Strawberry_Punch).grid(row=5,column=1)

txt_Guava_Splitzer=Entry(Drinks_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                         ,textvariable=E_Guava_Splitzer).grid(row=6,column=1)

txt_Litchi_Fantasy =Entry(Drinks_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                          ,textvariable=E_Litchi_Fantasy).grid(row=7,column=1)

txt_Green_Apple_Mojito=Entry(Drinks_F,font=( 'arial' ,16, 'bold' ),bd=8,width=6,justify=LEFT
                            ,textvariable=E_Green_Apple_Mojito).grid(row=8,column=1)

#==================================================================================================================================#


lblCostofPizza = Label(Cost_F, font=( 'arial' ,14, 'bold' ),text="Cost of Pizza\t",fg="Black",bg="Powder Blue")
lblCostofPizza.grid(row=0,column=0,sticky=W)
txtCostofPizza= Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),textvariable=CostofPizza,insertwidth=2,justify=RIGHT)
txtCostofPizza.grid(row=0,column=1)

lblCostofMocktail = Label(Cost_F, font=( 'arial' ,14, 'bold' ),text="Cost of Mocktail\t",fg="Black",bg="Powder Blue")
lblCostofMocktail.grid(row=1,column=0,sticky=W)
txtCostofMocktail= Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),textvariable=CostofMocktail,insertwidth=2,justify=RIGHT)
txtCostofMocktail.grid(row=1,column=1)

lblServiceCharge = Label(Cost_F, font=( 'arial' ,14, 'bold' ),text="Service Charge\t",fg="Black",bg="Powder Blue")
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge= Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),textvariable=ServiceCharge,insertwidth=2,justify=RIGHT)
txtServiceCharge.grid(row=2,column=1)

lblPaidTax = Label(Cost_F, font=( 'arial' ,14, 'bold' ),text="\tPaid Tax",fg="Black",bg="Powder Blue")
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax= Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),textvariable=PaidTax,insertwidth=2,justify=RIGHT)
txtPaidTax.grid(row=0,column=3)


lblSubtotal = Label(Cost_F, font=( 'arial' ,14, 'bold' ),text="\tSub Total",fg="Black",bg="Powder Blue")
lblSubtotal.grid(row=1,column=2,sticky=W)
txtSubtotal= Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),textvariable=Subtotal,insertwidth=2,justify=RIGHT)
txtSubtotal.grid(row=1,column=3)



lblTotalcost = Label(Cost_F, font=( 'arial' ,14, 'bold' ),text="\tTotal Cost",fg="Black",bg="Powder Blue")
lblTotalcost.grid(row=2,column=2,sticky=W)
txtTotalcost= Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),textvariable=Totalcost,insertwidth=2,justify=RIGHT)
txtTotalcost.grid(row=2,column=3)





#=========================================================================================================================#


txtReceipt= Text(Receipt_F,width=60,height=14,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)





btnTotal= Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=7,text="Total",
                 bg="Powder Blue",command= CostofItem).grid(row=0,column=0)

btnReceipt= Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=7,text="Receipt",
                 bg="Powder Blue",command= Receipt).grid(row=0,column=1)

btnReset= Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=7,text="Reset",
                 bg="Powder Blue",command= Reset).grid(row=0,column=2)

btnExit= Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=7,text="Exit",
                 bg="Powder Blue",command = iExit).grid(row=0,column=3)

#==================================================================================================================================#


def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""


#=============================================CALCULATOR======================================================================#

txtDisplay= Entry(Cal_F,width=45,bg="white",bd=4,font=('arial',16,'bold'),justify=RIGHT,textvariable=text_Input )
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

btn7=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="7",bg="light yellow",width=7,
            command=lambda:btnClick(7)).grid(row=2, column=0)

btn8=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="8",bg="light yellow",width=7,
            command=lambda:btnClick(8)).grid(row=2, column=1)

btn9=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="9",bg="light yellow",width=7,
            command=lambda:btnClick(9)).grid(row=2, column=2)

Addition=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="+",bg="light yellow",width=7,
            command=lambda:btnClick("+")).grid(row=2, column=3)


btn4=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="4",bg="light yellow",width=7,
            command=lambda:btnClick(4)).grid(row=3, column=0)

btn5=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="5",bg="light yellow",width=7,
            command=lambda:btnClick(5)).grid(row=3, column=1)

btn6=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="6",bg="light yellow",width=7,
            command=lambda:btnClick(6)).grid(row=3, column=2)

Subtraction=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="-",bg="light yellow",width=7,
            command=lambda:btnClick("-")).grid(row=3, column=3)


btn1=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="1",bg="light yellow",width=7,
            command=lambda:btnClick(1)).grid(row=4, column=0)

btn2=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="2",bg="light yellow",width=7,
            command=lambda:btnClick(2)).grid(row=4, column=1)

btn3=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="3",bg="light yellow",width=7,
            command=lambda:btnClick(3)).grid(row=4, column=2)

Multiplication=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="*",bg="light yellow",width=7,
            command=lambda:btnClick("*")).grid(row=4, column=3)



btn0=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="0",bg="light yellow",width=7,
            command=lambda:btnClick(0)).grid(row=5, column=0)

btnClear=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="C",bg="light yellow",width=7,
                command=btnClearDisplay).grid(row=5, column=1)

btn9Equals=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="=",bg="light yellow",width=7,
                  command=btnEqualsInput).grid(row=5, column=2)

Division=Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=("arial",16,'bold'),text="/",bg="light yellow",width=7,
            command=lambda:btnClick("/")).grid(row=5, column=3)


root.mainloop()
