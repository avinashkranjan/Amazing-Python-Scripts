from tkinter import *
import urllib.request
import webbrowser
from functools import partial
from tkinter import Tk, StringVar , ttk

###################################################################        

root = Tk()
root.title('ALL IN ONE CONVERTER')
root.geometry("450x400+100+200")
labelfont = ('ariel', 56, 'bold')
l=Label(root,text='ALL IN ONE CONVERTER',font = ("Arial", 20, "italic"), justify = CENTER)
l.place(x=80,y=20)

widget = Button(None, text="QUIT", bg="white", fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=root.destroy).place(x=350,y=350)

#############################################################################################################################################

def CurrencyConverter():

    ids = {"US Dollar" : 'USD', "Euros" : 'EUR', "Indian Rupees" : 'INR', "Qatar Doha" : 'QAR', "Zimbwabe Harare" : 'ZWD', "Arab Emirates Dirham" : 'AED', "Pound Sterling" : 'GBP', "Japanese Yen" : 'JPY', "Yuan Renminbi" : 'CNY'}

    def convert(amt, frm, to):
            html =urllib.request.urlopen("http://www.exchangerate-api.com/%s/%s/%f?k=a28d653d2d4fd2727003e437" % (frm , to, amt))
            return html.read().decode('utf-8')

    def callback():
            try:
                amt = float(in_field.get())
                            
            except ValueError:
                out_amt.set('Invalid input')
                return None
            if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
                out_amt.set('Input or output unit not chosen')
                return None
            else:
                frm = ids[in_unit.get()]
                to = ids[out_unit.get()]
                out_amt.set(convert(amt, frm, to))			
			
    root = Toplevel()
    root.title("Currency Converter")

    # initiate frame
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Currency Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)
    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    # Add input field
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    # Add drop-down for input unit
    in_select = OptionMenu(mainframe, in_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha", "Zimbwabe Harare", "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3, row=1, sticky=W)

    # Add output field and drop-down
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha", "Zimbwabe Harare", "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate",command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()

#################################################################################################

def WeightConverter():
        # factors to multiply to a value to convert from the following units to meters(m)
    factors = {'kg' : 1000, 'hg' : 100, 'dg' : 10, 'g' : 1,'deg' : 0.1, 'cg' : 0.01, 'mg' : 0.001}
    ids = {"Kilogram" : 'kg', "Hectagram" : 'hg', "Decagram" : 'dg', "Decigram" : 'deg', "Kilogram" : 'kg', "gram" : 'g', "centigram" : 'cg', "milligram" : 'mg'}
    # function to convert from a given unit to another
    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    # initiate window
    root = Toplevel()
    root.title("Weight Converter")

    # initiate frame
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Weight Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    # Add input field
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    # Add drop-down for input unit
    in_select = OptionMenu(mainframe, in_unit, "Kilogram","Hectagram","Decagram", "gram", "Decigram","Centigram", "Milligram") .grid(column=3, row=1, sticky=W)

    # Add output field and drop-down
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Kilogram","Hectagram","Decagram", "gram", "Decigram","Centigram", "Milligram").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()

###########################################################################################################

def AreaConverter():
    wind = Toplevel()
    wind.minsize(width=400, height=150)
    wind.maxsize(width=400, height=150) 

    meterFactor = {'square meter':1,'square km':1000000,'square rood':1011.7141056,'square cm':0.0001,'square foot':0.09290304 ,
                    'square inch':0.00064516, 'square mile':2589988.110336, 'milimeter':0.000001,'square rod':25.29285264,
                    'square yard':0.83612736, 'square township':93239571.9721, 'square acre':4046.8564224 ,'square are': 100,
                    'square barn':1e-28, 'square hectare':10000, 'square homestead':647497.027584 }

    def convert(x, fromUnit, toUnit):    
        if fromVar.get() in meterFactor.keys() and toVar.get() in meterFactor.keys():     
            resultxt.delete(0, END)
            result = (float(str(x))*meterFactor[fromUnit])/(meterFactor[toUnit])
            resultxt.insert(0, str(result))

    titleLabel = Label (wind, text = "Area Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)

    e = Entry(wind)
    e.grid(row = 1, column = 2)    
    values = list(meterFactor.keys())    

    fromVar = StringVar(wind)
    toVar = StringVar(wind)
    fromVar.set("From Unit")
    toVar.set("To Unit")

  
    fromOption = OptionMenu(wind, fromVar, *values, command= lambda y: convert(e.get(), fromVar.get() ,toVar.get()))
    fromOption.grid(row=1, column = 3)

    toLabel = Label(wind, text="To : ", font="Arial").grid(row=2, column = 2)  
    toOption = OptionMenu(wind, toVar, *values, command= lambda x: convert(e.get(), fromVar.get() ,toVar.get()))
    toOption.grid(row=3, column = 3)

    resultxt = Entry(wind)
    resultxt.grid(row=3, column=2) 

#############################################################################################################################################################

def LengthConverter():
    # factors to multiply to a value to convert from the following units to meters(m)
    factors = {'nmi' : 1852, 'mi' : 1609.34, 'yd' : 0.9144, 'ft' : 0.3048, 'inch' : 0.0254, 'km' : 1000, 'm' : 1, 'cm' : 0.01, 'mm' : 0.001}
    ids = {"Nautical Miles" : 'nmi', "Miles" : 'mi', "Yards" : 'yd', "Feet" : 'ft', "Inches" : 'inch', "Kilometers" : 'km', "meters" : 'm', "centimeters" : 'cm', "millileters" : 'mm'}

    # function to convert from a given unit to another
    def convert(amt, frm, to):
        if frm != 'm':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    # initiate window
    root = Toplevel()
    root.title("Length Converter")

    # initiate frame
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Length Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    # Add input field
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    # Add drop-down for input unit
    in_select = OptionMenu(mainframe, in_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "meters", "centimeters", "millileters").grid(column=3, row=1, sticky=W)

    # Add output field and drop-down
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "meters", "centimeters", "millileters").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()

