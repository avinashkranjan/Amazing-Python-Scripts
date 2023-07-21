import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from tkinter import font as tkFont
import time
import sqlite3
from sqlite3 import Error

# Function to connect to the SQL Database


def sql_connection():
    try:
        con = sqlite3.connect('./Stack-overflow-scraper/stackoverflow.db')
        return con
    except Error:
        print(Error)

# Function to create table


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS questions(question_text text, question_summary text, question_link text,votes integer, views integer )")
    con.commit()


# Call functions to connect to database and create table
con = sql_connection()
sql_table(con)

# Function to insert into table


def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute(
        'INSERT INTO questions(question_text, question_summary, question_link, votes, views) VALUES(?, ?, ?, ?, ?)', entities)
    con.commit()

# Function to generate URL based on choice


def get_URL():
    tag = search_box.get()
    if not tag:
        messagebox.showinfo("Alert", "Please Enter tag!")
        return
    url = 'https://stackoverflow.com/questions/tagged/{}?sort=MostVotes&edited=true'.format(
        tag)
    return url


def number_questions():
    questions = int(questions_box.get())
    if type(questions) != int or questions > 15:
        return 15
    return questions


def scrape_questions():
    for count in range(5):
        progress['value'] += 15
        window.update_idletasks()
        time.sleep(0.10)

    question_count = number_questions()
    count = 0

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
        if count >= question_count:
            break
        question_text = question.find(
            'a', {'class': 'question-hyperlink'}).text.strip()
        question_summary = question.find(
            'div', {'class': 'excerpt'}).text.strip()
        question_summary = question_summary.replace('\n', ' ')
        question_link = 'https://stackoverflow.com{}'.format(
            question.find('a', {'class': 'question-hyperlink'})['href'])
        votes = question.find(
            'span', {'class': 'vote-count-post'}).text.strip()
        views = question.find(
            'div', {'class': 'views'}).text.strip().split()[0]
        entities = (question_text, question_summary,
                    question_link, votes, views)
        sql_insert(con, entities)
        count += 1

    messagebox.showinfo("Success!", "Questions scrapped successfully!")
    clear_progress()

# Function to fetch stackoverflow questions from DB


def sql_fetch(con):
    cursorObj = con.cursor()
    try:
        # SQL search query
        cursorObj.execute(
            'SELECT DISTINCT * FROM questions ORDER BY rowid DESC')
    except Error:
        print("Database empty... Fetch users using GUI")
        return

    rows = cursorObj.fetchall()
    display_text = ""

    # Show messagebox incase of empty DB
    if len(rows) == 0:
        messagebox.showinfo("Alert", "No users scraped yet!")
        return " "

    first_row = "{:^65}".format("Question") + "{:^65}".format("Summary") + "{:^40}".format(
        "Link") + "{:^15}".format("Votes") + "{:^15}".format("Views") + '\n'
    display_text += first_row

    # Format rows
    for row in rows:
        question_text = "{:<65}".format(
            row[0] if len(row[0]) < 60 else row[0][:56]+"...")
        question_summary = "{:<65}".format(
            row[1] if len(row[1]) < 60 else row[1][:56]+"...")
        question_link = "{:<40}".format(
            row[2] if len(row[2]) < 30 else row[2][:36]+"...")
        votes = "{:^15}".format(row[3])
        views = "{:^15}".format(row[4])
        display_text += (question_text + question_summary +
                         question_link + votes + views + '\n')

    return display_text


def show_results():
    display_text = sql_fetch(con)
    query_label.config(state=tk.NORMAL)
    query_label.delete(1.0, "end")
    query_label.insert(1.0, display_text)
    query_label.config(state=tk.DISABLED)


def clear_progress():
    # set progress bar back to 0
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
style.map('my.TButton', background=[('active', 'white')])
style.configure('my.TButton', font=('Helvetica', 16, 'bold'))
style.configure('my.TButton', background='white')
style.configure('my.TButton', foreground='orange')
style.configure('my.TFrame', background='white')

# label text for title
ttk.Label(window, text="Stack overflow question scraper",
          background='white', foreground="Orange",
          font=("Helvetica", 30, 'bold')).grid(row=0, column=1)

# label texts
ttk.Label(window, text="Enter tag (ex - python):", background='white',
          font=("Helvetica", 15)).grid(column=0,
                                       row=5, padx=10, pady=25)

ttk.Label(window, text="No of questions to scrape:", background='white',
          font=("Helvetica", 15)).grid(column=0,
                                       row=6, padx=10, pady=5)


# Button creation
scrape_btn = ttk.Button(window, text="Scrape questions!",
                        style='my.TButton', command=scrape_questions)
scrape_btn.grid(row=5, column=2, pady=5, padx=15, ipadx=5)

display_btn = ttk.Button(window, text="Display from DB",
                         style='my.TButton', command=show_results)
display_btn.grid(row=6, column=2, pady=5, padx=15, ipadx=5)

# Search Box
search_box = tk.Entry(window, font=("Helvetica 15"), bd=2, width=60)
search_box.grid(row=5, column=1, pady=5, padx=15, ipadx=5)

questions_box = tk.Entry(window, font=("Helvetica 15"), bd=2, width=60)
questions_box.grid(row=6, column=1, pady=5, padx=15, ipadx=5)

frame = ttk.Frame(window, style='my.TFrame')
frame.place(relx=0.50, rely=0.18, relwidth=0.98, relheight=0.90, anchor="n")

# Progress bar
progress = ttk.Progressbar(window, orient="horizontal",
                           length=200, mode="determinate")
progress.grid(row=5, column=5, pady=5, padx=15, ipadx=5)

# To display questions data
query_label = tk.Text(frame, height="52", width="500", bg="alice blue")
query_label.grid(row=10,  columnspan=2)

window.mainloop()
