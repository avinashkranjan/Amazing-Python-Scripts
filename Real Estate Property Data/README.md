# Real Estate Webscrapper
- It will take information from the real estate site and store it in the form of csv file making the data more organised and locally accessible.

___

## Requirements
- BeautifulSoup
- Pandas
---
## How To install
> pip install pandas

> pip install beautifulsoup
---
- Now run the real_estate_webscrapper.py file to create the output.csv file.
- Then output.csv will be created in the same folder as real_estate_webscrapper.py file and it can be opened using Microsoft Excel.
---

## Procedure

### Step 1
- Load the website  http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/ in your code using requests.
- Count the number of pages in the website

### Step 2
- Use inspect in website to know which div contains the information that we need
- Use beautiful soup to load the information in program and store it into a dictionary for each property where each key of the dictionary represents an attribute of property

### Step 3
- Use pandas to convert the list of dictionaries to csv file
