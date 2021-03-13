import requests
from bs4 import BeautifulSoup as bs
import smtplib
import time
# BEGIN CONFIG
headers = {'User-Agent': 'Mozilla/5.0 Chrome/86.0.4240.75'}
# Enter the URL of the product page on flipkart
PRODUCT_URL = ''
# Enter the threshhold price of the product as a float
THRESHHOLD = 0000.0
# Enter the email address used to send the mail
MY_EMAIL = ''
# Enter app password (Check readme.md for steps to get app password)
MY_APP_PASSWORD = ''
# Enter time delay in seconds
CHECK_AGAIN = 60 * 30  # 60*30 will be 30 minutes
# Enter the recipient email
RECEIVER_EMAIL = ''
# END CONFIG

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
    if(price < THRESHHOLD):
        sendMail(title)
if (PRODUCT_URL == '' or MY_APP_PASSWORD == '' or MY_EMAIL == '' or RECEIVER_EMAIL == ''):
    print('VALUES MISSING! CHECK CONFIG VARS AGAIN!')
    exit()
while(True):
    priceCheck()
    time.sleep(CHECK_AGAIN*60)
