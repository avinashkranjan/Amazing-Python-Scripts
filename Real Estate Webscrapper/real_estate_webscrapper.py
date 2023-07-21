import requests
from bs4 import BeautifulSoup
import pandas


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

r = requests.get(
    "https://www.magicbricks.com/ready-to-move-flats-in-new-delhi-pppfs", headers=headers)
c = r.content
soup = BeautifulSoup(c, "html.parser")


complete_dataset = []


all_containers = soup.find_all(
    "div", {"class": "flex relative clearfix m-srp-card__container"})
for item in all_containers:
    item_data = {}
    try:
        Price = item.find("div", {"class": "m-srp-card__price"}
                          ).text.replace("\n", "").replace(" ", "").replace("₹", "")
        p = Price.split()
        item_data["Price"] = p[0]

    except:
        Price = item.find("span", {"class": "luxury-srp-card__price"}
                          ).text.replace("\n", "").replace(" ", "").replace("₹", "")
        p = Price.split()
        item_data["Price"] = p[0]

    try:
        Pricepersqft = item.find(
            "div", {"class": "m-srp-card__area"}).text.replace("₹", "")
        pr = Pricepersqft.split()
        item_data["Pricepersqft"] = pr[0]

    except:
        try:
            Pricepersqft = item.find("span", {"class": "luxury-srp-card__sqft"}).text.replace(
                "\n", "").replace(" ", "").replace("₹", "")
            pr = Pricepersqft.split()
            item_data["Pricepersqft"] = pr[0]
        except:
            item_data["Pricepersqft"] = None

    try:
        item_data["Size"] = item.find(
            "span", {"class": "m-srp-card__title__bhk"}).text.replace("\n", "").strip()[0:5]
    except:
        item_data["Size"] = None

    title = item.find("span", {"class": "m-srp-card__title"})

    words = (title.text.replace("in", "")).split()

    for i in range(len(words)):
        if words[i] == "sale" or words[i] == "Sale":
            break
    s = ""
    for word in range(i+1, len(words)):
        s = s+words[word]+" "

    item_data["Address"] = s

    try:
        item_data["Carpet Area"] = item.find(
            "div", {"class": "m-srp-card__summary__info"}).text
    except:
        item_data["Carpet Area"] = item.find(
            "div", {"class": "luxury-srp-card__area__value"}).text

    complete_dataset.append(item_data)


df = pandas.DataFrame(complete_dataset)
df.to_csv("./Real Estate Webscrapper/scraped.csv")
