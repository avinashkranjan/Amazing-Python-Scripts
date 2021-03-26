import time
from plyer import notification
import requests
import json

country_code = input("Enter the country code for the news: ")
api_key = input("Enter the api key: ")

news = requests.get(f'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}')

data = json.loads(news.content)

for i in range(10):

    notification.notify(
       title = data['articles'][i]['title'],
       message= data['articles'][i]['description'] ,
       # displaying time
       timeout=2 ,
       toast=False)

    # waiting time
    time.sleep(7)


