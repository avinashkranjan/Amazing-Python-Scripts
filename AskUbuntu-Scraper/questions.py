from bs4 import BeautifulSoup
import requests
import json


class AskUbuntu:
    """
    Create an instance of `AskUbuntu` class.

    ```python
    questions = AskUbuntu("topic")
    ```
    """

    def __init__(self, topic):
        self.topic = topic

    def getQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            json_data = json.dumps(questions_data)
            return json_data
        except ValueError:
            error_message = {
                "message": "No questions related to the topic found"}
            ejson = json.dumps(error_message)
            return ejson
