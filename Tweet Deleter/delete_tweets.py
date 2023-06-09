import tweepy
import json

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Path to the extracted Twitter Archive JSON file
archive_path = "PATH_TO_YOUR_TWITTER_ARCHIVE/data/js/tweets/"

# Delete all tweets
with open(archive_path + "tweet.js", "r") as file:
    tweets = json.load(file)

    for tweet in tweets:
        tweet_id = tweet["tweet"]["id_str"]
        try:
            api.destroy_status(tweet_id)
            print(f"Deleted tweet with ID: {tweet_id}")
        except tweepy.TweepError as e:
            print(f"Failed to delete tweet with ID: {tweet_id}\nError: {e}")
