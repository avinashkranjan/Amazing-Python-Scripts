## Image Scraper

The aim of the provided script is to scrape all HTML <img> tags from a given URL.

    It imports the necessary modules: BeautifulSoup from the bs4 (Beautiful Soup) library for parsing HTML, and requests for making HTTP requests.
    The code checks the length of the command-line arguments. If the length is not equal to 2 (indicating that a URL was not provided), it exits with an error message.
    It uses the requests.get() function to make an HTTP GET request to the provided URL. The User-Agent header is set to mimic a web browser to avoid any potential blocking or filtering.
    The response from the request is then passed to BeautifulSoup to parse the HTML content of the page.
    The find_all() method is used on the parsed HTML data to find all <img> tags with a valid src attribute. The src=True parameter filters out <img> tags without the src attribute.
    A loop iterates over the list of found images, and each image is printed.

In summary, the script allows you to scrape and print all HTML <img> tags (along with their attributes) from a given URL.


### Installation Requirements -
1. pip install beautifulsoup4
2. pip install requests

