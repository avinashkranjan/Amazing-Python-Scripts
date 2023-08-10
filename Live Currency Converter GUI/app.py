import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = "http://api.exchangeratesapi.io/v1/latest"
API_KEY = "111010136e803fdc2d600a9b204fa385"

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.configure(bg="black")


        self.amount_label = tk.Label(root, text="Amount:", fg="white", bg="black")
        self.amount_label.pack()



        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()



        self.from_label = tk.Label(root, text="From Currency:", fg="white", bg="black")
        self.from_label.pack()

        self.from_currency_entry = tk.Entry(root)
        self.from_currency_entry.pack()




        self.to_label = tk.Label(root, text="To Currency:", fg="white", bg="black")
        self.to_label.pack()

        self.to_currency_entry = tk.Entry(root)
        self.to_currency_entry.pack()



        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.pack()



    def get_rates(self):
        payload = {"access_key": API_KEY}

        response = requests.get(url=BASE_URL, params=payload)
        data = response.json()

        return data.get("rates")

    def get_currency(self, currency, rates):
        currency = currency.upper()
        if currency in rates.keys():

            return rates.get(currency)

        else:
            raise ValueError(f"{currency} is not a valid currency")



    def convert_currency(self):
        amount = float(self.amount_entry.get())

        from_currency = self.from_currency_entry.get()

        to_currency = self.to_currency_entry.get()

        rates = self.get_rates()

        from_rate = self.get_currency(from_currency, rates)
        to_rate = self.get_currency(to_currency, rates)


        conversion = round((to_rate / from_rate) * amount, 2)

        messagebox.showinfo("Conversion Result", f"{amount:.2f} ({from_currency}) is {conversion:.2f} ({to_currency})")

def main():
    app = tk.Tk()

    app.configure(bg="black")

    currency_converter = CurrencyConverterApp(app)


    app.mainloop()

if __name__ == "__main__":
    main()
