import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# Get chrome driver path
driver_path = input("Enter chrome driver path: ")

# Setup csv file to write data into
filename = "job_records.csv"
fields = ['Job Title', 'Company', 'Location', 'Job Description', 'URL']

# Get user choice until valid choice is entered
while (True):
    search_option = int(input(
        "Enter 1 - to search by location \nEnter 2 - to search by role, skill or company \nEnter 3 for both : "))
    if (search_option == 1):
        location = input("Enter location :")
        url = 'https://www.monsterindia.com/srp/results?locations={}'.format(
            location)
        break
    elif (search_option == 2):
        job_type = input("Enter role, skill or company : ")
        url = 'https://www.monsterindia.com/srp/results?query={}'.format(
            job_type)
        break
    elif (search_option == 3):
        location = input("Enter location :")
        job_type = input("Enter role, skill or company : ")
        url = 'https://www.monsterindia.com/srp/results?query={}&locations={}'.format(
            job_type, location)
        break
    else:
        continue
# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome(driver_path)
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)
html = driver.page_source

# Now apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
job_divs = soup.find_all("div", {"class": "card-apply-content"})

with open(filename, 'w', newline='', encoding='utf8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for job in job_divs:
        job_title_div = job.find('div', {"class": "job-tittle"})

        # Get job title
        job_title_holder = job_title_div.find('h3')
        job_title = (job_title_holder.find('a')).text.strip()

        # Get company name
        company_name_tag = job_title_div.find(
            'span', {"class": "company-name"})
        company_name = company_name_tag.find('a', {"class": "under-link"})
        if (company_name is None):
            company_name = 'confidential'
        else:
            company_name = company_name.text

        # Get location
        company_location_tag = job_title_div.find('span', {"class": "loc"})
        company_location = company_location_tag.find('small').text.strip()

        # Get job description
        job_description = job.find('p', {"class": "job-descrip"}).text.strip()

        # Get job URL
        job_url = "https:"+((job_title_holder.find('a'))['href'])

        # Add data as a row in CSV file
        csvwriter.writerow(
            [job_title, company_name, company_location, job_description, job_url])

print("Job data successfully saved in job_records.csv")
driver.close()  # closing the webdriver
