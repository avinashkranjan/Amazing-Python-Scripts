## Real Estate Webscrapper
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
- Now run the real_estate_webscrapper.py file to create the output2.csv file.
- Then output2.csv will be created in the same folder as real_estate_webscrapper.py file and it can be opened using Microsoft Excel.
---
### Step 1
- Load the website https://www.magicbricks.com/ready-to-move-flats-in-new-delhi-pppfs in your code using requests.

### Step 2
- Use inspect in website to know which div contains the information that we need
- Use beautiful soup to load the information in program and store it into a dictionary for each property

### Step 3
- Use pandas to convert the list of dictionaries to csv file
---

## Author
[Himanshi2997](https://github.com/Himanshi2997)
---

## Output
![output2](https://user-images.githubusercontent.com/67272318/118381259-b8b71f80-b606-11eb-983d-5d8094d05f06.PNG)
