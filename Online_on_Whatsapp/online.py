from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import users


def checkStatus():
    try:
        browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span"
        )
    except NoSuchElementException:
        return False
    return True


NEWCHAT = "/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div/span"
SEARCH = "/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]"
USER = "/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div"
ONLINE = "/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span"

browser = webdriver.Chrome(executable_path=r"/Users/sanketwable/downloads/chromedriver")
browser.get("https://web.whatsapp.com/")

print("Loading..\n")

wait = WebDriverWait(browser, 600)
time.sleep(10)

for user_name in users.USERS:

    newchat = browser.find_element_by_xpath(NEWCHAT)
    newchat.click()
    search = browser.find_element_by_xpath(SEARCH)
    search.send_keys(user_name)
    time.sleep(2)

    user = browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
    user.click()

    time.sleep(2)

    if checkStatus():
        print(user_name)
        print("is online\n")
    else:
        print(user_name)
        print("is offline\n")


print("Done checking WhatsApp online Status")