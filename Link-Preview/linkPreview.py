import requests
import json
import os
import time
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
    if (res == None or len(res.split()) == 0):
        res = "Not available"
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
    if (res == None or len(res.split()) == 0):
        res = "Not available"
    return res.strip()

# to scrape image link


def getImage(soup, url):
    ogImg = soup.find("meta", property="og:image")

    twitterImg = soup.find("meta", attrs={"name": "twitter:image"})

    metaImg = soup.find("link", attrs={"rel": "img_src"})

    img = soup.find("img")

    res = ogImg or twitterImg or metaImg or img
    res = res.get("content", None) or res.get_text() or res.get("src", None)

    count = 0
    for i in range(0, len(res)):
        if (res[i] == "." or res[i] == "/"):
            count += 1
        else:
            break
    res = res[count::]
    if ((not res == None) and ((not "https://" in res) or (not "https://" in res))):
        res = url + "/" + res
    if (res == None or len(res.split()) == 0):
        res = "Not available"

    return res

# print dictionary


def printData(data):
    for item in data.items():
        print(f'{item[0].capitalize()}: {item[1]}')


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
    f = open('Link-Preview/db.json', "w")
    f.write("{}")
    f.close()

# read db
with open('Link-Preview/db.json', 'r+') as file:
    data = file.read()
    if (len(data) == 0):
        data = "{}"
        file.write(data)
    db = json.loads(data)

# check if it exists
if (url in db and db[url]["time"] < round(time.time())):
    printData(db[url])
else:
    # if not in db get via request

    # getting the html
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    sevenDaysInSec = 7*24*60*60
    # printing data
    newData = {
        "title": getTitle(soup),
        "description": getDesc(soup),
        "url": url,
        "image": getImage(soup, url),
        "time": round(time.time() * 1000) + sevenDaysInSec
    }
    printData(newData)
    # parse file
    db[url] = newData
    with open('Link-Preview/db.json', 'w') as file:
        json.dump(db, file)

print("\n--END--\n")
