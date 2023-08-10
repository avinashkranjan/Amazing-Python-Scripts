import requests
from bs4 import BeautifulSoup


def scrape_amazon_bestsellers(category_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(category_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', class_='zg-item-immersion')

        for index, product in enumerate(products, start=1):
            title = product.find(
                'div', class_='p13n-sc-truncate').get_text().strip()
            rank = index
            print(f"Rank: {rank}\nTitle: {title}\n")

    else:
        print("Failed to retrieve data from Amazon.")


if __name__ == "__main__":
    category_url = "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/"
    scrape_amazon_bestsellers(category_url)
