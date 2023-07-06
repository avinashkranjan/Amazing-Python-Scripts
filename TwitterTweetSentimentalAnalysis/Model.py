from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

import tweepy


class model(object):

    def __init__(self, candidate_key, candidate_sec, access_key, access_sec):
        super().__init__()
        self.candidate_key = candidate_key
        self.candidate_sec = candidate_sec
        self.access_key = access_key
        self.access_sec = access_sec

    def get_authenticated_api(self):
        auth = tweepy.OAuthHandler(self.candidate_key, self.candidate_sec)
        auth.set_access_token(self.access_key, self.access_sec)
        api = tweepy.API(auth)
        return api

    def get_live_tweets_from_Twitter(self, text):

        api = self.get_authenticated_api()

        tweet_live = api.search(text, tweet_mode='extended')
        return tweet_live

    def analysis_live_tweet_data(self, text):

        tweet_live = self.get_live_tweets_from_Twitter(text)
        for tweet in tweet_live:
            tweet_is = tweet.text
            analysis = TextBlob(tweet_is)

    def detailed_analysis_tweet_data(self, text):

        # if polarity is in negative then the tweet is negative
        # if in positive then its a positive tweet
        # if polarity is greater then 0 and less then 5 then tweet is neutral

        tweet_live = self.get_live_tweets_from_Twitter(text)
        result = []
        for tweet in tweet_live:
            polarity = TextBlob(tweet.full_text).sentiment.polarity
            subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
            score = SentimentIntensityAnalyzer().polarity_scores(tweet.full_text)

            if polarity < 0 or subjectivity < 0 and score['neg'] > score['pos']:
                result.append([tweet.full_text, polarity, subjectivity, score, "negative"])
            elif polarity > 0 and subjectivity > 0 and score['neg'] < score['pos']:
                result.append([tweet.full_text, polarity, subjectivity, score, "positive"])
            else:
                result.append([tweet.full_text, polarity, subjectivity, score, "neutral"])

        return result
