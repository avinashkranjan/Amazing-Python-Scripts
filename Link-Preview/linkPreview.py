import requests
import json
import os
from bs4 import BeautifulSoup

# to scrape title


def getTitle(soup):
    ogTitle = soup.find("meta", property="og:title")

    twitterTitle = soup.find("meta", attrs={"name": "twitter:title"})

    documentTitle = soup.find("title")
    h1Title = soup.find("h1")
    h2Title = soup.find("h2")
    pTitle = soup.find("p")

    res = ogTitle or twitterTitle or documentTitle or h1Title or h2Title or pTitle
    res = res.get_text() or res.get("content", None)

    if (len(res) > 60):
        res = res[0:60]
    return res.strip()

# to scrape page description


def getDesc(soup):
    ogDesc = soup.find("meta", property="og:description")

    twitterDesc = soup.find("meta", attrs={"name": "twitter:description"})

    metaDesc = soup.find("meta", attrs={"name": "description"})

    pDesc = soup.find("p")

    res = ogDesc or twitterDesc or metaDesc or pDesc
    res = res.get_text() or res.get("content", None)
    if (len(res) > 60):
        res = res[0:60]
    return res.strip()

# to scrape image link


def getImage(soup, url):
    ogImg = soup.find("meta", property="og:image")

    twitterImg = soup.find("meta", attrs={"name": "twitter:image"})

    metaImg = soup.find("link", attrs={"rel": "img_src"})

    img = soup.find("img")

    res = ogImg or twitterImg or metaImg or img
    res = res.get("content", None) or res.get_text() or res.get("src", None)

    if ((not res == None) and ((not "https://" in res) or (not "https://" in res))):
        res.replace(".", "")
        if (not res[0] == "/"):
            res = "/" + res
        res = url + res
    if (res == None):
        res = "Not available"

    return res


# start
print("\n======================")
print("- Link Preview -")
print("======================\n")

# get url from user
url = input("Enter URL to preview : ")

# parsing and checking the url
if (url == ""):
    url = 'www.girlscript.tech'
if ((not "http://" in url) or (not "https://" in url)):
    url = "https://" + url

# printing values

# first check in the DB
db = {}
# create file if it doesn't exist
if not os.path.exists('Link-Preview/db.json'):
    f = open('Link-Preview/db.json', 'w')
    f.write("{}")
    f.close()

with open('Link-Preview/db.json', 'r') as file:
    db = json.loads(file.read())
db["mj"] = {
    "name": "madhav"
}
print(db)

# parse file
with open('Link-Preview/db.json', 'w') as file:
    json.dump(db, file)

# if not in db get via request

# getting the html
# r = requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")

# print("\nTitle : ", getTitle(soup))
# print("Description : ", getDesc(soup))
# print("URL : ", url)
# print("Image link : ", getImage(soup, url))
# print("\n--END--\n")
