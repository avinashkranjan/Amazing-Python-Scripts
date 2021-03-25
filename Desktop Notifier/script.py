import time
from plyer import notification
import requests
import json



news = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=51606761f68a4b20b4296e61814dbd1a')

data = json.loads(news.content)

for i in range(10):

    notification.notify(
       title = data['articles'][i]['title'],
       message= data['articles'][i]['description'] ,
       app_icon = data['articles'][i]['urlToImage'] ,
       # displaying time
       timeout=2 ,
       toast=False)

    # waiting time
    time.sleep(7)


