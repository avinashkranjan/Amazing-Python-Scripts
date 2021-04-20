import requests
import tkinter as tk
from tkinter import ttk


def calculate_conversion():
    # URL of respective API
    url = "https://api.exchangerate-api.com/v4/latest/INR"

    # Receive Data from API
    data = requests.get(url).json()
    currency_rates = data['rates']

    # get From amount from GUI
    amount = float(from_amount.get())

    # Get country code from GUI
    fc = from_currency_code.get()
    tc = to_currency_code.get()

    # Logic to convert amount to INR (if county code is not INR)
    if fc != 'INR':
        amount = amount/currency_rates[fc]

    # INR to To_country code
    amount = amount * currency_rates[tc]
    amount = round(amount, 2)

    # Set amount to Label in GUI
    to_amount.config(text=str(amount))


if __name__ == '__main__':

    # url and data extraction
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    data = requests.get(url).json()
    currency_rates = data['rates']

    # Building of GUI
    screen = tk.Tk()
    screen.title("Currency convertor")
    screen.geometry("500x300")
    screen.config(bg="#282828")

    # Introduction Label
    main_label = tk.Label(screen, text=" Welcome to Currency Convertor ")
    main_label.config(font=("Lato", 15, "bold"),
                      anchor="center", bg='#3500D3', fg='white')
    main_label.place(x=70, y=10)

    # from_amount input field and placing
    from_amount = tk.Entry(screen, justify=tk.CENTER)
    from_amount.place(x=58, y=180)

    # Converted amount label and it's placing
    to_amount = tk.Label(screen, anchor="center", bg='white',
                         fg='black', width=16, font=("Lato", 12))
    to_amount.place(x=300, y=180)

    # Variable declation for dropdown menu and set default values
    from_currency_code = tk.StringVar(screen)
    from_currency_code.set("INR")

    to_currency_code = tk.StringVar(screen)
    to_currency_code.set("INR")

    # dropdown menu for from_currency and it's placing
    from_currency_menu = ttk.Combobox(screen, textvariable=from_currency_code, values=list(
        currency_rates.keys()), font=("Lato", 12), state='readonly', width=14, justify=tk.CENTER)
    from_currency_menu.place(x=61, y=110)

    # dropdown menu for to_currency and it's placing
    to_currency_menu = ttk.Combobox(screen, textvariable=to_currency_code, values=list(
        currency_rates.keys()), font=("Lato", 12), state='readonly', width=14, justify=tk.CENTER)
    to_currency_menu.place(x=303, y=110)

    # Convert button and placing
    convert_btn = tk.Button(
        screen, text="Convert", fg='white', bg="#3500D3", command=calculate_conversion)
    convert_btn.place(x=230, y=240)

    screen.mainloop()
