import requests
from bs4 import BeautifulSoup
import json


class TechCrunch:
    """
    Class - `TechCrunch`
    Example:
    ```
    articles = TechCrunch()
    ```\n
    Methods :\n
    1. ``.getArticles() | Response - Articles with title, descriptions, images, date and link.
    """

    def get_articles(self, category):
        """
        Class - `TechCrunch`
        Example:
        ```
        articles = TechCrunch()
        articles.getArticles("artificial-intelligence")
        ```
        Returns:
        {
            "title": Tile of the article
            "description": Description of the article
            "image": Image of the article
            "author": Author of the Article
            "date": Date the article was posted
            "link": Link to the article
        }
        """
        url = (
            "https://techcrunch.com/category/" +
            category.replace(" ", "-").lower()
        )
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            articles_data = {"articles": []}

            articles = soup.find_all(
                "div", class_="post-block post-block--image post-block--unread"
            )
            for n in articles:
                name = (
                    n.select_one(".post-block__title__link")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                desc = (
                    n.select_one(".post-block__content")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                img = n.find_all("img", src=True)
                image = img[0]["src"]
                author = (
                    n.select_one(".river-byline__authors")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                time = n.find_all("div", class_="river-byline")
                date = (
                    time[0]
                    .select_one(".river-byline__time")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                links = n.find_all(
                    "a", class_="post-block__title__link", href=True)
                link = links[0]["href"]
                articles_data["articles"].append(
                    {
                        "title": name,
                        "description": desc,
                        "image": image,
                        "author": author,
                        "date": date,
                        "link": link,
                    }
                )
            res_json = json.dumps(articles_data)
            return res_json
        except ValueError:
            error_message = {
                "message": "Can't fetch any articles from the topic provided."
            }
            ejson = json.dumps(error_message)
            return ejson

    def search(self, topic):
        """
        Class - `TechCrunch`
        Example:
        ```
        articles = TechCrunch()
        articles.search("github")
        ```
        Returns:
        {
            "title": Tile of the article
            "description": Description of the article
            "image": Image of the article
            "author": Author of the Article
            "date": Date the article was posted
            "link": Link to the article
        }
        """
        url = "https://search.techcrunch.com/search?p=" + topic + "&fr=techcrunch"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            articles_data = {"articles": []}

            articles = soup.find_all(
                "li", class_="ov-a mt-0 pt-26 pb-26 bt-dbdbdb")
            for i in articles:
                name = i.find("a", class_="fz-20 lh-22 fw-b").getText()
                desc = i.find("p", class_="fz-14 lh-20 c-777").getText()
                img = i.find(
                    "img", class_="s-img mr-10 s-img-errchk", src=True)
                image = img["src"]
                author = i.find("span", class_="mr-15").getText()
                date = i.find("span", class_="pl-15 bl-1-666").getText()
                links = i.find("a", class_="fz-20 lh-22 fw-b", href=True)
                link = links["href"]
                articles_data["articles"].append(
                    {
                        "title": name,
                        "description": desc,
                        "image": image,
                        "author": author,
                        "date": date,
                        "link": link,
                    }
                )
            return articles_data
        except ValueError:
            error_message = {
                "message": "Can't fetch any articles from the topic provided."
            }
            ejson = json.dumps(error_message)
            return ejson
