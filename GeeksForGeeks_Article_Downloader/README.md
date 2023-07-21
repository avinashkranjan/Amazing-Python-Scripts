# Save any article you like from GeeksForGeeks as a pdf

This python script will download articles from GeeksForGeeks and save them as a pdf file. The script uses Selenium Webdriver and fpdf library. Selenium is used with Chrome Webdriver, so having Chrome browser is a requirement.

## Setting up:

- Create a virtual environment and activate it.

- Install the requirements

```sh
  $ pip install -r requirements.txt
```

## Running the script:

```sh
  $ python geeksforgeeks_article_downloader.py [url]  #without the brackets
```

## Example running the script :

```sh
  $ python geeksforgeeks_article_downloader.py https://www.geeksforgeeks.org/shortest-path-faster-algorithm/?ref=leftbar-rightbar
```

The program will ask you to enter a filename(without '.pdf'). The pdf will be created in the same folder.

![article screenshot](https://snipboard.io/KNtJ3X.jpg)