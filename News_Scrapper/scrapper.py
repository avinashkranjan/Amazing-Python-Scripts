from bs4 import BeautifulSoup
import requests
import csv

URL = "https://www.indiatoday.in/"


def writeToCSV(topTenNews, category):
    with open("topTen" + category + "News.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Link", "Headline"])
        for news in topTenNews:
            writer.writerow(
                [news[2], "https://www.indiatoday.in/" + news[1], news[0]])


def getTopTenFromDivTag(category):
    topTenNews = []
    count = 0
    category_url = URL + category

    page = requests.get(category_url)
    soup = BeautifulSoup(page.text, "html.parser")

    all_div_tags = soup.find_all(class_="detail")

    for div in all_div_tags:
        count += 1
        if count > 10:
            break
        headline = div.find("h2").text
        link = div.find("a").attrs["href"]
        date = div.find("a").attrs["href"][-10:]
        topTenNews.append([headline, link, date])

    return topTenNews


def getTopTenFromLiTag(category):
    topTenNews = []
    count = 0
    category_url = URL + category

    page = requests.get(category_url)
    soup = BeautifulSoup(page.text, "html.parser")

    ul_tag = soup.find_all(class_="itg-listing")
    ul_tag = str(ul_tag)[25:-6]
    li_tags = ul_tag.split("</li>")

    for li in li_tags:
        count += 1
        if count > 10:
            break
        ele = li.split(">")
        link = ele[1].split("=")[1][2:-1]
        headline = ele[2][:-3]
        date = link[-10:]
        topTenNews.append([headline, link, date])

    return topTenNews


def main():

    categories = ["india", "world", "cities", "business", "health", "technology", "sports",
                  "education", "lifestyle"]

    print("Please Choose a Category from the following list")

    for index, category in enumerate(categories):
        print(str(index + 1) + ". " + category.capitalize())

    print("Example: Enter 'world' for top 10 world news")
    print()

    category = input()
    category = category.lower()

    if category not in categories:
        print("\nPlease choose a valid category!")
        exit()

    if category in categories[:5]:
        topTenNews = getTopTenFromDivTag(category)
    else:
        topTenNews = getTopTenFromLiTag(category)

    writeToCSV(topTenNews, category)

    print("Created CSV File Successfully!")


main()
