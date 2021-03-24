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


def get_info(soup):
    info = {}
    labels = ["title", "year", "rating", "genre", "plot", "date", "country",
              "language", "budget", "gross", "gross_usa", "opening_week_usa"]
    try:
        info["title"] = soup.find(
            'div', attrs={"class": "title_wrapper"}).h1.get_text(strip=True)
        info["year"] = soup.find(
            'span', attrs={"id": "titleYear"}).a.get_text(strip=True)
        info["rating"] = soup.find(
            'span', attrs={"itemprop": "ratingValue"}).get_text(strip=True)
        subtext = soup.find("div", attrs={"class": "subtext"})
        info["genre"] = subtext.a.get_text(strip=True)
        article = soup.find('div', attrs={"id": "titleStoryLine"})
        info["plot"] = article.find(
            'div', attrs={"class": "canwrap"}).p.span.get_text(strip=True)
        details = soup.find('div', attrs={"id": "titleDetails"})
        blocks = details.findAll('div', attrs={"class": "txt-block"})
        for block in blocks:
            heading = block.h4.get_text(strip=True)
            if heading == "Release Date:":
                info["date"] = block.get_text(strip=True).replace(
                    "See more»", '').replace(heading, '')
            if heading == "Country:":
                info["country"] = block.a.get_text(strip=True)
            if heading == "Language":
                info["language"] = block.a.get_text(strip=True)
            if heading == "Budget:":
                info["budget"] = block.get_text(
                    strip=True).replace(heading, '')
            if heading == "Cumulative Worldwide Gross:":
                info["gross"] = block.get_text(
                    strip=True).replace(heading, '')
            if heading == "Gross USA:":
                info["gross_usa"] = block.get_text(
                    strip=True).replace(heading, '')
            if heading == "Opening Weekend USA:":
                info["opening_week_usa"] = block.get_text(
                    strip=True).replace(heading, '')
    except:
        assert any(obj in labels for obj in info), "No info found"

    if len(info) > 4:
        print(info, end="\n\n\n")


def find_movie(query):
    url = base+query
    resp = requests.get(url)
# for parsing we have used the lxml parser for optimization purposes, if lxml does not work for you replace 'lxml' with 'html.parser'
    soup1 = bs(resp.text, 'lxml')
# Since for every query imdb gives about 150-200 responses , we choose the top 5 and return the details for them
    movie_list = soup1.findAll("tr", attrs={"class": "findResult"})[0:5]
    if movie_list:
        for movie in movie_list:
            # Through the table given , we extract the title id from the 'href' attribute of the <a> tag
            title_id = movie.find(
                'td', attrs={"class": "result_text"}).a.attrs["href"][6:]

            url = base_id+title_id
            respo = requests.get(base_id+title_id)
            soup = bs(respo.text, 'lxml')
            get_info(soup)
    else:
        print("No results found")


if __name__ == "__main__":
    args = parser.parse_args()
    find_movie(args.t)
