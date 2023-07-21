import requests
from bs4 import BeautifulSoup
import iocextract

r = requests.get('your_link')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
items_of_href = []
# find all the anchor tags with "href"
for item in soup.find_all('a'):
    items_of_href.append(item.get('href'))

items = list(iocextract.extract_urls((str(items_of_href))))
refanged = list(iocextract.extract_urls((str(items_of_href)), refang=True))
compromised = list(set(refanged) - set(items))
print(compromised)
count = 0
for item in compromised:
    count += 1
    print(count, item)
