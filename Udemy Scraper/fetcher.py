import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Get chrome driver path
driver_path = 'C:\Webdrivers\chromedriver'

# Get input for course category to scrape
category = input("Enter course category:")

url = 'https://www.udemy.com/courses/search/?src=ukw&q={}'.format(category)

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome(driver_path)
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)
html = driver.page_source

# Now apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
job_divs = soup.find_all("div", {"class": "course-card--container--3w8Zm course-card--large--1BVxY"})

for job_div in job_divs:
    title = job_div.find("div",{"class":"udlite-focus-visible-target udlite-heading-md course-card--course-title--2f7tE"}).text.strip()
    description = job_div.find("p",{"class":"udlite-text-sm course-card--course-headline--yIrRk"}).text.strip()
    instructor = job_div.find("div",{"class":"udlite-text-xs course-card--instructor-list--lIA4f"}).text.strip()

    current_price = job_div.find("div",{"class":"price-text--price-part--Tu6MH course-card--discount-price--3TaBk udlite-heading-md"}).text.strip()
    current_price = current_price.replace("Current price₹","")

    original_price = job_div.find("div",{"class":"price-text--price-part--Tu6MH price-text--original-price--2e-F5 course-card--list-price--2AO6G udlite-text-sm"}).text.strip()
    original_price = original_price.replace("Original Price₹","")

    rating = job_div.find("span",{"class":"udlite-heading-sm star-rating--rating-number--3lVe8"}).text.strip()

    hours = job_div.find_all("span",{"class":"course-card--row--1OMjg"})[0].text.strip().split()[0]

    lectures = job_div.find_all("span",{"class":"course-card--row--1OMjg"})[1].text.strip().split()[0]
    

driver.close()  # closing the webdriver