import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from tkinter import font as tkFont
import time

# Function to generate URL based on choice
def get_URL():
    tag = search_box.get()
    if not tag:
        messagebox.showinfo("Alert", "Please Enter tag!")
        return
    url = 'https://stackoverflow.com/questions/tagged/{}?sort=MostVotes&edited=true'.format(tag)
    return url

def scrape_questions():
    for count in range(5):
        progress['value'] += 15
        window.update_idletasks()
        time.sleep(0.10)

    url = get_URL()
    if url:
        page = requests.get(url)
    else:
        clear_progress()
        return 

    # Start scraping resultant html data
    soup = BeautifulSoup(page.content, 'html.parser')
    questions = soup.find_all('div', {'class': 'question-summary'})
    if not questions:
        messagebox.showinfo("Invalid", "Invalid search tag")
        clear_progress()        
        return ""
    for question in questions:
        question_text = question.find('a', {'class': 'question-hyperlink'}).text.strip()
        question_link =  'https://stackoverflow.com{}'.format(question.find('a', {'class': 'question-hyperlink'})['href'])
        question_summary = question.find('div', {'class': 'excerpt'}).text.strip()
        votes = question.find('span', {'class': 'vote-count-post'}).text.strip()
        views = question.find('div', {'class': 'views'}).text.strip().split()[0]

    messagebox.showinfo("Success!", "Questions scrapped successfully!") 
    clear_progress()

def clear_progress():
    #set progress bar back to 0
        progress['value'] = 100
        window.update_idletasks()
        progress['value'] = 0
        window.update_idletasks()

# Creating tkinter window
window = tk.Tk()
window.title('Stack overflow question scraper')
window.geometry('1200x1000')
window.configure(bg='white')

style = ttk.Style()
style.theme_use('alt')
style.map('my.TButton', background=[('active','white')])
style.configure('my.TButton', font=('Helvetica', 16, 'bold'))
style.configure('my.TButton', background='white')
style.configure('my.TButton', foreground='orange')
style.configure('my.TFrame', background='white')

# label text for title
ttk.Label(window, text="Stack overflow question scraper",
          background='white', foreground="Orange",
          font=("Helvetica", 30, 'bold')).grid(row=0, column=1)

# label for combobox
ttk.Label(window, text="Enter tag (ex - python):", background = 'white',
          font=("Helvetica", 15)).grid(column=0,
                                       row=5, padx=10, pady=25)


# Button creation
scrape_btn = ttk.Button(window, text="Scrape questions!", style='my.TButton', command=scrape_questions)
scrape_btn.grid(row=5, column=2, pady=5, padx=15, ipadx=5)

display_btn = ttk.Button(window, text="Display from DB", style='my.TButton')
display_btn.grid(row=7, column=2, pady=5, padx=15, ipadx=5)

# Search Box
search_box = tk.Entry(window, font=("Helvetica 15"), bd = 2, width=60)
search_box.grid(row=5, column=1, pady=5, padx=15, ipadx=5)

frame = ttk.Frame(window, style='my.TFrame')
frame.place(relx=0.50, rely=0.18, relwidth=0.98, relheight=0.90, anchor="n")

# Progress bar
progress = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress.grid(row=5, column=5, pady=5, padx=15, ipadx=5)

# To display questions data
query_label = tk.Text(frame ,height="52" ,width="500", bg="alice blue")
query_label.grid(row=10,  columnspan=2)

window.mainloop()