# Youtube Trending Feed Scrapper
# Written by XZANATOL
from optparse import OptionParser
from selenium import webdriver
import pandas as pd
import mongoengine
import pymongo
import time
import sys

# Help menu
usage = """
<Script> [Options]

[Options]
    -h, --help    Shows this help message and exit.
    -c, --csv     Saves extracted contents to a CSV file.
    -m, --mongo   Saves extracted contents to a MongoDB.
"""

# Load args
parser = OptionParser()
parser.add_option("-c", "--csv", action="store_true", dest="csv",
                  help="Saves extracted contents to a CSV file.")
parser.add_option("-m", "--mongo", action="store_true",
                  dest="mongo", help="Saves extracted contents to a MongoDB.")

# Defined DataFrame to avoid check errors
df = pd.DataFrame()

# MongoDB Collection (Table) Template


class Trending(mongoengine.Document):
    section = mongoengine.StringField(required=True)
    title = mongoengine.StringField(required=True)
    channel = mongoengine.StringField(required=True)
    link = mongoengine.StringField(required=True)
    views = mongoengine.StringField(required=True)
    date = mongoengine.StringField(required=True)

    meta = {"indexes": ["section"]}


def load_driver():
    """Load Chrome webdriver."""
    driver = webdriver.Chrome("chromedriver.exe")
    return driver


def page_scrap(driver):
    """Scrap YouTube trending feed."""
    # pages to be scrapped: Now, Music, Gaming, Movies
    pages = ["https://www.youtube.com/feed/trending",
             "https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D",
             "https://www.youtube.com/feed/trending?bp=4gIcGhpnYW1pbmdfY29ycHVzX21vc3RfcG9wdWxhcg%3D%3D",
             "https://www.youtube.com/feed/trending?bp=4gIKGgh0cmFpbGVycw%3D%3D"]
    sections = ["Now", "Music", "Gaming", "Movies"]

    for num in range(4):
        driver.get(pages[num])
        time.sleep(3)  # Make sure that all the page is loaded
        # Extract first 10 contents
        cards = driver.find_elements_by_tag_name("ytd-video-renderer")[:10]
        links = driver.find_elements_by_id("video-title")[:10]
        meta_data = driver.find_elements_by_tag_name(
            "ytd-video-meta-block")[:10]
        for i in range(10):
            # Splitted meta data that will be saved
            meta_splitted = meta_data[i].text.split("\n")
            # Sometimes this character is extracted for unknown reasons
            try:
                meta_splitted.remove("•")
            except:
                pass
            section = sections[num]     # Scrapped from which section?
            link = links[i].get_attribute("href")  # Video Link
            title = links[i].text     # Video title
            channel = meta_splitted[0]  # Channel name
            views = meta_splitted[1]  # Video Views
            date = meta_splitted[2]  # Release date

            """Arguments validation is better than making a scrapping algorithm for each"""
            if mongo:
                save_to_db(section, title, channel, link, views, date)
            if csv:
                append_to_df(section, title, channel, link, views, date)

        print(f"[+]Finished scraping '{sections[num]}' section!")

    # last validation for csv
    if csv:
        save_to_csv()


def save_to_db(section, title, channel, link, views, date):
    """Saves a record to database."""
    # Create object
    record = Trending(
        section=section,
        title=title,
        channel=channel,
        link=link,
        views=views,
        date=date)
    # Save record
    record.save()


def append_to_df(section, title, channel, link, views, date):
    """Appends a record to dataframe."""
    global df
    df = df.append({"section": section,
                    "title": title,
                    "channel": channel,
                    "link": link,
                    "views": views,
                    "date": date, }, ignore_index=True)


def save_to_csv():
    """exports dataframe to a CSV file."""
    global df
    df.to_csv("Youtube.csv", index=False, columns=["section", "title",
                                                   "channel", "link",
                                                   "views", "date"])
    # Function end (eye friendly comment to seperate the function end line)


if __name__ == "__main__":
    (options, args) = parser.parse_args()

    # Flags
    csv = options.csv
    mongo = options.mongo
    # Validate flags
    if not (bool(csv) or bool(mongo)):
        print(usage)
        sys.exit()

    if mongo:
        mongoengine.connect("Youtube")

    driver = load_driver()  # load driver
    page_scrap(driver)  # start scrapping
    print("[+]Done !")
    # End session
    driver.quit()
    sys.exit()
