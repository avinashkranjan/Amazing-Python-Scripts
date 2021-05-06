import praw
import PySimpleGUI as sg
import wget
import pandas as pd
import datetime as dt
import json
import os

destination_folder = sg.popup_get_folder(
    'Choose where to download files:\n\n'
    'NOTE: A folder to store the files will be created within the directory!',
    default_path='',
    title='Choose destination')
folder_lst = [destination_folder]
if folder_lst[0] is None:
    sg.Popup('Destination not specified!\nProgram terminated!',
             title='ERROR: No destination!',
             custom_text='Close',
             button_type=0)
    raise SystemExit()


class RedditCred:
    def __init__(self):
        self.text_file = 'reddit_tokens.json'


# Functions made to read the reddit app id and secret from file


    def read_id(self):
        file = self.text_file
        with open(file, 'r') as f:
            data = json.load(f)
            keys = data.keys()
            return str(*keys)

    def read_secret(self):
        file = self.text_file
        with open(file, 'r') as f:
            data = json.load(f)
            value = data.values()
            return str(*value)


red_cred = RedditCred()
u_agent = 'Script that downloads memes from various subreddits'

reddit = praw.Reddit(client_id=red_cred.read_id(),
                     client_secret=red_cred.read_secret(),
                     user_agent=u_agent)

subreddit = reddit.subreddit(
    'deepfriedmemes+surrealmemes+nukedmemes+bigbangedmemes+wackytictacs+bonehurtingjuice'
)
posts = subreddit.hot(limit=25)

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

# This creates a GUI window with a progress bar to keep track of the download

layout = [[sg.Text(f"Downloading files...", key='textkey')],
          [sg.ProgressBar(25, orientation='h', size=(20, 20), key='progbar')],
          [sg.Cancel()]]

window = sg.Window('Download in Progress', layout)

# This iterates through URLs, checks if it has the specified image extension and downloads the image

for index, url in enumerate(image_urls):
    path = str(folder_lst[0])
    file_ending = str(url)[2:-1]
    event, values = window.read(timeout=0)
    _, extension = os.path.splitext(file_ending)
    if extension in image_extensions:
        try:
            if os.path.exists(path + '/' + 'Downloaded Images'):
                pass
            else:
                os.mkdir(path + '/' + 'Downloaded Images')
            if event == 'Cancel' or event == sg.WIN_CLOSED:
                break

            destination = str(folder_lst[0]) + '/' + 'Downloaded Images' + '/'
            window['progbar'].update_bar(index + 1)
            print(
                f"Downloading '{str(image_titles[index])[2:-1]}' to '{path}' from '{str(image_urls[index])[2:-1]}'"
            )
            download = wget.download(str(image_urls[index])[2:-1],
                                     out=destination)
        except:
            print(
                f"Something went wrong while downloading '{str(image_urls[index])[2:-1]}'\n"
            )
else:
    print("\nDownload complete!")
    window.close()
    sg.Popup(f"Files downloaded into:\n\n'{path}/Downloaded Images'",
             title='Download complete!')

# Optional saving of collected data to .csv file

dataframe = pd.DataFrame({
    'Title': image_titles,
    'Score': image_scores,
    'URL': image_urls,
    'Timestamp': image_timestamps,
    'ID': image_ids
})
csv = dataframe.to_csv('./images.csv', index=True, header=True)
