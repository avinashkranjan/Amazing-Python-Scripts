import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 43):
    # url="https://www.flipkart.com"
    url = "https://www.flipkart.com/search?q=MOBILE+PHONE+UNDER+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
        str(2)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
    names = box.find_all("div", class_="_4rR01T")

    # scraping data  1.product name
    for i in names:
        name = i.text
        Product_name.append(name)

    # 2.prices
    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        Prices.append(name)

    # 3.description
    desc = box.find_all("ul", class_="_1xgFaf")
    for i in desc:
        name = i.text
        Description.append(name)

    # 4.reviews
    revi = box.find_all("div", class_="_3LWZlK")
    for i in revi:
        name = i.text
        Reviews.append(name)

    # data frame
    df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices,
                      "Description": Description, "Reviews": Reviews})
    # print(df)

# DF TO CSV
df.to_csv("filpkart-Scraping-under-50k.csv")
