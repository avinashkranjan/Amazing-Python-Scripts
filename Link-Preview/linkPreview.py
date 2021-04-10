import requests
from bs4 import BeautifulSoup

url = 'https://www.girlscript.tech/'
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
# print(soup)

title = soup.find("meta", property = "og:title")
description = soup.find("meta", property = "og:description")
url = soup.find("meta", property = "og:url")
img = soup.find("meta", property = "og:image")


print("Title : ", title.get("content", None))
print("Description : ", description.get("content", None))
print("URL : ", url.get("content", None))
print("Image Link : ", img.get("content", None))
