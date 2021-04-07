# Codechef Scraper
This python script will let the user to scrape 'n' number of codechef problems from any category/difficulty in https://www.codechef.com/ ,as provided by the user. The functionality of the script is to gain the information regarding particular codechef problem in different PDFs.


## Prerequisite Steps:
Download the required packages from the following command in you terminal.(Make sure you're in the same project directory) 

```
pip3 install -r requirements.txt

```

To run this script,you need to have selenium installed and configure webdriver to use chrome browser in your`$PATH`.You can directly download chrome driver from the link below-
https://chromedriver.chromium.org/downloads
Further,you can set the path to chromedriver using

```
driver = webdriver.chrome("/usr/lib/chromium-browser/chromedriver") 

```



## Running the script:
After installing all the requirements,run this command in your terminal.

```
python3 codechef.py

```

## Output:
This script will generate 'n' number of different PDFs in a folder to store the problem information (problem title,problem statement,test cases,problem link) separately.

![image](https://user-images.githubusercontent.com/30191221/113629602-46a4ff80-9684-11eb-8938-c6e8f934d3ae.png)

![image](https://user-images.githubusercontent.com/30191221/113629697-64726480-9684-11eb-9d14-3b1ac515d40e.png)

Author:
[Smriti Raina](https://github.com/smriti26raina)
