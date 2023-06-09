import requests
from bs4 import BeautifulSoup

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    
    return links

# Example usage:
url = 'https://www.dataschool.io/how-to-contribute-on-github/'  # Replace with the desired webpage URL
all_links = extract_links(url)
print(all_links)
