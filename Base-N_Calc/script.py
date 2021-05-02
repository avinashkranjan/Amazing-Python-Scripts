from tkinter import *

def SetStatusError():
    """ Sets Status bar label to error message """
    Status["text"] = "Wronge Input(s)... :\ "
    Status["fg"] = "red"


def Con_Base_X_to_Dec(num, base_x):
    # Converting the integeral part
    integeral_part = str(int(num))[::-1]                            # Extract integerals in reverse order
    i=0
    res = 0
    for number in integeral_part:
        element = int(number) * (base_x**i)                         # Convert each number to decimal
        res += element                                              # Add element to result
        i+=1

    # Converting the decimal part
    decimal_part = str(num)
    decimal_part = decimal_part[decimal_part.index(".")+1:]         # Extract decimal part using string manipulation
    i = -1
    for decimal in decimal_part:
        element = int(decimal) * (base_x**i)                        # Convert each number to decimal
        res += element                                              # Add element to result
        i += -1

    # Return total result
    return res


def Con_Dec_to_Base_Y(num, base_y):
    # Converting the integeral part
    integeral_part = int(num)
    res_int = []
    while int(integeral_part) != 0:
        integeral_part = integeral_part / base_y                    # Divide number by base
        element = (integeral_part - int(integeral_part)) * base_y   # Get the remainder
        res_int.append(str(int(element)))                           # Append element
    res_int = res_int[::-1]                                         # Numbers are organised from LCM to HCM

    # Converting the decimal part
    decimal_part = num - int(num)
    res_dec = []
    while (decimal_part != 0):
        decimal_part = (decimal_part - int(decimal_part)) * base_y  # Multiply decimal part by base
        if str(int(decimal_part)) in res_dec:                       # Check if not duplicated, for no infinite loops
            break
        res_dec.append(str(int(decimal_part)))                      # Append element

    # Organize result
    if len(res_dec) == 0:
        res = res_int                                               # If result has decimal numbers
    else:
        res = res_int + ["."] + res_dec                             # If not

    # Return grouped result
    return " ".join(res)


def Main():
    """ Function to validate entry fields """
    # <----- Validation ----->
    # Validate Number
    num = Num_Val.get()
    try:
        num = float(num)
    except:
        Num.focus()
        SetStatusError()
        return
    # Validate Base X
    base_x = Base_X_Val.get()
    try:
        base_x = int(base_x)
    except:
        Base_X.focus()
        SetStatusError()
        return
    # Validate Base X
    base_y = Base_Y_Val.get()
    try:
        base_y = int(base_y)
    except:
        Base_Y.focus()
        SetStatusError()
        return
    # If same bases are entered
    if base_x == base_y or base_x<2 or base_y<2:
        Status["text"] = "Huh?! -_- "
        Status["fg"] = "orange"
        return
    # <----- check base x value ----->
    if base_x == 10:
        Result = Con_Dec_to_Base_Y(num, base_y)
    if base_y == 10:
        Result = Con_Base_X_to_Dec(num, base_x)
    else:
        Result = Con_Base_X_to_Dec(num, base_x)
        Result = Con_Dec_to_Base_Y(Result, base_y)

    Status["text"] = "Successfull Conversion! :0 "
    Status["fg"] = "green"
    Result_Entry_Val.set(Result)


# <----- GUI Code Beginning ----->
main_window = Tk()
main_window.title("Base-N Calculator")
Icon = PhotoImage(file="./Base-N_Calc/data/GSSOC.png")
main_window.iconphoto(False, Icon)
main_window.geometry("420x250")


# <----- Elements for number that is going to be converted -----> 
Num_Label = Label(main_window, text="Enter Number :", anchor=E, font=("Calibri", 9))
Num_Label.place(x=30,y=30)
Num_Val = StringVar()
Num = Entry(main_window, textvariable=Num_Val, font=("Calibri", 9))
Num.place(x=120,y=32)


# <----- Elements for Base-X ----->
Base_X_Label = Label(main_window, text="Base-X :", anchor=E, font=("Calibri", 9))
Base_X_Label.place(x=250,y=30)
Base_X_Val = StringVar()
Base_X = Entry(main_window, textvariable=Base_X_Val, font=("Calibri", 9))
Base_X.place(x=305,y=32,width=30)


# <----- Elements for Base-Y ----->
Base_Y_Label = Label(main_window, text="Base-Y :", anchor=E, font=("Calibri", 9))
Base_Y_Label.place(x=250,y=50)
Base_Y_Val = StringVar()
Base_Y = Entry(main_window, textvariable=Base_Y_Val, font=("Calibri", 9))
Base_Y.place(x=305,y=52,width=30)


# <----- Elements for calculate button ----->
Calculate_Button = Button(main_window, text="Convert", font=("Calibri", 9), command=Main)
Calculate_Button.place(x=180,y=75,width=80)


# <----- Elements for Result ----->
Result_Label = Label(main_window, text="Result :", anchor=E, font=("Calibri", 9))
Result_Label.place(x=100,y=130)
Result_Entry_Val = StringVar()
Result_Entry = Entry(main_window, textvariable=Result_Entry_Val, font=("Calibri", 9))
Result_Entry.configure(state='readonly')
Result_Entry.place(x=150,y=130)


# <----- Elements for Status Bar ----->
Status = Label(main_window, text="Hello!! :D", fg="green", font=("Calibri", 9), bd=1, relief=SUNKEN, anchor=W, padx=3)
Status.pack(side=BOTTOM, fill=X)


# <----- Load Main Window ----->
main_window.mainloop()
