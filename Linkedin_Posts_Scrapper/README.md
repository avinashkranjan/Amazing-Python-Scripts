# LinkedIn Posts Scrapper

It is an automated script to scrap LinkedIn Posts, and number of Reactions and Comments from the `` /detail/recent-activity/shares/ `` endpoint.

# Installation

* Make sure you have the following Python libraries:
> pip3 install selenium pandas

* Place `` CromeDriver.exe `` in the same directory of the script. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) <br>
(Note: Download the one with the same version of your Chrome browser.)

# Usage

> python scrapper.py -e \<email\> -p \<password\> -n \<number-of-posts-to-scrap\>

# Output

The script should output a `` Scrap.csv `` file containing the scrapped posts whose columns are in the following order: Heading, Reactions, Comments

Note: If post has a 0 reaction or comment, the output will be substituted with None

