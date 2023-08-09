import tweepy
import requests

# Function to get tweets from Twitter API


def get_tweets(api_key, api_secret_key, access_token, access_token_secret, username):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = []
    try:
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items(10):
            tweets.append(tweet.full_text)
    except tweepy.TweepError as e:
        print(f"Error: {e}")

    return tweets

# Function to get weather data from OpenWeatherMap API


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print(f"Error: {data['message']}")
        return None

# Function to get stock data from Alpha Vantage API


def get_stock_data(api_key, symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if "Time Series (Daily)" in data:
        return data["Time Series (Daily)"]
    else:
        print(f"Error: {data['Note']}")
        return None


if __name__ == "__main__":
    # Replace with your Twitter API credentials
    twitter_api_key = "YOUR_TWITTER_API_KEY"
    twitter_api_secret_key = "YOUR_TWITTER_API_SECRET_KEY"
    twitter_access_token = "YOUR_TWITTER_ACCESS_TOKEN"
    twitter_access_token_secret = "YOUR_TWITTER_ACCESS_TOKEN_SECRET"
    twitter_username = "target_username"

    # Replace with your OpenWeatherMap API key
    weather_api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    city_name = "New York"

    # Replace with your Alpha Vantage API key
    alpha_vantage_api_key = "YOUR_ALPHA_VANTAGE_API_KEY"
    stock_symbol = "AAPL"

    # Retrieve data from APIs
    tweets = get_tweets(twitter_api_key, twitter_api_secret_key,
                        twitter_access_token, twitter_access_token_secret, twitter_username)
    weather_data = get_weather(weather_api_key, city_name)
    stock_data = get_stock_data(alpha_vantage_api_key, stock_symbol)

    # Print the results
    print("Twitter Tweets:")
    for idx, tweet in enumerate(tweets, start=1):
        print(f"{idx}. {tweet}")

    print("\nWeather Data:")
    print(weather_data)

    print("\nStock Data:")
    print(stock_data)
