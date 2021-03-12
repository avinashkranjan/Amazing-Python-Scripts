<h1 align="center"> IMDB Scraper</h1>
Collects the information given on IMDB for the given title

---

## Modules Used

- requests
- bs4 (BeautifuSoup)
- argparse

<hr>

## How it works

- The User provides a query title and the script scrapes the IMDB website for data on it

- Since IMDB provides 200 results for every query, the data of top 5 is scraped, this is easily configurable.

## Usage

- Install dependencies
- python scraper.py --t movie-name-here(in double quotes)
- sample : python scraper.py --t "red"

## Screenshots

![Screenshot of scraped data](https://i.imgur.com/8pFFG7r.png)

#### By [Priyanshu Sharma](https://github.com/priyanshu20)
