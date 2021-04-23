# this is a local Credential Helper
import tweepy
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

import TwitterTweetSentimentalAnalysis.CredentialHelper as twitterCredential


# Tweepy is a lib that can be used to connect to twitter api
# helps us to make sentimental analysis on the given data on bases of text


class model(object):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_authenticated_api():
        auth = tweepy.OAuthHandler(twitterCredential.candidate_key, twitterCredential.candidate_sec)
        auth.set_access_token(twitterCredential.access_key, twitterCredential.access_sec)
        api = tweepy.API(auth)
        return api

    def get_user_name(self):
        api = self.get_authenticated_api()
        user = api.me()
        return user.name

    def get_live_tweets_from_Twitter(self, text):
        api = self.get_authenticated_api()
        # getting the tweets form twitter using The Twitter aap and tweepy
        # Demo of getting text from twitter

        tweet_live = api.search(text, tweet_mode='extended')
        # for tweet in tweet_live:
        #     tweet_is = tweet.text
        #     for demo added a print statement
        #     print(tweet_is)
        return tweet_live

    def analysis_live_tweet_data(self, text):
        # Making prediction on the tweet provided by twitter related to this topic

        # lets choose a random topic i choose this as it was in news alot

        # we were abe to get the
        tweet_live = self.get_live_tweets_from_Twitter(text)
        for tweet in tweet_live:
            tweet_is = tweet.text
            analysis = TextBlob(tweet_is)
            # print(analysis.sentiment)

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
            # print("polarity =", polarity)
            # print('*' * 20)
            # print("subjectivity =", subjectivity)
            # print('*' * 20)
            # print('*' * 30)

            if polarity < 0 or subjectivity < 0 and score['neg'] > score['pos']:
                result.append([tweet.full_text, polarity, subjectivity, score, "negative"])
            elif polarity > 0 and subjectivity > 0 and score['neg'] < score['pos']:
                result.append([tweet.full_text, polarity, subjectivity, score, "positive"])
            else:
                result.append([tweet.full_text, polarity, subjectivity, score, "neutral"])

        return result


if __name__ == "__main__":
    ob = model()
    text = "black lives matter"
    ob.get_live_tweets_from_Twitter(text)
    res = ob.detailed_analysis_tweet_data(text)
    for i in res:
        print(i)
