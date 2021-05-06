import snscrape.modules.twitter as sntweets
import sqlite3


def sql_connection():
    """
    Establishes a connection to the SQL file database
    :return connection object:
    """
    con = sqlite3.connect('./Twitter_Scraper_without_API/TwitterDatabase.db')
    return con


def sql_table(con):
    """
    Creates a table in the database (if it does not exist already)
    to store the tweet info
    :param con:
    :return:
    """
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tweets(HASHTAG text, USERNAME text,"
                " CONTENT text, URL text)")
    con.commit()


def sql_insert_table(con, entities):
    """
    Inserts the desired data into the table to store tweet info
    :param con:
    :param entities:
    :return:
    """
    cur = con.cursor()
    cur.execute('INSERT INTO tweets(HASHTAG, USERNAME, CONTENT, '
                'URL) VALUES(?, ?, ?, ?)', entities)
    con.commit()


con = sql_connection()
sql_table(con)

while 1:
    tag = input('\n\nEnter a hashtag: #')
    max_count = int(input('Enter maximum number of tweets to be listed: '))

    count = 0
    # snscrape uses the given string of hashtag to find the desired amount of
    # tweets and associated info
    for i in sntweets.TwitterSearchScraper('#' + tag).get_items():
        count += 1
        entities = ('#'+tag, i.username, i.content, i.url)
        sql_insert_table(con, entities)

        if count == max_count:
            break

    print('Done!')

    ans = input('Press (y) to continue or any other key to exit: ').lower()
    if ans == 'y':
        continue
    else:
        print('Exiting..')
        break

