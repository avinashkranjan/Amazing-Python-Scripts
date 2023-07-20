from selenium import webdriver  # connect python with webbrowser-chrome
from selenium.webdriver.common.keys import Keys
import pyautogui as pag


def main():
    url = "http://linkedin.com/"  # url of LinkedIn
    network_url = "http://linkedin.com/mynetwork/"    # url of LinkedIn network page
    # path to browser web driver
    driver = webdriver.Chrome('F:\Argha\WebDriver\chromedriver.exe')
    driver.get(url)


def login():
    username = driver.find_element_by_id(
        "login-email")      # Getting the login element
    # Sending the keys for username
    username.send_keys("username")
    password = driver.find_element_by_id(
        "login-password")     # Getting the password element
    # Sending the keys for password
    password.send_keys("password")
    # Getting the tag for submit button
    driver.find_element_by_id("login-submit").click()


def goto_network():
    driver.find_element_by_id("mynetwork-tab-icon").click()


def send_requests():
    n = input("Number of requsts: ")   # Number of requests you want to send
    for i in range(0, n):
        pag.click(880, 770)  # position(in px) of connection button
    print("Done!")
