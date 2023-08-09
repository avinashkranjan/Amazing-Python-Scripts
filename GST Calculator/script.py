from tkinter import *

# Function for finding CGST, SGST, and Total GST rates


def GST_Calc():
    cgst_percentField.delete(0, END)
    sgst_percentField.delete(0, END)
    total_gstField.delete(0, END)

    org_cost = int(original_priceField.get())
    N_price = int(net_priceField.get())
    total_gst_rate = ((N_price - org_cost) * 100) / org_cost
    cgst_rate = total_gst_rate / 2
    sgst_rate = total_gst_rate / 2

    cgst_percentField.insert(10, str(cgst_rate) + " % ")
    sgst_percentField.insert(10, str(sgst_rate) + " % ")

    total_gst = (N_price - org_cost)
    total_gstField.insert(10, f"₹ {total_gst:.2f}")


def clearAll():
    original_priceField.delete(0, END)
    net_priceField.delete(0, END)
    cgst_percentField.delete(0, END)
    sgst_percentField.delete(0, END)
    total_gstField.delete(0, END)


# Driver Code
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light blue")
    gui.title("GST Calculator")
    gui.geometry("500x300")

    label_font = ('Arial', 14)
    entry_font = ('Arial', 12)
    button_font = ('Arial', 12, 'bold')

    original_price = Label(gui, text="Original Price:", font=label_font)
    original_price.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    original_priceField = Entry(gui, font=entry_font)
    original_priceField.grid(row=1, column=1, padx=10, pady=10, sticky='w')

    net_price = Label(gui, text="Net Price:", font=label_font)
    net_price.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    net_priceField = Entry(gui, font=entry_font)
    net_priceField.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    find = Button(gui, text="Calculate GST", fg="black",
                  bg="light yellow", font=button_font, command=GST_Calc)
    find.grid(row=3, column=1, padx=10, pady=10, sticky='w')

    cgst_percent = Label(gui, text="CGST Rate:", font=label_font)
    cgst_percent.grid(row=4, column=0, padx=10, pady=10, sticky='w')

    cgst_percentField = Entry(gui, font=entry_font)
    cgst_percentField.grid(row=4, column=1, padx=10, pady=10, sticky='w')

    sgst_percent = Label(gui, text="SGST Rate:", font=label_font)
    sgst_percent.grid(row=5, column=0, padx=10, pady=10, sticky='w')

    sgst_percentField = Entry(gui, font=entry_font)
    sgst_percentField.grid(row=5, column=1, padx=10, pady=10, sticky='w')

    total_gst_label = Label(gui, text="Total GST Amount:", font=label_font)
    total_gst_label.grid(row=6, column=0, padx=10, pady=10, sticky='w')

    total_gstField = Entry(gui, font=entry_font)
    total_gstField.grid(row=6, column=1, padx=10, pady=10, sticky='w')

    clear = Button(gui, text="Clear All", fg="black",
                   bg="light yellow", font=button_font, command=clearAll)
    clear.grid(row=7, column=1, padx=10, pady=10, sticky='w')

    # Start the GUI
    gui.mainloop()
