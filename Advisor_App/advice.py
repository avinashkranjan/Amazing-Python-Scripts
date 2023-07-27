# Importing files
import requests

# Function taking api link and fetch random advice quotes
def advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    print("\n")
    print(res["slip"]["advice"])
    print("\n")

advice()
