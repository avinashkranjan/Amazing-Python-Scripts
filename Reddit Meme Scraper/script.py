import praw
import PySimpleGUI as pg
import urllib
import pandas
import datetime as dt
import os

reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     user_agent = '')

subreddit = reddit.subreddit('sbname+sbname+sbname')
posts = subreddit.hot(limit=10)

# Empty lists to hold data

image_urls = []
image_titles = []
image_scores = []
image_timestamps = []
image_ids = []
image_extensions = ['.jpg', '.jpeg', '.png']

# This iterates through posts and collects their data into lists

for post in posts:
    image_urls.append(post.url.encode('utf-8'))
    image_titles.append(post.title.encode('utf-8'))
    image_scores.append(post.score)
    image_timestamps.append(dt.datetime.fromtimestamp(post.created))
    image_ids.append(post.id)

# This iterates through URLs, checks if it has the specified image extension and downloads the image

for index, url in enumerate(image_urls):
    images_path = os.getcwd()
    _, ext = os.path.splitext(url)
    if ext in image_extensions:
        try:
            print('Downloading ', image_urls[index], ' at', images_path + image_titles[index] + ext)
            urllib.urlretrieve(image_urls[index], images_path + image_titles[index] + ext)
        except:
            print('Something went wrong while downloading ', image_urls[index])