from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import datetime

start = datetime.datetime.now()


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
        self.url = self.driver.current_url
        if self.url == "https://www.instagram.com/accounts/onetap/?next=%2F":
            self.driver.find_element_by_xpath(
                "//button[contains(text(), 'Not Now')]").click()
            sleep(4)
            self.driver.find_element_by_xpath(
                "//button[contains(text(), 'Not Now')]").click()
        else:
            sleep(2)
            self.driver.find_element_by_xpath(
                "//button[contains(text(), 'Not Now')]").click()
            sleep(1)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath(
            "//a[contains(@href,'/nidhi_vanjare')]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//a[contains(@href,'/following')]").click()
        sleep(2)
        # sug = self.driver.find_element_by_xpath(
        #     '//h4[contains(text(), Suggestions)]')
        # self.driver.execute_script('arguments[0].scrollIntoView()', sug)
        # sleep(2)

        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script(""""
                arguments[0].scrollTo(0,arguments[0].scrollHeigth);
                return arguments[0],scrollHeight;
                """, scroll_box)


usr_name = input("Enter Username : ")
password = input("Enter Password : ")


my_bot = InstaBot(usr_name, password)
my_bot.get_unfollowers()
