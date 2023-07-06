import io
import os
import sys
from contextlib import contextmanager

import newsapi
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

more_news = True
article_number = 0


def fetch_news() -> dict:
    query = input("What do you want to hear about? ")
    return newsapi.get_everything(q=query)


# To play audio text-to-speech during execution
def speak(text: str):
    with io.BytesIO() as f:
        gTTS(text=text, lang='en').write_to_fp(f)
        f.seek(0)
        audio = AudioSegment.from_file(f, format="mp3")
        play(audio)


if __name__ == '__main__':
    with open("api_key.txt", "r") as file:
        api_key = file.readline()
    newsapi = newsapi.NewsApiClient(api_key=api_key)

    headlines = fetch_news()
    while more_news:
        article_number += 1
        try:
            print()
            article = headlines["articles"][article_number]
            print(article["title"], "-", article["source"]["name"])
            speak(article["title"])
            print(article["description"])
            speak(article["description"])
            print("Continue reading on this URL:", article["source"]["name"])
        except IndexError:
            speak(
                "It looks as there are no more news on this topic. Why not search something else? "
            )
        except KeyboardInterrupt:
            break
        if article_number == 10:
            article_number = 0
            if input("Want to hear more news? [y/n] ") != "y":
                more_news = False
