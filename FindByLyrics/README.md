# Python Scripts

This repository contains multiple Python scripts that serve different purposes. Each script is described briefly below.

## `main.py`
The `main.py` script is a Python command-line tool for retrieving song lyrics and finding songs based on lyric snippets. It utilizes the `lyricsscraper` library and provides various options for searching and filtering results.

### Prerequisites
- Python 3.x
- `argparse` library
- `fuzzywuzzy` library
- `lyricsscraper` library
- `beautifulsoup4` library

### Usage
To run the script, use the command: `python main.py [arguments]`

### Description
The `main.py` script allows you to search for song lyrics or find songs based on a snippet of their lyrics. It provides options for filtering results based on various criteria such as exact match, gender, artist, album, genre, year, and more.

The script uses the `argparse` library to parse command-line arguments and provide a user-friendly interface. The available options are described below:

- `st`: The lyric snippet to search for.
- `--exact-match` or `-e`: Only return results with an exact match within them.
- `--exact-title` or `-t`: Only return results that have an exact match in the titles.
- `--gender` or `-n`: Genders to match: m for male, f for female, g for groups. Or a comma-separated list of values.
- `--artists` or `-a`: Return artists that match (can be combined with `-l` and `-m`).
- `--albums` or `-m`: Return albums that match (can be combined with `-a` and `-l`).
- `--lyrics` or `-l`: Return lyrics that match (can be combined with `-a` and `-m`).
- `--genre` or `-g`: Return matches in the genre(s). Genre can be a music genre or a comma-separated list of genres.
- `--output` or `-o`: Output the search results to a JSON file.
- `--decade` or `-d`: Only return results in the specified decade(s). The value can be a single decade or a comma-separated list of decades.
- `--count` or `-c`: Return the specified number of matches. Defaults to 1.
- `--year` or `-y`: Only return results from the specified year(s). The value can be a single year or a comma-separated list of years.
- `--style` or `-s`: Specify the style(s) to match.
- `--download-full-lyrics` or `-b`: Download the full lyrics of all matched songs into individual text files.
- `--listener` or `--full-lyrics`: Print the full lyrics from the match.
- `--page` or `-p`: Scrape multiple explicitly specified pages.
- `--help`: Show the help message and usage instructions.

The script utilizes the `LyricsDotComScraper` class from the `lyricsscraper` library to scrape and retrieve the song lyrics. It performs a search based on the provided options and displays the results. If specified, the results can be saved to a JSON file.

## Disclaimer
Please note that the accuracy and availability of song lyrics depend on the source being scraped. This script relies on the `lyricsscraper` library and its compatibility with the lyrics.com website. It is recommended to verify the obtained results and comply with the terms of use of the website.