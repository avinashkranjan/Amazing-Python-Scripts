# LeetCode Scraper
This python script will let the user to scrape 'n' number of LeetCode problems from any category/difficulty in [Leetcode](https://leetcode.com/problemset/all), as provided by the user. The functionality of the script is to gain the information regarding particular leetcode problem in different PDFs.

## Prerequisites:
Download the required packages from the following command in you terminal.(Make sure you're in the same project directory)

` pip3 install -r requirements.txt `

To run this script, you need to have selenium installed and configure webdriver to use chrome browser in your$PATH. You can directly download chrome driver from the link below- https://chromedriver.chromium.org/downloads.  Then, just enter the chrome driver path as asked in the prompt.

## Running the script:
After installing all the requirements,run this command in your terminal.

` python3 ques.py `

## Output:
This script will generate 'n' number of different PDFs in the same folder to store the problem information, specifically problem title, problem statement, test cases, and the problem link. 
