from datetime import datetime
from time import sleep

from pandas import read_csv
from selenium import webdriver
from Voice_control_Module import *


def loadText():
    """[loads the text from 'message.txt' file]"""
    with open("whatsapp-bot/message.txt", "r") as text_file:
        message = text_file.read().replace("\n", " ")
    return message


def loadContacts():
    """[gets a list of phone numbers from 'phoneNo.csv' file]"""
    data = read_csv("whatsapp-bot/phoneNo.csv")
    userNums = []
    for number in data["Phone No."]:
        userNums.append(str(number))
    return userNums


def sendMessage(userNums, message):
    """[summary]

    Args:
        userNums ([list]): [List of Phone Numbers]
        message ([str]): [Message to be sent]
    """
    for number in userNums:
        url = f"https://web.whatsapp.com/send?phone={number}"
        driver.get(url)
        sleep(5)
        messageBox = driver.find_element_by_xpath(xpaths["xMessageBox"])
        messageBox.send_keys(message)
        send = driver.find_element_by_xpath(xpaths["xSend"])
        send.click()
        sleep(1)


def scheduler():
    """[Schedule the message]"""
    speak("say year")
    year = takeCommand()

    speak("say month")
    month = takeCommand()

    speak("say day")
    day = takeCommand()

    speak("say hours")
    hours = takeCommand()

    speak("say minute")
    minute = takeCommand()

    scheduleDateTime = datetime(year, month, day, hours, minute)
    timeDiff = scheduleDateTime - datetime.now()
    sleep(timeDiff.total_seconds())


# Xpaths to locate elements
xpaths = {
    "xMessageBox": '//div[@spellcheck="true"]',
    "xSend": '//span[@data-icon="send"]',
}

if __name__ == "__main__":
    speak("Schedule the message ? say y or n")
    response = takeCommand()
    response.upper()
    if response.upper() == "Y":
        scheduler()
    # Initialize Drivers
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")

    # Authenticate Login within 15 seconds
    print("Scan the QR code to authenticate")
    sleep(15)
    speak("say user name")
    userNums = takeCommand()

    speak("say message")
    message = takeCommand()

    sendMessage(userNums, message)
    driver.close()
    pass
