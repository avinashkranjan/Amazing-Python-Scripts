import urllib
import time
import requests
import re
import csv
from bs4 import BeautifulSoup


def write_csv(loc, info):
    """
    The function writes the job openings collected in a .csv file
    """
    headers = ['Title', 'Company Name', 'Location', 'Date', 'Summary', 'Url']

    # Adding info into the rows of the file
    with open('./Job Scraper/' + loc+'_openings.csv', 'a', encoding='utf-8') as csv_f:
        csv_p = csv.writer(csv_f, delimiter=',')
        csv_p.writerow(headers)
        csv_p.writerows(info)

    print(f'\n{loc}_openings.csv has been saved to your directory!\n')


def job_scraper():
    """
    The function scrapes the required number of job openings posted for a given job title and location
    and stores all the associated information in a .csv file
    """
    title = input("\nEnter job title: ").replace(" ", "+")
    loc = input("Enter job location: ").replace(" ", "+")
    num = int(input("Enter the number of job openings to obtain: "))

    url = f'https://in.indeed.com/jobs?q={title}&l={loc}'
    req_page = requests.get(url)

    job_array = []

    if req_page.status_code == 200:
        soup = BeautifulSoup(req_page.text, "html.parser")
        job_table = soup.find("td", id="resultsCol")
        count = 0
        
        flag = 1
        while flag :
            for job_card in job_table.find_all("div", class_="jobsearch-SerpJobCard"):
                # Getting the job title
                title_elem = job_card.find('a', class_='jobtitle turnstileLink')
                title = title_elem.text.strip()

                # Getting the company name
                company_details = job_card.find('div', class_='sjcl')
                company_name = company_details.find('span', class_='company')
                company_name = company_name.text.strip()
                
                # Getting the company location
                company_loc = company_details.find('span', class_='location')
                if company_loc!= None:
                    company_loc = company_loc.text.strip()
                else:
                    company_loc = loc

                # Getting the URL of the post
                link = job_card.find('a')['href']
                link = 'https://in.indeed.com' + link

                # Getting the date of the post
                date_elem = job_card.find('span', class_='date')
                date = date_elem.text.strip()

                # Getting the job summary
                summary_ele = job_card.findAll('div', attrs={'class': 'summary'})
                for span in summary_ele:
                    span = span.text.strip()

                count += 1

                job_array.append([title, company_name, company_loc, date, span, link])
                if count == num:
                    flag = 0
                    break

            # To go to the next page
            page = soup.find("ul", class_="pagination-list")
            found = 0
            for page in page.find_all('a'):
                if page.attrs['aria-label'] == 'Next':
                    found = 1
                    break
            
            if found:
                next_page_link = 'https://in.indeed.com' + page.attrs['href']

                time.sleep(2)

                req_page = requests.get(next_page_link)
                soup = BeautifulSoup(req_page.text, "html.parser")
                job_table = soup.find("td", id="resultsCol")

            else:
                flag = 0

        write_csv(loc, job_array)


    else:
        print('There seems to be a problem fetching the results. Check your inputs, connections and try again')


if __name__ == '__main__':
    job_scraper()

