import requests
from bs4 import BeautifulSoup

# Taking City You Want to Check Temperaature
city = input("Enter City : ")
# Storing City You Want to Check Temperaature
search = "weather in" + city
# Searching it on google
url = f"https://www.google.com/search?&q={search}"
# Sending and Receiving Requests
r = requests.get(url)
# Scraping Details
s = BeautifulSoup(r.text, "html.parser")
# Storing Details
update = s.find("div", class_="BNeawe").text
# Printing Details
print("Temperature in " + city + " is: " + update)
