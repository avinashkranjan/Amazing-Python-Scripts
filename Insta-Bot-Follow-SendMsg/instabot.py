from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(10)
users = list(map(str, input(
    "Enter Users Username Comma-Separated Whom You Want to Follow and Send Msg ").split(",")))
USERNAME = input("Enter Your Username ")
PASSWORD = input("Enter Your password ")

browser.get('https://www.instagram.com/')
wait = WebDriverWait(browser, 120)
time.sleep(2)

username_field = browser.find_element_by_name('username')
username_field.send_keys(USERNAME)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()
print(users)
time.sleep(5)
for user in users:
    browser.get(f"https://www.instagram.com/{user}/")
    time.sleep(3)
    try:
        follow = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')))
        follow.click()
        time.sleep(3)
    except:
        pass
    try:
        message = browser.find_element_by_class_name('_862NM ')
        message.click()
        time.sleep(4)
        browser.find_element_by_class_name('mt3GC').click()
        time.sleep(5)
        mbox = browser.find_element_by_tag_name('textarea')
        mbox.send_keys(input("Write Msg you Want to Send "))
        mbox.send_keys(Keys.RETURN)
        time.sleep(5)
    except:
        pass
