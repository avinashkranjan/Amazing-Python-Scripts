# Monster Jobs Scrapper

Running this Script would allow the user to scrape job openings from [Monster jobs](https://www.monsterindia.com), based on their choice of location, job role, company or designation.

## Setup instructions

In order to run this script, you need to have Python and pip installed on your system. After you're done installing Python and pip, run the following command from your terminal to install the requirements from the same folder (directory) of the project.

```
pip install -r requirements.txt
```

As this script uses selenium, you will need to install the chrome webdriver from [this link](https://sites.google.com/a/chromium.org/chromedriver/downloads)

After satisfying all the requirements for the project, Open the terminal in the project folder and run

```
python scraper.py
```

or

```
python3 scraper.py
```

depending upon the python version. Make sure that you are running the command from the same virtual environment in which the required modules are installed.

## Output

The user needs to enter input as per required job

![User is asked for input](https://i.postimg.cc/tg270Zjs/monster-scraper-input.png)

The scraped jobs are stored in a CSV file with name job_records.csv

![Jobs saved in csv file](https://i.postimg.cc/x1gbQFGj/monster-scraper-output.png)

## Author

[Ayush Jain](https://github.com/Ayushjain2205)
