# Dev.to Scrapper
Running this Script would allow the user to scrape any number of articles from [dev.to](https://dev.to/) from any category as per the user's choice

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
The user needs to enter Category and Number of articles
![User is asked for input](https://i.postimg.cc/Qd8YfjXj/dev-scrapper1.png)

The scraped pdf files get saved in the folder in which the script is run
![Files saved in folder](https://i.postimg.cc/FzXD34W5/dev-scrapper2.png)

## Author
[Ayush Jain](https://github.com/Ayushjain2205)