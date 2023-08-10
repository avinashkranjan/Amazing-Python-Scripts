import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText


def get_amazon_product_price(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(product_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find('span', id='priceblock_ourprice')

        if price_element:
            price_text = price_element.get_text()
            return price_text.strip()
        else:
            return "Price not available"

    else:
        return "Failed to retrieve data from Amazon"


def send_email(subject, message):
    sender_email = 'your_sender_email@gmail.com'
    sender_password = 'your_sender_password'
    recipient_email = 'recipient_email@example.com'

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()


if __name__ == "__main__":
    amazon_product_url = "https://www.amazon.com/dp/B07RF1XD36/"
    target_price = 500  # Set your desired target price

    while True:
        current_price = get_amazon_product_price(amazon_product_url)
        print(f"Current Price: {current_price}")

        if current_price != "Price not available":
            numeric_price = float(current_price.replace('$', ''))
            if numeric_price <= target_price:
                subject = f"Price Alert: Amazon Product Price is now ${numeric_price}"
                message = f"The price of the Amazon product is now ${numeric_price}. You can check it here: {amazon_product_url}"
                send_email(subject, message)
                break

        # Check the price every hour
        time.sleep(3600)
