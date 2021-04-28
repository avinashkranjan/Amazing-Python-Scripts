from tkinter import *

# Function for finding GST rate
def GST_Calc() :
    
    gst_percentField.delete(0, END)

    org_cost= int(original_priceField.get())
    
    N_price = int(net_priceField.get())

    gst_rate = ((N_price - org_cost) * 100) / org_cost; 

    gst_percentField.insert(10, str(gst_rate) + " % ") 

def clearAll():
 
    original_priceField.delete(0, END)
    
    net_priceField.delete(0, END)
    
    gst_percentField.delete(0, END)
    

# Driver Code
if __name__ == "__main__" :

    gui = Tk() 
  
    gui.configure(background = "light blue") 
    
    gui.title("GST Calculator") 
    
    gui.geometry("500x500") 

    original_price = Label(gui, text = "Original Price", 
                    font=(None,18))

    original_price.grid(row = 1, column = 1,padx = 10,pady = 10,sticky='w')

    original_priceField = Entry(gui)

    original_priceField.grid(row = 1, column = 2 ,padx = 10,pady = 10,sticky='w')

    
    net_price = Label(gui, text = "Net Price", 
                    font=(None,18))

    net_price.grid(row = 2, column = 1, padx = 10, pady = 10,sticky='w')
    net_priceField = Entry(gui)
    net_priceField.grid(row = 2, column = 2, padx = 10,pady = 10,sticky='w')


    find = Button(gui, text = "Find", fg = "Black", 
                bg = "light yellow", 
                command = GST_Calc)
    find.grid(row = 3, column = 2,padx = 10,pady = 10,sticky='w')
    
    gst_percent = Label(gui, text = "Gst Rate", font=(None,18)) 
    gst_percent.grid(row = 4, column = 1,padx = 10, pady = 10,sticky='w')
    gst_percentField = Entry(gui)

    gst_percentField.grid(row = 4, column = 2, padx = 10,pady = 10,sticky='w')

    clear = Button(gui, text = "Clear", fg = "Black",
                bg = "light yellow",
                command = clearAll)      
    
    clear.grid(row = 5, column = 2, padx = 10, pady = 10,sticky='w') 
    
    # Start the GUI 
    gui.mainloop()
