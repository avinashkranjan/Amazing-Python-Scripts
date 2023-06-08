import requests
from bs4 import BeautifulSoup

# Make a GET request to the BBC News website
url = "https://www.bbc.com/news"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the news headlines on the page
headline_tags = soup.find_all("h3", class_="gs-c-promo-heading__title")

# Extract and print the headlines
print("BBC News Headlines:")
for tag in headline_tags:
    headline = tag.get_text().strip()
    print("- " + headline)
