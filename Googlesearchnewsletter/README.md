# GoogleSearchNewsletter

## What this program does 
- Performs google search of topic stated in config file
- Go to news tab of google search results
- Extract each news heading and link from first search results page
- Save search results to file
- Read file to send email to address in config file

## How to use

### 1. Setup Python and modules

Python and the following modules must be installed on the computer running this script.

Install Python and pip:
```
sudo apt-get install python
sudo apt-get install pip
```

Install selenium:
```
pip install -r requirements.txt
```

### 2. Download browser and driver

You need to have either Firefox or Chrome installed. You also need the corresponding driver for the browser.

For Firefox download geckodriver:
https://github.com/mozilla/geckodriver/releases

For Chrome download chromedriver:
https://chromedriver.chromium.org/downloads


### 3. Configure config.ini

Example configuration:
```
[your_settings]
driver = geckodriver
search_topic = Nintendo news
email_subject = My newsletter for Nintendo
email_smtp = smtp.live.com
sender_email_address = sendingemail@live.com
email_password = yourpassword
receiver_email_address = receiveremail@live.com
```

Note: 
- The "email_smtp" is the mail server of the sender. 
- See [this link](https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html) to find a list of smtp servers and insert the correct one for your email address.


### 4. Run program

```
python google-search-newsletter.py
```

You should receive an email in the receiver address containing the news headlines and links.

### 5. Setup running schedule using Crontab Linux utility

Schedule the time and frequency to run this script. See the [Crontab man page](https://linux.die.net/man/5/crontab) for more info.

Open the crontab file for editing. Run on command line:
```
crontab -e
```

Add the following to the end of the crontab file. This example will run the script everyday at 07:05am. Edit according to your needs.
```
# needed if headless=false
DISPLAY=:0

# at 07:05am go to directory of script and run. log output and potential errors to file 'crontab.log'
05 07 * * * cd /pathtoscript/ && python google-search-newsletter.py > crontab.log 2>&1
```
Save the crontab file and you will see:
```
crontab: installing new crontab
```
The script should now run everyday at 07:05am.


### Tips for developers

The browsers run in headless mode which means the browser GUI is not opened while running the program.
If you want the GUI to open while running do the following:
- If using geckodriver change `firefox_options.headless = True` to `firefox_options.headless = False`
- If using chromedriver change `chrome_options.add_argument('--headless')` to `chrome_options.add_argument('--None')`