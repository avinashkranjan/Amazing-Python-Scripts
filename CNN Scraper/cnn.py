from bs4 import BeautifulSoup
import requests


class NewsCNN:
    """
    Create an instance of `NewsCNN` class.\n
    ```python
    news = NewsCNN()
    ```
    | Methods               | Details                                                                           |
    | ---------------------------- | -------------------------------------------------------------------------- |
    | `.news_by_location(country="india)` | Returns the list of articles by a specific country.               |
    | `.news_by_category(type)`           | Returns the list of articles by a specific category.              |
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }

    def news_by_location(self, country: str):
        """
        Returns the relevant news articles corresponding to that particular geo-continent or country\n
        Class - `NewsCNN`
        Parameters: \n
        - country: Name of the country\n
        ```python
        news = newsCNN()
        news.news_by_location()
        ```
        """

        try:
            sol = []
            obj_keys = ["news", "link"]
            location = country.lower()
            URL = f"https://edition.cnn.com/world/{location}"
            page = requests.get(URL)
            parse = BeautifulSoup(page.content, "html.parser")
            heads = parse.find_all("span", attrs={"data-editable": "headline"})
            links1 = parse.find_all(
                "a",
                attrs={
                    "class": "container__link container_lead-plus-headlines-with-images__link"
                },
            )
            links2 = parse.find_all(
                "a", attrs={"class": "container__link container_vertical-strip__link"}
            )
            links3 = parse.find_all(
                "a",
                attrs={"class": "container__link container_lead-plus-headlines__link"},
            )

            base = "https://edition.cnn.com/"
            allurls = []
            allheads = []

            for i in heads:
                tmp = i.text
                allheads.append(tmp)

            for i in links1 + links2 + links3:
                t = base + i["href"]
                allurls.append(t)
            allurls = list(set(allurls))

            for i in range(len(allurls)):
                obj_values = [allheads[i], allurls[i]]
                new_obj = dict(zip(obj_keys, obj_values))
                sol.append(new_obj)

            return sol
        except:
            return None

    def news_by_category(self, type: str):
        """
        Returns a list of news articles from a specific category.

        Parameters:
        - type (str): The category of news articles to retrieve. Allowable types are: "politics", "business", "opinions", "health", "style".

        Returns:
        A list of dictionaries, each containing news article information including title and link, or an exception if an error occurs.

        Example:
        ```python
        news = NewsCNN()
        politics_articles = news.news_by_category("politics")
        ```
        """
        try:
            sol = []
            type = type.lower()
            url = f"https://edition.cnn.com/{type}"
            page = requests.get(url, headers=self.headers)
            parse = BeautifulSoup(page.content, "html.parser")
            articles = parse.find_all(
                "a", {"class": "container__link container_lead-plus-headlines__link"}
            )
            for article in articles:
                text = article.find("span", {"data-editable": "headline"})
                if text:
                    link = "https://edition.cnn.com" + article["href"]
                    data = {"Title": text.text, "Link": link}
                    sol.append(data)
            return sol
        except Exception as e:
            return e
