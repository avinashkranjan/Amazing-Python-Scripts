from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

URL = 'http://www.cricbuzz.com/cricket-match/live-scores'


def notify(title, score):
    # Function for Windows toast desktop notification
    toaster = ToastNotifier()
    # toaster.show_toast(score, "Get! Set! GO!", duration=5,icon_path='cricket.ico')
    toaster.show_toast("CRICKET LIVE SCORE",
                       score,
                       duration=30,
                       icon_path='ipl.ico')


while True:
    request = Request(URL, headers={'User-Agent': 'XYZ/3.0'})
    response = urlopen(request, timeout=20).read()
    data_content = response
    # print(data_content)

    # page = urlopen(URL)
    soup = BeautifulSoup(data_content, 'html.parser')

    update = []
    # print(soup)
    # print(soup.find_all('div',attrs={'class':'cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main'}))
    for score in soup.find_all(
            'div',
            attrs={
                'class':
                'cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main'
            }):
        # print(score)
        header = score.find('div',
                            attrs={'class': 'cb-col-100 cb-col cb-schdl'})
        header = header.text.strip()

        status = score.find('div',
                            attrs={'class': 'cb-scr-wll-chvrn cb-lv-scrs-col'})
        s = status.text.strip()

        notify(header, s)
        time.sleep(10)
