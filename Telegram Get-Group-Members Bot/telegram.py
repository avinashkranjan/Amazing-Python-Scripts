from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Telegram Web URL
driver.get("https://web.telegram.org/k/")
print("Scan QR Code, And then Enter")
time.sleep(10)
print("Logged In")

# XPath for the search input field
search_input_xpath = "//input[@class='input-field-input i18n input-search-input']"

# Wait for the search input field to be clickable
wait = WebDriverWait(driver, 10)
search_input = wait.until(EC.element_to_be_clickable((By.XPATH, search_input_xpath)))

group_name = input("Enter the group name")
# Perform a search by sending keys and pressing RETURN
search_input.send_keys(group_name)
time.sleep(2)
search_input.send_keys(Keys.RETURN)

# Find and click on a chat from the search results
chat_xpath = "//a[@class='row no-wrap row-with-padding row-clickable hover-effect rp chatlist-chat chatlist-chat-abitbigger']"
chat_element = driver.find_element(By.XPATH, chat_xpath)
time.sleep(2)
chat_element.click()

# Find and click on a group in the chat
person_profile_xpath = "//div[@class='person']"
person_profile_element = driver.find_element(By.XPATH, person_profile_xpath)
time.sleep(2)
person_profile_element.click()

# Get the page source and parse with BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Find the container for member information
members_container = soup.find("div", {"class": "search-super-content-members"})

# Iterate through each member and extract information
for member_item in members_container.find("ul"):
    member_name = member_item.find("span", {"class": "peer-title"})
    if member_name:
        print("Member Name:", member_name.text)

    member_img = member_item.find("img")
    if member_img:
        print("Member Image:", member_img['src'])


