import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import time

# Dictionary for date values
dates = {'Today':'daily','This week':'weekly','This month':'monthly'}

# Function to generate URL based on choice
def get_URL():
    url_lang = language.get()
    url_date = dates[date.get()]
    url = 'https://github.com/trending/developers/{}?since={}'.format(url_lang.lower(), url_date)
    return url

def scrape_users():
    url = get_URL()
    page = requests.get(url)

    # Start scraping resultant html data
    soup = BeautifulSoup(page.content, 'html.parser')
    users = soup.find_all('article', {'class': 'Box-row d-flex'})
    for user in users:
        name = user.find('h1', {'class': 'h3 lh-condensed'}).text.strip()
        profile_link =  'https://github.com{}'.format(user.find('h1', {'class': 'h3 lh-condensed'}).find('a')['href'])
        repo = user.find('h1', {'class': 'h4 lh-condensed'}).text.strip()
        repo_link = 'https://github.com{}'.format(user.find('h1', {'class': 'h4 lh-condensed'}).find('a')['href'])
        print(repo_link)

# Creating tkinter window
window = tk.Tk()
window.title('Github Trending User Fetcher')
window.geometry('1200x1000')
window.configure(bg='white')

style = ttk.Style()
style.configure('my.TButton', font=('Helvetica', 16))
style.configure('my.TFrame', background='white')

# label text for title
ttk.Label(window, text="Trending Github Users",
          background='white', foreground="Blue",
          font=("Helvetica", 30, 'bold')).grid(row=0, column=1)

# label for combobox
ttk.Label(window, text="Select Language:", background = 'white',
          font=("Helvetica", 15)).grid(column=0,
                                       row=5, padx=10, pady=25)
ttk.Label(window, text="Select Date range:", background = 'white',
          font=("Helvetica", 15)).grid(column=2,
                                       row=5, padx=10, pady=25)

# Combobox creation
language = ttk.Combobox(
    window, width=30, state='readonly', font="Helvetica 15")
date = ttk.Combobox(
    window, width=20, state='readonly',font="Helvetica 15")

# Button creation
submit_btn = ttk.Button(window, text="Scrape Users!", style='my.TButton', command=scrape_users)

display_btn = ttk.Button(window, text="Display from DB", style='my.TButton')

# Adding combobox drop down list
language['values'] = ('C++', 'HTML', 'Java', 'Javascript', 'PHP', 'Python', 'Ruby', 'C#', 'C', 'Dockerfile', 'JSON', 'Julia', 'Dart'
                        'Shell','Solidity','YAML')

date['values'] = ('Today','This week','This month')

language.grid(column=1, row=5, padx=10)
language.current(0)

date.grid(column=3, row=5, padx=10)
date.current(0)

submit_btn.grid(row=5, column=4, pady=5, padx=15, ipadx=5)
display_btn.grid(row=7, column=2, pady=5, padx=15, ipadx=5)

frame = ttk.Frame(window, style='my.TFrame')
frame.place(relx=0.50, rely=0.18, relwidth=0.98, relheight=0.90, anchor="n")

# To display stock data
query_label = tk.Text(frame ,height="52" ,width="500", bg="alice blue")
query_label.grid(row=10,  columnspan=2)

window.mainloop()
