import requests
from bs4 import BeautifulSoup as bs
import argparse


parser = argparse.ArgumentParser(description='IMDB Scraper')
parser.add_argument('--t', action='store', type=str, required=True,
                    help='Enter the title of the movie')


# Base id url is used when the title id is known
base_id = "https://www.imdb.com/title"
# base url is used when the user gives a title to search for
base = "https://www.imdb.com/find?s=tt&q="
# for parsing we have used the lxml parser for optimization purposes, if lxml does not work for you replace 'lxml' with 'html.parser'


def get_info(soup):
    info = {}
    try:
        info["title"] = soup.find(
            'div', attrs={"class": "title_wrapper"}).h1.text
        info["year"] = soup.find('span', attrs={"id": "titleYear"}).a.text
        info["rating"] = soup.find(
            'span', attrs={"itemprop": "ratingValue"}).text
        subtext = soup.find("div", attrs={"class": "subtext"})
        info["genre"] = subtext.a.text
        article = soup.find('div', attrs={"id": "titleStoryLine"})
        info["plot"] = article.find(
            'div', attrs={"class": "canwrap"}).p.span.text
        details = soup.find('div', attrs={"id": "titleDetails"})
        blocks = details.findAll('div', attrs={"class": "txt-block"})
      #   Strings have been stripped as the html of imdb is not clean
      # Formatting of strings is preferrential you can change that to suit your needs
        info["country"] = blocks[1].a.text
        info["date"] = blocks[3].text[15:30]
        info["budget"] = blocks[6].text[8:23]
        info["gross_USA"] = blocks[8].text[11:]
        info["gross_worldwide"] = blocks[9].text[28:]
    except:
        print("Something went wrong")

    print(info, end="\n\n\n")


def find_movie(query):
    url = base+query
    resp = requests.get(url)
    soup1 = bs(resp.text, 'lxml')
#     Since for every query imdb gives about 150-200 responses , we choose the top 5 and return the details for them
    movie_list = soup1.findAll("tr", attrs={"class": "findResult"})[0:5]
    for movie in movie_list:
      #     Through the table given , we extract the title id from the 'href' attribute of the <a> tag
        title_id = movie.find(
            'td', attrs={"class": "result_text"}).a.attrs["href"][6:]

        url = base_id+title_id
        respo = requests.get(base_id+title_id)
        soup = bs(respo.text, 'lxml')
        get_info(soup)


if __name__ == "__main__":
    args = parser.parse_args()
    find_movie(args.t)
