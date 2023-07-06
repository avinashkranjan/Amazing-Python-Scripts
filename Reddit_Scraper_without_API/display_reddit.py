import sqlite3
import os


def sql_connection():
    """
    Establishes a connection to the SQL file database
    :return connection object:
    """
    path = os.path.abspath('SubredditDatabase.db')
    con = sqlite3.connect(path)
    return con


def sql_fetcher(con):
    """
    Fetches all the tweets with the given hashtag from our database
    :param con:
    :return:
    """
    subreddit = input("\nEnter subreddit to search: r/")
    count = 0
    cur = con.cursor()
    cur.execute('SELECT * FROM posts')  # SQL search query
    rows = cur.fetchall()

    for r in rows:
        if subreddit in r:
            count += 1
            print(f'\nTAG: {r[1]}\nPOST TITLE: {r[2]}\nAUTHOR: {r[3]}\n'
                  f'TIME STAMP: {r[4]}\nUPVOTES: {r[5]}\nCOMMENTS: {r[6]}'
                  f'\nURL: {r[7]}\n')

    if count:
        print(f'{count} posts fetched from database\n')
    else:
        print('\nNo posts stored for this subreddit\n')


con = sql_connection()

while 1:
    sql_fetcher(con)

    ans = input('\nPress (y) to continue or any other key to exit: ').lower()
    if ans == 'y':
        continue
    else:
        print('\nExiting..\n')
        break

