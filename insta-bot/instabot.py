from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from pandas import read_csv
from time import sleep


def getCredentials():
    cred = []
    with open('insta-bot/username.txt', 'r') as text_file:
        userName = text_file.readline()
        cred.append(userName)
    with open('insta-bot/password.txt', 'r') as text_file:
        password = text_file.readline()
        cred.append(password)
    return cred


def logIn():
    cred = getCredentials()
    driver.find_element_by_xpath(xpaths['xUser']).send_keys(cred[0])
    driver.find_element_by_xpath(xpaths['xPassword']).send_keys(cred[1])
    driver.find_element_by_xpath(xpaths['xLogIn']).click()
    sleep(3)


def follow(userNames):
    for user in userNames:
        driver.get('https://instagram.com/'+user)
        try:
            driver.find_element_by_xpath(xpaths['xFollow']).click()
        except NoSuchElementException:
            print('User Not Found:', user)


def unfollow(userNames):
    for user in userNames:
        driver.get('https://instagram.com/'+user)
        try:
            driver.find_element_by_xpath(xpaths['xFollowing']).click()
            sleep(2)
            driver.find_element_by_xpath(xpaths['xUnfollow']).click()
        except NoSuchElementException:
            print('User Not Found:', user)


def getUserNames():
    """[gets a list of usernames from 'people.csv' file]
    """
    data = read_csv('insta-bot/people.csv')
    userNames = []
    for names in data['Username']:
        userNames.append(names)
    return(userNames)


# Xpaths to locate elements
xpaths = {
    "xUser": "//input[@name='username']",
    "xPassword": "//input[@name='password']",
    "xLogIn": "//button[@type='submit']",
    "xFollow": "//button[contains(.,'Follow')]",
    "xFollowing": '//span[@aria-label="Following"]',
    "xUnfollow": "//button[contains(.,'Unfollow')]",
}

if __name__ == "__main__":
    res = input('''Follow/Unfollow?
Press 1 to follow
Press 0 to Unfollow
>''')
    option = Options()

    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })
    driver = webdriver.Chrome(chrome_options=option)
    driver.get('https://instagram.com')
    sleep(2)
    logIn()
    userNames = getUserNames()
    if res == '1':
        follow(userNames)
    if res == '0':
        unfollow(userNames)
    driver.close()
