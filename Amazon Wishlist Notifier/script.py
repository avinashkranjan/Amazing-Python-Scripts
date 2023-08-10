import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText

# Replace with your own email and password
SENDER_EMAIL = 'your_sender_email@gmail.com'
SENDER_PASSWORD = 'your_sender_password'
RECIPIENT_EMAIL = 'recipient_email@example.com'

WISHLIST_URL = 'https://www.amazon.com/gp/registry/wishlist/YOUR_WISHLIST_ID'
CHECK_INTERVAL = 3600  # Check every hour


def get_wishlist_items():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(WISHLIST_URL, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('li', class_='a-spacing-none g-item-sortable')

        wishlist = []
        for item in items:
            name = item.find('a', class_='a-link-normal').get_text().strip()
            price_element = item.find('span', class_='a-offscreen')
            price = price_element.get_text().strip() if price_element else "Price not available"
            availability = "In stock" if "In Stock" in item.get_text() else "Out of stock"
            wishlist.append({'name': name, 'price': price,
                            'availability': availability})

        return wishlist

    else:
        print("Failed to retrieve wishlist data from Amazon.")
        return []


def send_email(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
    server.quit()


def main():
    while True:
        wishlist_items = get_wishlist_items()

        for item in wishlist_items:
            if "Price not available" not in item['price'] and "$" in item['price']:
                price = float(item['price'][1:])
                if price < 100.00:  # Set your desired price threshold
                    subject = f"Wishlist Alert: Price drop for {item['name']}!"
                    message = f"The price of {item['name']} has dropped to {item['price']}. Check it out on your wishlist: {WISHLIST_URL}"
                    send_email(subject, message)
            elif item['availability'] == "In stock":
                subject = f"Wishlist Alert: {item['name']} is back in stock!"
                message = f"{item['name']} is now back in stock. Check it out on your wishlist: {WISHLIST_URL}"
                send_email(subject, message)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
