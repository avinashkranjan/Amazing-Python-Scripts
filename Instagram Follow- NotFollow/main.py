from selenium import webdriver
from time import sleep
import datetime
from prettytable import PrettyTable

start = datetime.datetime.now()


table = PrettyTable()
column_names = ["Non-Followers"]


class InstaBot:
    """ for login
        """

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
        """ names of unfollowers
        """
        self.driver.find_element_by_xpath(
            "//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//a[contains(@href,'/following')]").click()
        following = self._get_names()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//a[contains(@href,'/followers')]").click()
        sleep(2)
        followers = self._get_names()

        notfollowingback = [
            user for user in following if user not in followers]

        table.add_column(column_names[0], notfollowingback)

        print(table)

    def _get_names(self):
        """ names of unfollowers
        """

        sleep(2)
        scroll_box = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]')
        last_ht, ht = 0, 1

        # Keep scrolling till you can't go down any further
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script(
                """
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)

        # Gets the list of accounts
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        sleep(1)

        # Closes the box
        close_btn = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[1]/div/div[2]')
        close_btn.click()

        return names


usr_name = input("Enter Username : ")
password = input("Enter Password : ")

my_bot = InstaBot(usr_name, password)
my_bot.get_unfollowers()
