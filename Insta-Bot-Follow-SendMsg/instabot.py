from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from selenium.webdriver.common.action_chains import ActionChains


users=['lit_perception']

USERNAME='enter username'
PASSWORD='enter password'

browser = webdriver.Chrome(
    executable_path='chromedriver.exe')

browser.get('https://www.instagram.com/')
wait = WebDriverWait(browser, 120)
time.sleep(2)

username_field = browser.find_element_by_name('username')
username_field.send_keys(USERNAME)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()
#loginForm > div > div:nth-child(3) > button > div
#msg =//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div[1]/div/button
# name msg

time.sleep(2)
for user in users:
    browser.get(f"https://www.instagram.com/{user}/")
    time.sleep(3)
    try:
        follow = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')))
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
        mbox.send_keys('HELLO')
        mbox.send_keys(Keys.RETURN)
        time.sleep(5)
    except:
        pass


