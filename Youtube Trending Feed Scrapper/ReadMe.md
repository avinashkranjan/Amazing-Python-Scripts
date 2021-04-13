# Youtube Trending Feed Scrapper

It's a 2 scripts that is used to scrap and read the first 10 trending news in YouTube from any its available categories. Let be What's happening right ``Now``, in ``Gaming``, in ``Music``, or in ``Movies`` You will get it on your local machine.

# Installation
* Install the following Python libraries:
> ``pip3 install selenium pymongo mongoengine pandas``


* Place ChromeDriver in the same directory of the script. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). <br>
(Note: Download the one with the same version of your Chrome browser.)


* Install MongoDB Community Server on your machine. You can refer to the installation from [here](https://docs.mongodb.com/manual/administration/install-community/).

# Usage

The scripts allows you to save the scrapped content using 2 methods:

1) A MongoDB called ``Youtube`` and saved in a collection called ``trending``.
2) A CSV file called ``Youtube.csv``.

You can save using either or both, It's up to your desires. The same goes with ``scrap_reader.py``, It can read from either MongoDB or the CSV file.

* For saving-to/reading-from a MongoDB, pass the ``-m`` argument.
* For saving-to/reading-from a CSV file, pass the ``-c`` argument.

# Output

whatever the used argument to save the data is, it will be saved containing these video attributes:
1) Video Section
2) Video Title
3) Video Link
4) Video Channel
5) Video Views
6) Video Date

# Authors

Written by [XZANATOL](https://www.github.com/XZANATOL).

The project was built as a contribution during [GSSOC'21](https://gssoc.girlscript.tech/).
