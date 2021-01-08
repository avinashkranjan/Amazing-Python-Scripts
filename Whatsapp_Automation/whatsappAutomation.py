# Selenium is required for automation
# sleep is required to have some time for scanning
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def whatsapp(to, message):
    person = [to]
    string = message
    chrome_driver_binary = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
    # Selenium chromedriver path
    driver = webdriver.Chrome(chrome_driver_binary)
    driver.get("https://web.whatsapp.com/")
    sleep(15)
    # This will find the person we want to send the message to in the list
    for name in person:
        user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
        user.click()
        text_box = driver.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        try:
            text_box.send_keys(string)
            sendbutton = driver.find_elements_by_xpath(
                '//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            sendbutton.click()
            sleep(10)
            print('Message Sent!!')
        except:
            print('Error occured....')


if __name__ == "__main__":
    to = input('Who do you want to send a message to? Enter the name: ')
    content = input("What message to you want to send? Enter the message: ")
    whatsapp(to, content)
