import urllib
import requests
import pandas as pd
import json
from bs4 import BeautifulSoup as Soup


class Quora:

    """
    Class - `Quora`\n
    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.fetch_answers()`          | Returns the list of answers pertaining to a particular url gien by the user as parameter.            |
    | `.get_by_query()`             | Returns the list of answers pertaining to a particular query given by the user.                      |
    | `.profile_details()`             | Returns the list of the name of a user along with their quora profile link.                          |

    """

    def __init__(self):
        pass

    def fetch_answers(self, url):
        """
        Class - `Quora`
        Example:
        ```
        quora = Quora()
        quora.fetch_answers('url goes here')
        ```
        Returns:
        ```js
        {
            "answers": The list of all the answers aviliable for a particular link of question.
        }
        ```
        """
        try:
            req = requests.get(url)

            page_soup = Soup(req.content, "html.parser")
            main_box = page_soup.findAll("script", {"type": "application/ld+json"})[
                0
            ].text

            data = json.loads(main_box)
            answers = []
            try:
                answers += [x["text"] for x in data["mainEntity"]["acceptedAnswer"]]
            except:
                pass
            answers += [x["text"] for x in data["mainEntity"]["suggestedAnswer"]]

            return answers
        except:
            return None

    def get_by_query(self, query):
        """
        Returns the list of all the answers aviliable for a particular query of question given. If there is no data aviliable, then empty list is returned.
        Class - `Quora`
        Example:
        ```python
        quora = Quora()
        quora.get_by_query(query="How-should-I-start-learning-Python-1")
        ```
        Returns:
        ```js
        [ ... ]
        ```
        """
        try:
            base = "https://www.quora.com/"
            query = query.replace(" ", "-")
            url = base + query
            k = Quora().fetch_answers(url)
            return k[0]
        except:
            return None

    def profile_details(self, username):
        """
        Class - `Quora`
        Example:
        ```python
        quora = Quora()
        quora.profile_details(username="Nikhil-Raj-1727")
        ```
        Returns:
        ```js
        {'name': 'Avinash Ranjan', 'url': 'https://www.quora.com/profile/avinash'}
        ```
        """
        try:
            username = username.upper()
            username = username.split()
            for i in range(1, len(username)):
                username[i] = "-" + username[i]

            res = "".join(username)
            base = "https://www.quora.com/profile/"
            url = base + res
            req = requests.get(url)
            soup = Soup(req.content, "html.parser")

            name = soup.find_all("meta")[3]["content"]
            obj_keys = ["name", "url"]
            obj_values = [name, url]

            return dict(zip(obj_keys, obj_values))
        except:
            return None
