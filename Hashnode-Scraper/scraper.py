import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from fpdf import FPDF

# Get input for category and number of articles
category = input("Enter category: ")
number_articles = int(input("Enter number of articles: "))
driver_path = input('Enter chrome driver path: ')

url = 'https://hashnode.com/search?q={}'.format(category)

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome(driver_path)
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)
html = driver.page_source

# Now apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
results_div = soup.find('div', {'class': 'pb-20'})
blogs = results_div.find('div')

# Getting articles from dev.to
count = 0
for blog in blogs:

    # If div is not a blog then skip 
    check_blog = blog.find('a')['href']
    if check_blog[0] == '/':
        continue
    
    # If div is blog then start scraping individual blogs
    blog_link = blog.find('a', class_='items-start')['href']
    post_url = blog_link
    driver.get(post_url)
    time.sleep(5)

    post_html = driver.page_source
    soup = BeautifulSoup(post_html, "html.parser")
    title = soup.find('h1', itemprop = 'headline name').text
    author = soup.find('span', itemprop = 'name').text
    
    # Post content found
    blog_content_body = soup.find(
        'div', itemprop='text')
    content_tags = blog_content_body.find_all(['p','h2','h3','h4'])

    title_string = (title.strip()).encode(
        'latin-1', 'replace').decode('latin-1')
    author_string = ("By - {}".format(author.strip())
                     ).encode('latin-1', 'replace').decode('latin-1')

    # Add a page
    pdf = FPDF()
    pdf.add_page()
    # set style and size of font
    pdf.set_font("Arial", size=12)

    # Blog Title cell
    pdf.cell(200, 5, txt=title_string, ln=1, align='C')
    # Blog Author cell
    pdf.cell(200, 10, txt=author_string, ln=2, align='C')

    for tag in content_tags:
        article_part = (tag.text.strip()).encode(
            'latin-1', 'replace').decode('latin-1')
        # Add part of article to pdf
        pdf.multi_cell(0, 5, txt=article_part, align='L')

    # Trim title 
    title = title if len(title) < 30 else title[:30]

    # save the pdf with name .pdf
    pdf_title = ''.join(e for e in title if e.isalnum())
    pdf.output("{}.pdf".format(pdf_title))

    count = count + 1
    if(count == number_articles):
        break

driver.close()  # closing the webdriver
