# Python Script to auto fill Google Forms

This is a python script which can helps you to fillout the google form automatically by bot.

## Steps to make it run

1. Clone/Download this repository
```
git clone clone_path
```
2. Downlaod the required packages 
```
pip install -r requirements.txt
```

3. To run the script you need to use the following command
```
python app.py
```

4. To run this script you need to have selenium installed and you nedd to have geckodriver.
you can downlaod geckodriver from here: https://github.com/mozilla/geckodriver/releases
After downloading the geckodriver, need to set-path for that as shown below:
```
webdriver.Firefox(executable_path=
'D:\Selenium_RiponAlWasim\geckodriver-v0.18.0-win64\geckodriver.exe')
```
### working
1. You can add or delete the records in .csv file.
  ![Screenshot (589)](https://user-images.githubusercontent.com/61947484/103745563-b4aa3e00-5025-11eb-98cf-7d3c8834d657.png)
2. Intially the number of responses in the google-form will be null(no-entries):
 screenshot is attached below:
![Screenshot (590)](https://user-images.githubusercontent.com/61947484/103745668-e58a7300-5025-11eb-8c95-bc60d881b205.png)

3. After ruuning the script, the bot will automatically take the records from .csv file and it will will the form.
![Screenshot (591)](https://user-images.githubusercontent.com/61947484/103747825-3fd90300-5029-11eb-84aa-ef53c799f8ea.png)

you can check the working of the bot: 
https://user-images.githubusercontent.com/61947484/103747705-1029fb00-5029-11eb-8307-fcef2c8a3048.mp4