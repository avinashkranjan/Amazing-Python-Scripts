# Reddit Meme Scraper

This script locates and downloads images from several subreddits (r/deepfriedmemes, r/surrealmemes, r/nukedmemes, r/bigbangedmemes, r/wackytictacs, r/bonehurtingjuice) into your local system.

For the sake of simplicity (and so that your system doesn't get stuffed full of images), the **download is limited to 25 (total) images per run**.
However, you are **welcome to modify that limit** to whatever amount you'd like or **remove it** altogether, but then make sure you **update `sg.ProgressBar()`** so it properly represents the download progress.

## Usage

Make sure you have installed the **necessary packages** listed in **`requirements.txt`**, then simply run **`script.py`**.
You'll be greeted by a popup window asking where to download the images, after which the download will commence.

## Screenshots

Some screenshots showing how the script works:

![Popup Asking For Destination Folder](https://raw.githubusercontent.com/Kreateer/Amazing-Python-Scripts/redditmemescraper/Reddit%20Meme%20Scraper/images/RM_Scraper_Popup_Win_01.PNG)

![Progress Bar Window](https://raw.githubusercontent.com/Kreateer/Amazing-Python-Scripts/redditmemescraper/Reddit%20Meme%20Scraper/images/RM_Scraper_Popup_Win_03.PNG)

![Popup Informing The User Where The Files Are Located](https://raw.githubusercontent.com/Kreateer/Amazing-Python-Scripts/redditmemescraper/Reddit%20Meme%20Scraper/images/RM_Scraper_Popup_Win_02.PNG)

![Console Output](https://raw.githubusercontent.com/Kreateer/Amazing-Python-Scripts/redditmemescraper/Reddit%20Meme%20Scraper/images/RM_Scraper_Console.PNG)
