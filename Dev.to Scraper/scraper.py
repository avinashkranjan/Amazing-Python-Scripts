import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from fpdf import FPDF

# Get input for category and number of articles
category = input("Enter category: ")
number_articles = int(input("Enter number of articles: "))
driver_path = input("Enter chrome driver path: ")

url = 'https://dev.to/search?q={}'.format(category)

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome(driver_path)
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)
html = driver.page_source

# Now apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
results_div = soup.find('div', {'id': 'substories'})
articles = results_div.find_all('article')

# Getting articles from dev.to
count = 0
for article in articles:
    article_data = article.find(
        'a', class_='crayons-story__hidden-navigation-link')['href']

    post_url = "https://dev.to{}".format(article_data)
    driver.get(post_url)
    time.sleep(5)

    post_html = driver.page_source
    soup = BeautifulSoup(post_html, "html.parser")
    article_div = soup.find('div', {'class': 'article-wrapper'})
    article_content = article_div.find(
        'article', {'id': 'article-show-container'})

    # Title of post found
    header_tag = article_content.find(
        'header', class_='crayons-article__header')
    title_div = header_tag.find('div', class_='crayons-article__header__meta')
    title_content = title_div.find('h1')

    # Author of post found
    author_tag = title_div.find('div', class_='crayons-article__subheader')
    author_name = author_tag.find('a', class_='crayons-link')

    # Post content found
    article_content_div = article_content.find(
        'div', class_='crayons-article__main')
    article_content_body = article_content_div.find(
        'div', class_='crayons-article__body')
    p_tags = article_content_body.find_all('p')

    title_string = (title_content.text.strip()).encode(
        'latin-1', 'replace').decode('latin-1')
    author_string = ("By - {}".format(author_name.text.strip())
                     ).encode('latin-1', 'replace').decode('latin-1')

    # Add a page
    pdf = FPDF()
    pdf.add_page()
    # set style and size of font
    pdf.set_font("Arial", size=12)

    # Title cell
    pdf.cell(200, 5, txt=title_string, ln=1, align='C')
    # Author cell
    pdf.cell(200, 10, txt=author_string, ln=2, align='C')

    for p_tag in p_tags:
        article_part = (p_tag.text.strip()).encode(
            'latin-1', 'replace').decode('latin-1')
        # Add part of article to pdf
        pdf.multi_cell(0, 5, txt=article_part, align='L')

    # save the pdf with name .pdf
    pdf_title = ''.join(e for e in title_string if e.isalnum())
    pdf.output("{}.pdf".format(pdf_title))

    count = count + 1
    if(count == number_articles):
        break

driver.close()  # closing the webdriver
