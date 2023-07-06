# Tweet Fetcher
There are 2 scripts in this project-
1. fetcher.py - This script is used to fetch tweets by a user specified hashtags and then store these tweets in a SQL database
2. display.py - This script is used to display the tweets from the database to the terminal

## Setup instructions
In order to run this script, you need to have Python and pip installed on your system. After you're done installing Python and pip, run the following command from your terminal to install the requirements from the same folder (directory) of the project.
```
pip install -r requirements.txt
```

After satisfying all the requirements for the project, Open the terminal in the project folder and run
```
python fetcher.py
python display.py
```
or
```
python3 translator.py
python3 display.py
```
depending upon the python version. Make sure that you are running the command from the same virtual environment in which the required modules are installed.

## Output
![Sample output of fetcher script](https://i.postimg.cc/9QRQNqzd/fetcher.png)
![Sample output of display script](https://i.postimg.cc/C52VjmGW/display.png)

## Author
[Ayush Jain](https://github.com/Ayushjain2205)