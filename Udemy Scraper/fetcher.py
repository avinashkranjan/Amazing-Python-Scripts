import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3
from sqlite3 import Error

# Function to connect to the SQL Database


def sql_connection():
    try:
        con = sqlite3.connect('./Udemy Scraper/udemyDatabase.db')
        return con
    except Error:
        print(Error)

# Function to create table


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS courses(title text, description text, instructor text,current_price INTEGER, original_price INTEGER, rating REAL, hours REAL, lectures INTEGER)")
    con.commit()


# Call functions to connect to database and create table
con = sql_connection()
sql_table(con)

# Function to insert into table


def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute(
        'INSERT INTO courses(title, description, instructor, current_price, original_price, rating, hours, lectures) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entities)
    con.commit()


# Get chrome driver path
driver_path = input("Enter chrome driver path: ")

print("\nSome Categories Available on Udemy include:\nDevelopment -  Python, Web Development, Javascript, Java \nDesign - Photoshop, Blender, Graphic design\n")

# Get input for course category to scrape
category = input("Enter course category: ")

url = 'https://www.udemy.com/courses/search/?src=ukw&q={}'.format(category)

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome(driver_path)
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)
html = driver.page_source

# Now apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
course_divs = soup.find_all(
    "div", {"class": "course-card--container--3w8Zm course-card--large--1BVxY"})

# Get all course divs and extract information from individual divs
for course_div in course_divs:
    title = course_div.find("div", {
                            "class": "udlite-focus-visible-target udlite-heading-md course-card--course-title--2f7tE"}).text.strip()
    description = course_div.find(
        "p", {"class": "udlite-text-sm course-card--course-headline--yIrRk"}).text.strip()
    instructor = course_div.find(
        "div", {"class": "udlite-text-xs course-card--instructor-list--lIA4f"}).text.strip()

    current_price = course_div.find(
        "div", {"class": "price-text--price-part--Tu6MH course-card--discount-price--3TaBk udlite-heading-md"}).text.strip()
    current_price = current_price.replace("Current price₹", "")

    original_price = course_div.find(
        "div", {"class": "price-text--price-part--Tu6MH price-text--original-price--2e-F5 course-card--list-price--2AO6G udlite-text-sm"}).text.strip()
    original_price = original_price.replace("Original Price₹", "")

    rating = course_div.find("span", {
                             "class": "udlite-heading-sm star-rating--rating-number--3lVe8"}).text.strip()

    hours = course_div.find_all(
        "span", {"class": "course-card--row--1OMjg"})[0].text.strip().split()[0]

    lectures = course_div.find_all(
        "span", {"class": "course-card--row--1OMjg"})[1].text.strip().split()[0]

    entities = (title, description, instructor, current_price,
                original_price, rating, hours, lectures)
    sql_insert(con, entities)

print("Saved successfully in database!")

driver.close()  # closing the webdriver
