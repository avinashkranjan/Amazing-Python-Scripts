# Football Player Club Information

This Python script allows you to scrape information about a player from Wikipedia based on their name. It uses the Wikipedia API and BeautifulSoup library to extract data from the player's Wikipedia page.

## Prerequisites

Before running the script, make sure you have the following libraries installed:
- pandas
- requests
- beautifulsoup4
- wikipedia-api

You can install these dependencies using pip:


## Usage

1. Clone this repository or download the script file (`scraper.py`).
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:
      ```    
       python scraper.py
      ```
4. The script will prompt you to enter the player's name. Provide the name of the player you want to scrape information for and press Enter.
5. The script will scrape the player's Wikipedia page and retrieve the sections related to the player's club career.
6. The retrieved sections will be printed in the console.


## Limitations
- The script assumes that the player's Wikipedia page is available in English. If the player's page is not found or is in a different language, the script may not work as expected.
- The script currently focuses on retrieving sections related to the player's club career. If you need to extract other types of information or sections, you will need to modify the code accordingly.

## Contributing
Contributions to the Football Player Club Info project are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request or open an issue.




