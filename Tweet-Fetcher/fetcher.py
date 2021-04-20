import tweepy
import sqlite3
from sqlite3 import Error

# Set Twitter API KEYS
consumer_key = '<Your key>'
consumer_secret = '<Your key>'
access_key = '<Your key>'
access_secret = '<Your key>'

# Initialize Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to connect to the SQL Database


def sql_connection():
    try:
        con = sqlite3.connect('tweetsDatabase.db')
        return con
    except Error:
        print(Error)

# Function to create table


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS tweets(hashtag text, tweet text)")
    con.commit()


# Call functions to connect to database and create table
con = sql_connection()
sql_table(con)

# Function to insert into table


def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute(
        'INSERT INTO tweets(hashtag, tweet) VALUES(?, ?)', entities)
    con.commit()


# Take input for hashtag to search and number of tweets to fetch
hashTag = input("\nEnter hashtag to search: ")
numberOfTweets = int(input("How many tweets do you want to fetch? "))
search_words = "#"+hashTag
new_search = search_words + " -filter:retweets"

# Call twitter API and pass above parameters
try:
    for tweet in tweepy.Cursor(api.search, q=new_search, count=5, lang="en", since_id=0).items(numberOfTweets):
        entities = (hashTag, tweet.text)
        # Insert tweet into database
        sql_insert(con, entities)
    print("Saved successfully in Database")
except Error:
    print(Error)
