import sqlite3
from sqlite3 import Error

# Function to connect to the SQL Database


def sql_connection():
    try:
        con = sqlite3.connect('tweetsDatabase.db')
        return con
    except Error:
        print(Error)


con = sql_connection()

# Function to Fetch tweets from database


def sql_fetch(con):
    searchHashtag = input("\nEnter hashtag whose tweets you want to display :")
    isEmptySearch = True
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM tweets')  # SQL search query
    rows = cursorObj.fetchall()

    print("\n")

    for row in rows:
        # Check if row has searched HashTag
        if (searchHashtag in row):
            print(row[1]+'\n')
            isEmptySearch = False

    if (isEmptySearch):
        print("\nNo tweets with #"+searchHashtag+" fetched into database \n")


sql_fetch(con)
