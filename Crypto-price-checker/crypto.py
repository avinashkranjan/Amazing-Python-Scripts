import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = input('Enter chrome driver path: ')


# Function to scrape stock data from generated URL
def scraper():
    url = 'https://www.cointracker.io/price'
    driver = webdriver.Chrome(driver_path)
    driver.get(url)

    # Wait for results to load
    time.sleep(5)
    html = driver.page_source

    # Start scraping resultant html data
    soup = BeautifulSoup(html, 'html.parser')

    # Find the crypto price table to scrape
    results = soup.find("table", {"class": 'table mx-auto'})
    rows = results.findChildren('tr')

    table_data = []
    row_values = []
    # Append individual cryptocurrency data into a list
    for row in rows:
        cells = row.findChildren(['th', 'td'])
        for cell in cells:
            value = cell.text.strip()
            value = " ".join(value.split())
            row_values.append(value)
        table_data.append(row_values)
        row_values = []

    # Formatting the cryptocurrency data stored in the list
    stocks_data = ""
    for stock in table_data:
        single_record = ""
        for cell in stock:
            format_cell = "{:<30}"
            single_record += format_cell.format(cell[:20])
        single_record += "\n"
        stocks_data += single_record

     # Adding the formatted data into tkinter GUI
    query_label.config(state=tk.NORMAL)
    query_label.delete(1.0, "end")
    query_label.insert(1.0, stocks_data)
    query_label.config(state=tk.DISABLED)
    driver.close()


# Creating tkinter window
window = tk.Tk()
window.title('Cryptocurrency Price Checker')
window.geometry('1200x1000')
window.configure(bg='white')

style = ttk.Style()
style.configure('my.TButton', font=('Helvetica', 16))
style.configure('my.TFrame', background='white')

# label text for title
ttk.Label(window, text="Cryptocurrency Price Checker",
          background='white', foreground="DodgerBlue2",
          font=("Helvetica", 30, 'bold')).grid(row=0, column=3, padx=300)

submit_btn = ttk.Button(window, text="Fetch Live Price!",
                        style='my.TButton', command=scraper)
submit_btn.grid(row=5, column=3, pady=5, padx=15, ipadx=5)

frame = ttk.Frame(window, style='my.TFrame')
frame.place(relx=0.50, rely=0.12, relwidth=0.98, relheight=0.90, anchor="n")

# To display stock data
query_label = tk.Text(frame, height="52", width="500", bg="lightskyblue1")
query_label.grid(row=7,  columnspan=2)

window.mainloop()
