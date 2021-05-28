from bs4 import BeautifulSoup
import requests
import pandas
import smtplib
import csv
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# to get the html code
response = requests.get("https://open.spotify.com/playlist/37i9dQZF1DX5KpP2LN299J")

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all(name="span", class_="track-name")
song_names = [song.getText() for song in song_names_spans]
hyperlinks = soup.find_all(name="meta", property="music:song")
song_links = [song.get("content") for song in hyperlinks]

my_dict = {"Song Name": song_names,
           "Song Link": song_links, }

data = pandas.DataFrame(my_dict)
data.to_csv("new_data.csv", index=False)
text = """
Hello, Friend.

Hope you enjoy this playlist:

{table}

Regards

"""

html = """
<html><body><p>Hello, Friend.</p>
<p>Hope you enjoy this playlist:</p>
{table}
<p>Regards</p>
</body></html>
"""

with open('new_data.csv', encoding='UTF-8') as input_file:
    reader = csv.reader(input_file)
    data = list(reader)
# to tabulate the data
text = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
html = html.format(table=tabulate(data, headers="firstrow", tablefmt="html"))

message = MIMEMultipart(
    "alternative", None, [MIMEText(text), MIMEText(html, 'html')])

# to send emails
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user="sender_address", password="sender_password")
    connection.sendmail(from_addr="sender_address", to_addrs="receiver_address", msg=message.as_string())
