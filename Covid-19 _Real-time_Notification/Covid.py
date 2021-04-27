from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notify_user(title, message):
    notification.notify(
    title = title,
    message = message,
    app_icon = "./Covid-19_Real-time_Notification/Notify_icon.ico" ,
    timeout = 3)
    
def getInfo(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
        states = list(map(str,input("Enter the name of states:").split(",")))
        
        while True:
            HtmlData = getInfo('https://www.medtalks.in/live-corona-counter-india')
            soup = BeautifulSoup(HtmlData, 'html.parser')
        
            myData = ""
            for tr in soup.find('tbody').find_all('tr'):
                myData += tr.get_text()
            myData = myData[1:]
            itemList = myData.split("\n\n")
            for item in itemList[:-2]:
                dataList = item.split('\n')
            
                if dataList[0] in states:
                    print(dataList)
                    nTitle = 'Cases of Covid-19'
                    nText = f"State: {dataList[0]}: Total: {dataList[1]}\n Active: {dataList[2]}\n Death: {dataList[3]}"
                    notify_user(nTitle, nText)
                    time.sleep(2)
            time.sleep(3600)