###################################################################################################################################################################

def TemperatureConverter():
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()

        if celTempVar.get() != 0.0:
            celToFah = (celTemp *  9/5 + 32)
            fahTempVar.set(celToFah)

        elif fahTempVar.get() != 0.0:
            fahToCel = ((fahTemp - 32) * (5/9))
            celTempVar.set(fahToCel)

    def reset():
        top = Toplevel(padx=50, pady=50)
        top.grid()
        message = Label(top, text = "Reset Complete")
        button = Button(top, text="OK", command=top.destroy)

        message.grid(row = 0, padx = 5, pady = 5)
        button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

        fahTempVar.set(int(0))
        celTempVar.set(int(0)) 
    top = Toplevel()
    top.title("Temperature Converter")
    ###MAIN###
    celTempVar = IntVar()
    celTempVar.set(int(0))
    fahTempVar = IntVar()
    fahTempVar.set(int(0))
    titleLabel = Label (top, text = "Temperature Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)
   
    celLabel = Label (top, text = "Celcius: ", font = ("Arial", 16), fg = "red")
    celLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)

    fahLabel = Label (top, text = "Fahrenheit: ", font = ("Arial", 16), fg = "blue")
    fahLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)

    celEntry = Entry (top, width = 10, bd = 5, textvariable = celTempVar)
    celEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 125 )


    fahEntry = Entry (top, width = 10, bd = 5, textvariable = fahTempVar)
    fahEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 125 )

    convertButton =Button (top, text = "Convert", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = convert)
    convertButton.grid(row = 4, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 55)

    resetButton = Button (top, text = "Reset", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = reset)
    resetButton.grid(row = 4, column = 2,ipady = 8, ipadx = 12, pady = 5, sticky = NW)
    

###################################################################################################################################################################################

def sensex(event):
    webbrowser.open_new(r"https://www.google.com/search?q=sensex%20today%20live%20chart")
def nifty(event):
    webbrowser.open_new(r"https://www.google.com/search?q=nifty%20today%20live%20chart")
def gold(event):
    webbrowser.open_new(r"https://www.google.com/search?q=gold%20today%20live%20chart")
def silver(event):
    webbrowser.open_new(r"https://www.moneycontrol.com/commodity/silver-price.html")

####################################################################################

#Hovering
def color_config(widget, color, event):
    widget.configure(foreground=color)

text =Label(root, text="SENSEX",font = ("Arial", 14, "bold"))

text.bind("<Enter>", partial(color_config, text, "red"))
text.bind("<Leave>", partial(color_config, text, "blue"))
text.pack()
text.bind("<Button-1>",sensex)
text.place(x=350,y=120)
text =Label(root, text="NIFTY",font = ("Arial", 14, "bold"))

text.bind("<Enter>", partial(color_config, text, "red"))
text.bind("<Leave>", partial(color_config, text, "blue"))
text.pack()
text.bind("<Button-1>",nifty)
text.place(x=350,y=150)

text =Label(root, text="GOLD",font = ("Arial", 14, "bold"))

text.bind("<Enter>", partial(color_config, text, "red"))
text.bind("<Leave>", partial(color_config, text, "blue"))
text.pack()
text.bind("<Button-1>",gold)
text.place(x=350,y=180)

text =Label(root, text="SILVER",font = ("Arial", 14, "bold"))

text.bind("<Enter>", partial(color_config, text, "red"))
text.bind("<Leave>", partial(color_config, text, "blue"))
text.pack()
text.bind("<Button-1>",silver)
text.place(x=350,y=210)

####################################################################################################

#TEMPERATURE CONVERTER
widget = Button(root, text="Temperature converter", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=TemperatureConverter).place(x=50,y=120)
widget = Button(root, text="Length Converter", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=LengthConverter).place(x=50,y=180)
widget = Button(root, text="Area Converter", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=AreaConverter).place(x=50,y=240)
widget = Button(root, text="Currency converter", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=CurrencyConverter).place(x=50,y=60)
widget = Button(root, text="Weight Converter", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=WeightConverter).place(x=50,y=300)

root.mainloop()
