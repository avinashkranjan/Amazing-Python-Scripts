# Youtube Trending Feed Reader
# Written by XZANATOL
from optparse import OptionParser
from pymongo import MongoClient
import pandas as pd
import sys

# Help menu
usage = """
<Script> [Options]

[Options]
    -h, --help    Shows this help message and exit
    -c, --csv     Reads data from "Youtube.csv" file
    -m, --mongo   Reads data from MongoDB
"""

# Load args
parser = OptionParser()
parser.add_option("-c", "--csv", action="store_true", dest="csv",
                  help="Saves extracted contents to a CSV file.")
parser.add_option("-m", "--mongo", action="store_true",
                  dest="mongo", help="Saves extracted contents to a MongoDB.")


def read_mongo():
    # Connect to service
    client = MongoClient("127.0.0.1")
    # Create an object
    db = client.Youtube.trending
    return db.find()  # Return all values


def read_csv():
    # read databse
    df = pd.read_csv("Youtube.csv")
    data = []
    for index, row in df.iterrows():
        data.append(row)  # Append each dictionary to the list
    return data  # Return all values


def display(data):
    i = 0
    for card in data:
        # For every 10 cards print section
        if i % 10 == 0:
            c = input("Show Section? [y/n] > ")
            if c.lower() == "y":
                print("***********************************")
                print(f"""{card["section"]} section""")
                print("***********************************")
            else:
                sys.exit()  # If had enough of reading
        i += 1  # Increament
        print("Title:", card["title"])
        print("Link:",  card["link"])
        print("Channel:", card["channel"])
        print("Views:", card["views"])
        print("Time:", card["date"])
        print("==============================================")


if __name__ == "__main__":
    (options, args) = parser.parse_args()

    # Flags
    csv = options.csv
    mongo = options.mongo
    # Validate flags
    if not (bool(csv) ^ bool(mongo)):  # XNOR Gate
        print(usage)
        sys.exit()

    if mongo:
        data = read_mongo()
    else:
        data = read_csv()
    display(data)
