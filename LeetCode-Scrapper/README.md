# LeetCode Scraper
This python script will let the user to scrape 'n' number of LeetCode problems from any category/difficulty in [Leetcode](https://leetcode.com/problemset/all) ,as provided by the user. The functionality of the script is to gain the information regarding particular codechef problem in different PDFs.

## Prerequisites:
Download the required packages from the following command in you terminal.(Make sure you're in the same project directory)

` pip3 install -r requirements.txt `

To run this script, you need to have selenium installed and configure webdriver to use chrome browser in your$PATH. You can directly download chrome driver from the link below- https://chromedriver.chromium.org/downloads. Further, if this argument is not specified, it will search path, otherwise you can set the path to chromedriver using

` driver = webdriver.Chrome('/path/to/chromedriver') ` 

## To Run the script:
After installing all the requirements,run this command in your terminal.

` python3 ques.py `

## Output:
This script will generate 'n' number of different PDFs in the same folder to store the problem information, specifically problem title, problem statement, test cases, and the problem link. 