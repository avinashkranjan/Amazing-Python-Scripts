import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

# Dictionary containing category and corresponding slug value
categories = {'Most Runs': 'most-runs',
              'Most Fours': 'most-fours', 'Most Sixes': 'most-sixes', 'Most Fifties': 'most-fifties',
              'Most Centuries': 'most-centuries', 'Highest Scores': 'highest-scores', 'Most Wickets': 'most-wickets',
              'Most Maidens': 'most-maidens', 'Most Dot Balls': 'most-dot-balls', 'Best Bowling Average': 'best-bowling-average',
              'Best Bowling Economy': 'best-bowling-economy', 'Best Bowling Strike Rate': 'best-bowling-strike-rate'}

# Function to generate request url based on user choice


def generate_url():
    category_choice = category.get()
    year_choice = year.get()
    if (year_choice == 'All time'):
        year_choice = 'all-time'
    category_slug = categories[category_choice]
    url = 'https://www.iplt20.com/stats/{}/{}'.format(
        year_choice, category_slug)
    return url

# Function to scrape results based on request url


def scrape_results():
    url = generate_url()
    page = requests.get(url)

    # Start scraping resultant html data
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(
        "table", {"class": "table table--scroll-on-tablet top-players"})
    rows = results.findChildren('tr')

    table_data = []
    row_values = []
    # Append player data into a list
    for row in rows:
        cells = row.findChildren(['th', 'td'])
        for cell in cells:
            value = cell.text.strip()
            value = " ".join(value.split())
            row_values.append(value)
        table_data.append(row_values)
        row_values = []

    # Formatting the data stored in the list
    p_records = ""
    for player in table_data[:51]:
        single_record = ""
        for cell in player:
            format_cell = "{:<20}"
            single_record += format_cell.format(cell[:20])
        single_record += "\n"
        p_records += single_record

    # Adding the formatted data into tkinter GUI
    query_label.config(state=tk.NORMAL)
    query_label.delete(1.0, "end")
    query_label.insert(1.0, p_records)
    query_label.config(state=tk.DISABLED)


# Creating tkinter window
window = tk.Tk()
window.title('IPL Statistics')
window.geometry('800x850')

# label text for title
ttk.Label(window, text="IPL Statistics",
          background='blue', foreground="white",
          font=("Helvetica", 20)).grid(row=0, column=1)

# label
ttk.Label(window, text="Select category and year :",
          font=("Helvetica", 15)).grid(column=0,
                                       row=5, padx=10, pady=25)

# Combobox creation
category = ttk.Combobox(
    window, width=27, state='readonly')
year = ttk.Combobox(
    window, width=27, state='readonly')

submit_btn = ttk.Button(window, text="Search", command=scrape_results)

# Adding combobox drop down list
category['values'] = ('Most Runs', 'Most Fours',
                      'Most Sixes', 'Most Fifties', 'Most Centuries', 'Highest Scores', 'Most Wickets', 'Most Maidens', 'Most Dot Balls', 'Best Bowling Average', 'Best Bowling Economy', 'Best Bowling Strike Rate')

year['values'] = ('All time', '2021', '2020', '2019',  '2018', '2017',  '2016',
                  '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008')

category.grid(column=1, row=5, padx=10)
category.current(0)

year.grid(column=2, row=5, padx=10)
year.current(0)

submit_btn.grid(row=5, column=3, pady=5, padx=15, ipadx=5)

frame = ttk.Frame(window)
frame.place(relx=0.50, rely=0.12, relwidth=0.98, relheight=0.90, anchor="n")

query_label = tk.Text(frame, height="52", width="500")
query_label.grid(row=7,  columnspan=2)

window.mainloop()
