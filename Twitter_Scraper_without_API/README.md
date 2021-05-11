# Tweet hashtag based scraper without Twitter API

- Here, we make use of snscrape to scrape tweets associated with a particular hashtag. Snscrape is a python library that scrapes twitter without the use of API keys.

- We have 2 scripts associated with this project one to fetch tweets with snscrape and store it in the database (we use SQLite3), and the other script displays the  tweets from the database.

- Using snscrape, we are storing the hashtag, the tweet content, user id, as well as the URL of the tweets in the database.

## Requirements

Packages associated can be installed as:

```sh
  $ pip install -r requirements.txt
```

## Running the script

For running the script which fetches tweets and other info associated with the hashtag and storing in the database:
```sh
  $ python fetch_hashtags.py
```

For running the script to display the tweet info stored in the database:
```sh
  $ python display_hashtags.py
```

## Working

```fetch_hashtags.py``` will work as follows:

![image](https://imgur.com/8YFK4OV.png)

```display_hashtags.py``` will work as follows:

![image](https://i.imgur.com/1uNEEMw.png)

## Author

[Rohini Rao](https://github.com/RohiniRG)
