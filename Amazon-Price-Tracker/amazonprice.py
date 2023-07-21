import requests
from bs4 import BeautifulSoup
import time
import smtplib
import pywhatkit
import datetime

# header = {
# "
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
# "
# }

# Url = "
# https://www.amazon.in/Apple-Original-MMTN2ZM-Lightning-Connector/dp/B01M1EEPOB/ref=sr_1_1?crid=XFITOYOGI999&keywords=airpods+apple&qid=1685422019&s=electronics&sprefix=airpods+appl%2Celectronics%2C458&sr=1-1
# "

# get your browser information by searching "my user agent"
user_agent = input("Enter your User-Agent string here\n")
headers = {"User-Agent": f'{user_agent}'}
Url = input("Drop the Url of product you wish to buy...!\n")

page = requests.get(Url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

# print(soup)


def message_sending(phone_number, title):
    now = datetime.datetime.now()
    message = f"Price of {title} is fallen below the threshold amount. Click on the link below to buy the product!!!\n\n"
    pywhatkit.sendwhatmsg(phone_number, message, now.hour, now.minute + 1)


def mail_sending(mail_id, title, password):
    server_mail = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(server_mail, port)
    server.ehlo()
    server.starttls()
    server.login(mail_id, password)
    subject = "GO BUY FAST!"
    body = f"Price of {title} is fallen below the threshold amount. Click on the link below to buy the product!!!\n\n" + Url
    message = f'Subject:{subject}\n\n {body}'
    server.sendmail(mail_id, mail_id, message)
    server.quit()


def check_price():
    title = soup.find(id="productTitle").get_text().strip()
    try:
        price = price = soup.find('span', class_='a-price-whole').text
        price = price[:len(price)-1]

    except:
        print("Object out of stock or removed")
        return

    fixed_price = float(price.replace(",", ""))
    print(title)
    print(f'The current price is {fixed_price}')
    y_price = (input('Enter the price you wish to get the product at:'))
    your_price = y_price.replace(',', '')
    mail_id = input("Please enter your email id: ")
    password = input("Enter your app password here: ")
    phone_number = input("Please enter your phone number: ")
    print(
        "Thank You! You'll receive an email as soon as the price of product drops...!"
    )
    # print(price)
    if fixed_price <= float(your_price):
        mail_sending(mail_id, title, password)
        message_sending(phone_number, title)
        exit()
    else:
        pass


while 1:
    check_price()
    # checks at an interval of 2 hours
    time.sleep(7200.00)
