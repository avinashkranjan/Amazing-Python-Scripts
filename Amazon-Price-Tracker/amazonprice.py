import requests
from bs4 import BeautifulSoup
import time
import smtplib

# header = {
# "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
# }

# Url = "https://www.amazon.in/Apple-AirPods-Wireless-Charging-Case/dp/B07QDRYVCZ/ref=sr_1_1_sspa?crid=2O0YQXVBL4T86&dchild=1&keywords=airpods&qid=1601031081&sprefix=airpod%2Caps%2C615&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFPVUpPNUNIQUE1RUUmZW5jcnlwdGVkSWQ9QTAxNzI3NjJPNlg3OTJFSTVSOE8mZW5jcnlwdGVkQWRJZD1BMDg1MTYzNjJSRUw4VFVKQzQ1TDkmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

# get your browser information by searching "my user agent"
user_agent = input("Enter your User-Agent string here\n")
headers = {"User-Agent": f'{user_agent}'}
Url = input("Drop the Url of product you wish to buy...!\n")

page = requests.get(Url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

# print(soup)


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
        price = soup.find(
            id="priceblock_ourprice_row").get_text().strip()[:20].replace(
                '₹', '').replace(' ', '').replace('Price:', '').replace(
                    '\n', '').replace('\xa0',
                                      '').replace(',', '').replace('Fu', '')

    except:
        try:
            price = soup.find(
                id="priceblock_dealprice").get_text().strip()[:20].replace(
                    '₹', '').replace(' ', '').replace('Price:', '').replace(
                        '\n', '').replace('\xa0',
                                          '').replace(',',
                                                      '').replace('Fu', '')

        except:
            try:
                price = soup.find(
                    id="priceblock_ourprice").get_text().strip()[:20].replace(
                        '₹',
                        '').replace(' ', '').replace('Price:', '').replace(
                            '\n',
                            '').replace('\xa0',
                                        '').replace(',', '').replace('Fu', '')

            except:
                price = soup.find(id="priceblock_ourprice_lbl").get_text(
                ).strip()[:20].replace('₹', '').replace(' ', '').replace(
                    'Price:',
                    '').replace('\n',
                                '').replace('\xa0',
                                            '').replace(',',
                                                        '').replace('Fu', '')

    fixed_price = float(price)
    print(title)
    print(f'The current price is {fixed_price}')
    y_price = (input('Enter the price you wish to get the product at:'))
    your_price = y_price.replace(',', '')
    mail_id = input("Please enter your email id: ")
    password = input("Enter your app password here: ")
    print(
        "Thank You! You'll receive an email as soon as the price of product drops...!"
    )
    # print(price)
    if fixed_price <= float(your_price):
        mail_sending(mail_id, title, password)
        exit()
    else:
        pass


while 1:
    check_price()
    # checks at an interval of 2 hours
    time.sleep(7200.00)
