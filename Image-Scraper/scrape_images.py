# Scrape all HTML <img> tags from a provided URL.

from bs4 import BeautifulSoup
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python scrape_images.py {url}")

response = requests.get(
    sys.argv[1],
    headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
)

html_data = BeautifulSoup(response.text, 'html.parser')
images = html_data.find_all('img', src=True)

for image in images:
    print(image)
