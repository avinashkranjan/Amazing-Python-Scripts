# Stack overflow question scraper
Running this Script would allow the user to scrape top questions from Stack overflow based on the question tag(python, java, etc) of their choice. The question, summary, link, votes and views will be stored in a local SQL DB.

## Setup instructions
In order to run this script, you need to have Python and pip installed on your system. After you're done installing Python and pip, run the following command from your terminal to install the requirements from the same folder (directory) of the project.
```
pip install -r requirements.txt
```
After satisfying all the requirements for the project, Open the terminal in the project folder and run
```
python scraper.py
```
or
```
python3 scraper.py
```
depending upon the python version. Make sure that you are running the command from the same virtual environment in which the required modules are installed.

## Output

The user can choose the question tag based on which they want to scrape top questions from Stack Overflow.

![Stack overflow question scraper](https://i.postimg.cc/d3FrwysV/stack.png)

## Author
[Ayush Jain](https://github.com/Ayushjain2205)