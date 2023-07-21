import requests
from bs4 import BeautifulSoup


def scrape_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href and href.startswith('http'):  # Filter out non-HTTP links
            print(href)


# Example usage:
# Replace with the URL of the website you want to scrape
url = 'https://www.linkedin.com/feed/'
scrape_links(url)
