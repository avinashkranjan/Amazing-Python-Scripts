import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont


# Creating tkinter window
window = tk.Tk()
window.title('NSE Stock data')
window.geometry('1200x1000')
window.configure(bg='white')

style = ttk.Style()
style.configure('my.TButton', font=('Helvetica', 16))
style.configure('my.TFrame', background='white')

# label text for title
ttk.Label(window, text="NSE Stock market data",
          background='white', foreground="SpringGreen2",
          font=("Helvetica", 30, 'bold')).grid(row=0, column=1)

# label
ttk.Label(window, text="Select Market data to get:", background = 'white',
          font=("Helvetica", 15)).grid(column=0,
                                       row=5, padx=10, pady=25)

# Combobox creation
category = ttk.Combobox(
    window, width=60, state='readonly',font="Helvetica 15")

submit_btn = ttk.Button(window, text="Get Stock Data!", style='my.TButton')

# Adding combobox drop down list
category['values'] = ('Most Active equities - Main Board','Most Active equities - SME','Most Active equities - ETFs','Most Active equities - Price Spurts',
                        'Most Active equities - Volume Spurts','NIFTY 50 Top 20 Gainers','NIFTY 50 Top 20 Losers')

category.grid(column=1, row=5, padx=10)
category.current(0)

submit_btn.grid(row=5, column=3, pady=5, padx=15, ipadx=5)

frame = ttk.Frame(window, style='my.TFrame')
frame.place(relx=0.50, rely=0.12, relwidth=0.98, relheight=0.90, anchor="n")

query_label = tk.Text(frame ,height="52" ,width="500", bg="alice blue")
query_label.grid(row=7,  columnspan=2)

window.mainloop()
