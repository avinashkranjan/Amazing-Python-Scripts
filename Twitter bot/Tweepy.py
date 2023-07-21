import tweepy

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Mention timeline tweets


def mention_timeline_tweets(username, count):
    try:
        # Get user timeline tweets
        tweets = api.user_timeline(screen_name=username, count=count)
        for tweet in tweets:
            # Mention the tweet author in a new tweet
            mention = f'@{tweet.user.screen_name} Hello! Just mentioning you.'
            api.update_status(mention, in_reply_to_status_id=tweet.id)
            print(
                f'Mentioned @{tweet.user.screen_name} in response to tweet: {tweet.text}')
    except tweepy.TweepError as e:
        print('Error:', str(e))


# Example usage
mention_timeline_tweets('openai', 5)
