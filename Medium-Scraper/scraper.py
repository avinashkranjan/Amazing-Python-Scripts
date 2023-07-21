import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from fpdf import FPDF

# Get input for category and number of articles
category = input("Enter category (Ex- Programming or javascript) : ")
number_articles = int(input("Enter number of articles: "))
driver_path = input("Enter chrome driver path: ")

url = 'https://medium.com/topic/{}'.format(category)

# initiating the webdriver to run in incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(driver_path, options=chrome_options)
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)
html = driver.page_source

# Now apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
articles = soup.find_all('section')

# Getting articles from medium
num = number_articles
for article in articles:
    article_data = article.find('a')['href']
    if article_data[0] == '/':
        article_data = 'https://medium.com' + article_data

    post_url = article_data
    driver.get(post_url)
    time.sleep(5)

    post_html = driver.page_source
    soup = BeautifulSoup(post_html, "html.parser")
    a_tags = soup.find_all('a')

    author = a_tags[2].text

    title = soup.find('h1').text.strip()
    section = soup.find_all('section')[1]
    p_tags = section.find_all('p')

    title_string = (title).encode(
        'latin-1', 'replace').decode('latin-1')
    author_string = (author).encode('latin-1', 'replace').decode('latin-1')

    # Add a page in pdf
    pdf = FPDF()
    pdf.add_page()
    # set style and size of font for pdf
    pdf.set_font("Arial", size=12)

    # Title cell
    pdf.cell(200, 5, txt=title_string, ln=1, align='C')
    # Author cell
    pdf.cell(200, 10, txt=author_string, ln=2, align='C')

    for p_tag in p_tags:
        article_part = (p_tag.text.strip()).encode(
            'latin-1', 'replace').decode('latin-1')
        article_part += '\n'
        # Add part of article to pdf
        pdf.multi_cell(0, 5, txt=article_part, align='L')

    # save the pdf with name .pdf
    pdf_title = ''.join(e for e in title if e.isalnum())
    pdf.output("{}.pdf".format(pdf_title))

    num = num-1
    if (num == 0):
        break


driver.close()  # closing the webdriver
