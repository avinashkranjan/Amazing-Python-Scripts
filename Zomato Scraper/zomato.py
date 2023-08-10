import re
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://zomato.com/ahmedabad/restaurants/cafes?category=2"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

container = soup.find("div", {"id": "root"})
i = 0

while True:
    i = 0
    for items in container.find_all("div", class_=re.compile("sc-1mo3ldo-0 sc-")):
        if i == 0:
            i = 1
            continue
        print(items.text)
        first_child = items.find("div")
        for item in first_child:
            link = item.find("a", href=True)['href']
            print(link)
            name = item.find("h4")
            print(name.text)
            rating = item.find("div", {"class": "sc-1q7bklc-1 cILgox"})
            print(rating.text)
            cusine = item.find("p")
            print(cusine.text)
            rate = item.find("p").next_sibling
            print(rate.text)
