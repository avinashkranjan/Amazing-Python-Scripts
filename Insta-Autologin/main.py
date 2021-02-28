from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time
chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("https://instagram.com")
time.sleep(4)
username = chrome.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[1]/div/label/input')
a = input("Enter username: ")
username.send_keys(a)
password = chrome.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[2]/div/label/input')
b = getpass()
password.send_keys(b)
# time.sleep(2)
login_btn = chrome.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[3]/button/div')
login_btn.click()
