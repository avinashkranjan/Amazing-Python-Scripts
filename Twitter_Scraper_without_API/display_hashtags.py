import sqlite3
import os


def sql_connection():
    """
    Establishes a connection to the SQL file database
    :return connection object:
    """
    path = os.path.abspath('./Twitter_Scraper_without_API/TwitterDatabase.db')
    con = sqlite3.connect(path)
    return con


def sql_fetcher(con):
    """
    Fetches all the tweets with the given hashtag from our database
    :param con:
    :return:
    """
    hashtag = input("\nEnter hashtag to search: #")
    hashtag = '#' + hashtag
    count = 0
    cur = con.cursor()
    cur.execute('SELECT * FROM tweets')  # SQL search query
    rows = cur.fetchall()

    for r in rows:
        if hashtag in r:
            count += 1
            print(f'USERNAME: {r[1]}\nTWEET CONTENT: {r[2]}\nURL: {r[3]}\n')

    if count:
        print(f'{count} tweets fetched from database')
    else:
        print('No tweets available for this hashtag')


con = sql_connection()

while 1:
    sql_fetcher(con)

    ans = input('Press (y) to continue or any other key to exit: ').lower()
    if ans == 'y':
        continue
    else:
        print('Exiting..')
        break
