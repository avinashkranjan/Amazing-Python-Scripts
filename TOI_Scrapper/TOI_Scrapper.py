import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrapper():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    # accessing TOI webpage disguised as a browser
    webpage = requests.get(
        'https://timesofindia.indiatimes.com/', headers=headers).text

    soup = BeautifulSoup(webpage, 'lxml')
    news = []
    link_list = []

    for i in soup.find_all('div', class_='col_l_6'):
        figcaption = i.find('figcaption')
        if figcaption is not None:
            # finding news headline as well its corresponding link
            link_news = i.find('a').get("href")
            text_news = figcaption.text.strip()

            news.append(text_news)
            link_list.append(link_news)
    df = pd.DataFrame({'News_Headline': news, 'News_Link': link_list})
    return df


TOI_headline = scrapper()
print(TOI_headline)
