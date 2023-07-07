import requests
from bs4 import BeautifulSoup as bs
import smtplib
import time
headers = {'User-Agent': 'Mozilla/5.0 Chrome/86.0.4240.75'}


def sendMail(title):
    '''Send Email'''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(MY_EMAIL, MY_APP_PASSWORD)
    subject = 'Change in price detected for ' + title
    print(subject)
    body = 'Click the link to go to the product page \n' + PRODUCT_URL
    msg = f"Subject: {subject}\n\n{body}"
    print(msg)
    server.sendmail(MY_EMAIL, RECEIVER_EMAIL, msg)
    print('Email Sent')
    server.quit()


def priceCheck():
    '''Price checking function'''
    page = requests.get(PRODUCT_URL, headers=headers)
    soup = bs(page.content, 'html.parser')
    # title from 'B_NuCI' class
    title = soup.find("span", {"class": "B_NuCI"}).get_text()[0:8] + '..'
    print(title)
    # price from '_30jeq3 _16Jk6d' class,
    raw_price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
    # removing unnecessary characters from the price.
    price = float(raw_price.get_text()[1:].replace(',', ''))
    print(price)
    print(THRESHHOLD)
    # If the price falls below threshold, send an email
    if (price < THRESHHOLD):
        sendMail(title)


PRODUCT_URL = input('Enter the product url:')
THRESHHOLD = float(input('Enter the desired price:'))
MY_EMAIL = input('Enter the email address that will be used to send alerts:')
MY_APP_PASSWORD = input('Enter password:')
RECEIVER_EMAIL = input('Enter the receiver email:')
CHECK_AGAIN = int(input('Enter the time between checks in minutes:'))

if (PRODUCT_URL == '' or MY_APP_PASSWORD == '' or MY_EMAIL == '' or RECEIVER_EMAIL == ''):
    print('VALUES MISSING! TRY AGAIN')
    exit()
while (True):
    priceCheck()
    time.sleep(CHECK_AGAIN*60)
