import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

inputName = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
inputEmailID = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
inputPhone = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

# Submit Button Xpath
Submit = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div'


def sleep():
    time.sleep(3)


browswer = webdriver.Firefox(
    executable_path='C:\geckodriver-v0.28.0-win64\geckodriver.exe')
browswer.get(
    'https://docs.google.com/forms/d/e/1FAIpQLScBejWF809oacjZlvkciXREi50fyHcq75l988KDJo3ycG7xkg/viewform'
)
name = []
email = []
phone = []
with open("input.csv", "r") as f_input:
    csv_input = csv.DictReader(f_input)
    for row in csv_input:
        name.append(row['name'])
        email.append(row['email'])
        phone.append(row['phone_number'])

    # print(name,email,phone)
i = 0

while i < len(name):
    browswer.find_element_by_xpath(inputName).send_keys(name[i])
    browswer.find_element_by_xpath(inputEmailID).send_keys(email[i])
    browswer.find_element_by_xpath(inputPhone).send_keys(phone[i])
    sleep()
    browswer.find_element_by_xpath(Submit).click()
    i += 1
    sleep()
    browswer.back()
    sleep()

# print(name,email,phone)
browswer.quit()
