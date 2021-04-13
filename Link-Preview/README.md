# Link Preview

A script to provide the user with a preview of the link entered.

- When entered a link, the script will provide with title, description, and link of the website that the URL points to.
- The script will do so by fetching the Html file for the link and analyzing the data from there.
- The data will be saved in a `JSON` file named `db.json` for further reference
- Every entry will have a time limit after which it will be updated (*Data expires after 7 days*)

## Setup instructions

Download the required packages from the following command in you terminal.(Make sure you're in the same project directory) 

```
pip3 install -r requirements.txt
```

## Running the script:
After installing all the requirements,run this command in your terminal.

```
python3 linkPreview.py
```

## Output

The script will provide you with Title, Description, Image Link and URL.

![demo gif](https://i.imgur.com/uoIG2io.gif)

## Author(s) 
Hi, I'm [Madhav Jha](https://github.com/jhamadhav) author of this script 🙋‍♂️

