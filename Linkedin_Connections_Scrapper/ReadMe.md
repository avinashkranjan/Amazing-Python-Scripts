# LinkedIn Connections Scrapper

It's a script built with the help of Selenium and Pandas to scrap LinkedIn connections list along with the skills of each connection if you want to. Using just a oneline command you can sitback and have a CSV file prepared for your cause.

# Installation

Make sure you have the following Python libraries:
> pip3 install selenium pandas

The rest should be present as core Python modules.
Next thing is to place ChromeDriver.exe in the same directory of the script. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
(Note: Download the one with the same version of your Chrome browser.)

# Usage

For basic use:
> python scrapper.py -e \<email\> -p \<password\>

For scrapping skills:
> python scrapper.py -e \<email\> -p \<password\> -s

# Furthur Notes

- The time of script progress depends on the number of connections the account has. For basic use, the script can take a time complexity of O(n^2).
- For skills scraping, the time will rise even more depending on the each profile and its contained details.
- The scripts prints out a couple of messages to explain in which phase it is.
- efficieny is also affected by Internet speed.

# Output

Basic use will output a \"scrap.csv\" file that will contain columns of Name, Headline, & Link. There will be a skills column but it will be empty.

Using the skills scrapper mode will add the skills of each profile to that column, each skill will be " -- " separated.

# Authors

Written by [XZANATOL](https://www.github.com/XZANATOL).

The project was built as a contribution during [GSSOC'21](https://gssoc.girlscript.tech/).

