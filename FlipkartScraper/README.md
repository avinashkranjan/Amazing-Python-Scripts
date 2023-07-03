# Flipkart Scraper
## This is a simple scraper designed to extract product information from Flipkart, an e-commerce platform. The scraper is written in Python and consists of the following files:

1. dbConnector.py: This file contains the code for connecting to a database and performing database operations related to storing the scraped data.

2. genericHtmlib.py: This file provides a set of generic functions and utilities for parsing HTML and extracting data from web pages.

3. main.py: This is the main entry point of the scraper. It initializes the necessary components and orchestrates the scraping process.

4. productList.py: container categories of list that you want to scrape.

5. pycache: This directory contains the compiled bytecode of the Python files for faster execution. You can safely ignore this directory.

6. useragent.py: This file defines the User-Agent string that the scraper uses for making HTTP requests. It helps mimic the behavior of a real web browser.

## To use the Flipkart scraper, follow these steps:

Make sure you have Python installed on your system.
- create a virtual env by running the following command:
```
python3 -m venv venv
```

Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```

- open productList.py and add the categories of list that you want to scrape.

Execute the scraper by running the following command:

```
python main.py
```

The scraper will start processing the product URLs one by one, extracting relevant information such as the product name, price, description, and any other details specified in the code. The scraped data will be stored in the configured database or output format.

Please note that web scraping should be done responsibly and in compliance with the terms and conditions of the target website. Make sure to respect the website's policies regarding scraping frequency and data usage.

If you encounter any issues or have any questions, feel free to open an issue or reach out to the project maintainer.

Built with ❤️ by [Paritosh Tripathi](https://github.com/paritoshtripathi935)