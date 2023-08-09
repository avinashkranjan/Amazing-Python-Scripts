import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.magicbricks.com/flats-in-kolkata-for-sale-pppfs")
print(response.status_code)


soup=BeautifulSoup(response.content,"html.parser")
#print(soup.prettify())

first_anchor_tag = soup.find("a")
#print(first_anchor_tag.prettify())

all=soup.find_all("div")
#print(all)

parent=soup.find_parent("a")
#print(parent)

siblings=soup.find_next_siblings("a")
#print(siblings)

card=soup.find("div",attrs={"class":"mb-srp__list"})
print("\n",card)

price=soup.find_all("div",attrs={"class":"mb-srp__card__price"})
for i in price:
    print("\n", i.text)

price1=card.find("div",attrs={"class":"mb-srp__card__price--amount"})
print("\n",price1.text)

title=soup.find_all("h2",attrs={"class":"mb-srp__card--title"})

for j in title:
    print("\n", j.text)

carpet_area=card.find("div",attrs={"class":"mb-srp__card__summary--value"})
print("\n", carpet_area.text)



status= card.find("span", attrs={"class": "mb-srp__card__summary--value"})
overlooking = card.find("div", attrs={"class": "mb-srp__card__summary--value"})

print("\nstatus:", status.text if status else "Not specified")
print("size:", overlooking.text if overlooking else "Not specified")

property_age = card.find("div", attrs={"class": "mb-srp__card__age"})

print("\nProperty Age:", property_age.text if property_age else "Not specified")


