# import requests module first 
import requests as rq
from bs4 import BeautifulSoup

url = input("Enter Link: ")### input link by user

if ("https" or "http") in url:
 data = rq.get(url)
else:
 data = rq.get("https://" + url)

soup = BeautifulSoup(data.text, "html.parser")

links = []

for link in soup.find_all("a"):
 links.append(link.get("href"))

with open("myLinks.txt", 'w') as saved:
 print(links[:20], file=saved)
