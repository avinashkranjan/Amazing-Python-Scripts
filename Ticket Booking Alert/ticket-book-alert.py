#!/usr/bin/env python3.7
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re
import smtplib
import time

url = "https://in.bookmyshow.com/buytickets/<movie_name>-<city>/"+
+"movie-<city-code>-<refnumber>-MT/"
# replace above with the movie name, city, city code
"""example of URL:
https://in.bookmyshow.com/buytickets/gadar-2-the-katha-continues
-bengaluru/movie-bang-ET00338629-MT/20230811"""
date = "<YYYYMMDD>"  # eg: 20230101
site = url + date
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) 
AppleWebKit/537.11 (KHTML, like Gecko) 
Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
venue = 'CPCL'  # found by inspecting the element data-id for venue
show = '9:30 PM'  # replace it with your preferred show timing
delay = 600   # timegap in seconds between 2 script runs

to = 'xyz@gmail.com'  # relace with your email id on which you want to get the alert
# Please add your username and password below, and make sure you
# toggle allow less secure apps to on
# https://myaccount.google.com/lesssecureapps?pli=1
gmail_user = 'no_reply@gmail.com'
gmail_pwd = '123et435!'
subject = 'Tickets are now available'
text = 'Tickets are now available for '+show+' show at the venue'+venue


def send_mail():
    """Function to send mail"""
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From:' + gmail_user
    header = header + '\n' + 'Subject:' + subject + '\n'
    messg = header + '\n' + text + '\n\n'
    smtpserver.sendmail(gmail_user, to, messg)
    smtpserver.close()


req = urllib.request.Request(site, headers=hdr)
try:
    # open the url
    with urllib.request.urlopen(req) as page:
        content = page.read()
        soup = BeautifulSoup(content, 'html.parser')
        soup2 = soup.find_all('div', {'data-online': 'Y'})
        line = str(soup2)
        soup3 = BeautifulSoup(line, 'html.parser')
        # Find all 'a' elements with 'data-venue-code' attr
        soup4 = soup3.find_all('a', {'data-venue-code': venue})
        line1 = str(soup4)
        soup5 = BeautifulSoup(line1, 'html.parser')
        # Find all 'a' elements with 'data-display-showtime' attr
        soup6 = soup3.find_all('a', {'data-display-showtime': show})
        line2 = str(soup6)
        # Use regular expression to find data-availability="A" in the modified HTML
        result = re.findall(r'data-availability="A"', line2)
        if len(result) > 0:
            print("Ticket Available")
            send_mail()
        else:
            print("Not available yet")

except urllib.error.URLError as e:
    print("Error occurred:", e)

time.sleep(delay)  # adjust the sleep timing by changing the delay variable as required
