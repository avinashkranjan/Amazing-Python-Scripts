import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}


# MAIN WEBSITE SCRAPERS

def amazon(item):
    URL = "https://www.amazon.in/s?k=" + item.replace(" ", "+")
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    name = "Amazon"
    # For access to product links un-comment these:
    #links = []
    # for link in soup.find_all("a",{"class":"a-link-normal a-text-normal"}, limit = 5):
    # links.append(link["href"])

    products = []
    prices = []

    for sp in soup.find_all("span", {"class": ["a-size-base-plus a-color-base a-text-normal", "a-size-medium a-color-base a-text-normal"]}, limit=5):
        products.append(sp.text)
    for p in soup.find_all("span", {"class": "a-price-whole"}, limit=5):
        # Extracting names of product and their prices
        prices.append(priceToInt(p.text))

    if products and prices:
        return cheapest(products, prices, name)
    else:
        print(name + " search failed.")


def flipkart(item):
    URL = "https://www.flipkart.com/search?q=" + item
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    name = "Flipkart"
    # For access to product links un-comment these:
    #links = []

    products = []
    prices = []
    for a in soup.find_all("a", {"class": "s1Q9rs"}, limit=5):
        products.append(a.text)
        # links.append(a["href"])
    for p in soup.find_all("div", {"class": "_30jeq3"}, limit=5):
        # Extracting names of product and their prices
        prices.append(priceToInt(p.text))

    if products and prices:
        return cheapest(products, prices, name)
    else:
        print(name + " search failed.")


def snapdeal(item):
    URL = "https://www.snapdeal.com/search?keyword=" + item.replace(" ", "+")
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    name = "Snapdeal"

    products = []
    prices = []

    for sp in soup.find_all("p", {"class": "product-title"}, limit=5):
        products.append(sp.text)
    for p in soup.find_all("span", {"class": "lfloat product-price"}, limit=5):
        # Extracting names of product and their prices
        prices.append(priceToInt(p.text))

    if products and prices:
        return cheapest(products, prices, name)
    else:
        print(name + " search failed.")


# HELPER FUNCTIONS

def cheapest(products, prices, name):
    # Prints top 5 products and returns the cheapest price
    productList = list(zip(products, prices))
    productList.sort(key=lambda x: x[1])
    print(name.upper() + " TOP 5 PRODUCTS:")
    print(tabulate(productList, headers=[
          "Product Name", "Price (Rs.)"]), end="\n\n")
    # Returns only the cheapest price for each website for final comparison
    return productList[0][1]


def priceToInt(price):
    # Converts the text scraped from website into integer for proper comparison
    converted_price = []
    for i in price:
        if i.isdigit():
            converted_price.append(i)  # Extracting only digits

    # Converting the string price to integer for comparison
    converted_price = int("".join(converted_price))
    return converted_price


if __name__ == "__main__":
    item = input("Enter the item you would like to search for: ")
    amazonPrices = [amazon(item), "Amazon"]
    flipkartPrices = [flipkart(item), "Flipkart"]
    snapdealPrices = [snapdeal(item), "Snapdeal"]
    if amazonPrices[0] and flipkartPrices[0] and snapdealPrices[0]:
        bestPrice = min(amazonPrices, flipkartPrices, snapdealPrices)
        print("\nBest product available for your search \"{}\" is on {} at Rs.{}".format(
            item, bestPrice[1], bestPrice[0]))
    else:
        print("Could not get the best price.")
