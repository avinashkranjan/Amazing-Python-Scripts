import requests
from bs4 import BeautifulSoup
import re

# Taking the URL input and validating using Regex
URL = input("Enter a valid Wikipedia URL:\n")
urlRegex = re.compile(r"^https\:\/\/([\w\.]+)wikipedia.org\/wiki\/([\w]+\_?)+")
mo = urlRegex.search(URL)
if mo == None:
    print("Wrong URL entered. Make sure to enter a valid Wikipedia URL. Make sure to add https:// before the URL if you forgot.")
    exit()

# Requesting the HTML and making the BeautifulSoup object
req = requests.get(mo.group())
soup = BeautifulSoup(req.text, "lxml")

# Validating if the site has content
if soup.find("p").text.strip() == "Other reasons this message may be displayed:":
    print("This Wikipedia site does not exists.\n")
    exit()

# Retriving and printing the page title
page_title = soup.find("h1", class_="firstHeading").text
print(f"\n---{page_title}---\n")

# Making the text file to save the text data
f = open(f"{page_title}.txt", "w", encoding="utf-8")
f.write(f"//{mo.group()}\n---{page_title}---\n\n")

# Topics to avoid
exclude = ["See also", "References", "Sources",
           "Further reading", "External links"]

# Scraping the site for headings and paragraphs
for info in soup.descendants:
    if info.name == "span":
        try:
            if info["class"][0] == "mw-headline":
                headline = info.get_text()
                if headline not in exclude:
                    print(f"{headline}:\n")  # Printing the heading
                    f.write(f"\n{headline}:\n\n")
        except KeyError:  # try except block to handle BS KeyError
            pass
    elif info.name == "p":
        para = info.get_text()
        print(f"{para}")  # Printing the paragraph
        f.write(f"{para}")
f.close()  # Closing the file
