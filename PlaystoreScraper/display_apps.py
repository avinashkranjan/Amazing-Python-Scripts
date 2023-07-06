import sqlite3
import os


def sql_connection():
    """
    Establishes a connection to the SQL file database
    :return connection object:
    """
    path = os.path.abspath('PlaystoreDatabase.db')
    con = sqlite3.connect(path)
    return con


def sql_fetcher(con):
    """
    Fetches all the  with the given query from our database
    :param con:
    :return:
    """
    query = input("\nEnter query to search: r/")
    count = 0
    cur = con.cursor()
    cur.execute('SELECT * FROM apps')  # SQL search query
    rows = cur.fetchall()

    for r in rows:
        if query in r:
            count += 1
            print(f'\nURL: {r[1]}\nNAME: {r[2]}\nRATING: {r[3]}\n'
                  f'REVIEWS: {r[4]}\nINSTALLS: {r[5]}\nVERSION: {r[6]}'
                  f'\nLASTUPDATE: {r[7]}\nCOMPANY: {r[8]}\nCONTACT: {r[9]}')

    if count:
        print(f'{count} posts fetched from database\n')
    else:
        print('\nNo posts stored for this query\n')


con = sql_connection()

while 1:
    sql_fetcher(con)

    ans = input('\nPress (y) to continue or any other key to exit: ').lower()
    if ans == 'y':
        continue
    else:
        print('\nExiting..\n')
        break

