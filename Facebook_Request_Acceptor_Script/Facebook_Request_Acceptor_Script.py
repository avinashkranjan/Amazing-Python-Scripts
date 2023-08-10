from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathlib import Path
import os
import time
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 2})

# Load environmental variables from .env file
load_dotenv(dotenv_path=Path(".", ".env"))

# Read credentials from environmental variables


def read_creds():
    return {"username": os.getenv("username"), "password": os.getenv("password")}

# Function for accepting requests


def accept_requests(browser):
    browser.get("https://www.facebook.com/friends")
    element_id = browser.find_element_by_css_selector("input#email")
    element_id.send_keys(credentials["username"])
    element_id = browser.find_element_by_css_selector("input#pass")
    element_id.send_keys(credentials["password"])
    element_id.submit()

    while True:
        confirm_btns = browser.find_elements_by_css_selector(
            "div[aria-label='Confirm']")
        if not confirm_btns:
            break

        for btn in confirm_btns:
            btn.click()
            time.sleep(2)

        try:
            see_more_btn = browser.find_element_by_css_selector(
                "div.k4urcfbm.f10w8fjw.pybr56ya.taijpn5t.btwxx1t3.j83agx80.bp9cbjyn"
            )
            see_more_btn.click()
            time.sleep(12)
        except:
            pass


def main():
    # Initialize Chrome browser with options
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()

    # Read credentials and accept requests
    credentials = read_creds()
    accept_requests(browser)

    print("All Request Accepted")
    browser.quit()


if _name_ == "_main_":
    main()
