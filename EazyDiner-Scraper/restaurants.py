import json
import requests
from bs4 import BeautifulSoup


class EazyDiner:
    """
    Class - `EazyDiner`
    Example:
    ```
    restaurants = EazyDiner(location="Delhi NCR")
    ```
    Methods :
    1. ``.getRestaurants() | Response - List of restraunts and its details.
    """

    def __init__(self, location):
        self.location = location

    def getRestaurants(self):
        """
        Class - `EazyDiner`
        Example:
        ```
        del = EazyDiner("Delhi NCR") or del = EazyDiner("delhi-ncr")
        del.getRestaurants()
        ```
        Returns:
        {
            "restaurant": restaurant name
            "location": location of restaurant
            "rating": rating
            "cuisine": cuisines provided
            "price": price for two people
        }
        """
        url = (
            "https://www.eazydiner.com/restaurants?location="
            + self.location.replace(" ", "-").replace(",", "").lower()
        )
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            restaurant_data = {"restaurants": []}

            restaurants = soup.select(".restaurant")
            for r in restaurants:
                name = r.find("h3", class_="res_name").getText().strip()
                location = r.find("h3", class_="res_loc").getText().strip()
                rating = r.find("span", class_="critic").getText().strip()
                cuisine = (
                    r.find("div", class_="res_cuisine").getText().replace(
                        ",", ", ")
                )
                price = (
                    r.find("span", class_="cost_for_two")
                    .getText()
                    .encode("ascii", "ignore")
                    .decode()
                    .strip()
                )
                restaurant_data["restaurants"].append(
                    {
                        "restaurant": name,
                        "location": location,
                        "rating": rating,
                        "cuisine": cuisine,
                        "price": "Rs. " + price + " for two",
                    }
                )
            res_json = json.dumps(restaurant_data)
            return res_json
        except ValueError:
            return None
