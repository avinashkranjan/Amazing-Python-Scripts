import sqlite3
from sqlite3 import Error

# Function to connect to the SQL Database


def sql_connection():
    try:
        con = sqlite3.connect('./Udemy Scraper/udemyDatabase.db')
        return con
    except Error:
        print(Error)


con = sql_connection()

# Function to Fetch courses from database


def sql_fetch(con):
    cursorObj = con.cursor()
    try:
        cursorObj.execute('SELECT * FROM courses')  # SQL search query
    except Error:
        print("Database empty... Fetch courses using fetcher script")
        return

    rows = cursorObj.fetchall()

    # Print table header
    print("{:^30}".format("Title"), "{:^30}".format("Description"), "{:^20}".format("Instructor"),
          "{:<15}".format("Current Price"), "{:<18}".format(
              "Original Price"), "{:^10}".format("Rating"),
          "{:^10}".format("Hours"), "{:^10}".format("Lectures"))

    # Print all rows
    for row in rows:
        # Format individual data items for printing in a table like manner
        title = "{:<30}".format(row[0] if len(
            row[0]) < 30 else row[0][:26]+"...")
        description = "{:<30}".format(
            row[1] if len(row[1]) < 30 else row[1][:26]+"...")
        instructor = "{:<20}".format(row[2] if len(
            row[2]) < 30 else row[2][:16]+"...")
        current_price = "{:^15}".format(row[3])
        original_price = "{:^18}".format(row[4])
        rating = "{:^10}".format(row[5])
        hours = "{:^10}".format(row[6])
        lectures = "{:^10}".format(row[7])
        print(title, description, instructor, current_price,
              original_price, rating, hours, lectures)


sql_fetch(con)
