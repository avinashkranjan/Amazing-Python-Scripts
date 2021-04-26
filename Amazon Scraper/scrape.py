#libraries used
import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

def scraper():

    #the csv file deceared
    f=open('amazon_report.csv','w',newline='',encoding='utf-8')
    data=csv.writer(f)
    main = []
    headers = (
        {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Accept-language': 'en-US,en;q=0.5'
        }      )
    preq=requests.get(url_name,headers)
    soup=BeautifulSoup(preq.content,features="html.parser")

    #scraping the details
    product_author_name=[i.text for i in soup.findAll("a",{"class":"a-size-base a-link-normal"})]
    data.writerow(product_author_name)
    main.append(product_author_name)
    product_rating=[ratings.text for ratings in soup.findAll("span",{"class":"a-size-base"})]
    data.writerow(product_rating)
    main.append(product_rating)


    #creating the DataFrame
    df=pd.DataFrame(data=main)
    df.to_csv('amazon_report.csv',index=False,header=False)


    #completion message
    print('Done')
    time.sleep(time_interval)

if __name__ == '__main__':

    #inputs for the programm
    take_max_run_time=int(input("Enter the time in 'SECOND' you want the scraper to work for the upadtion purpose:- "))
    time_interval=int(input("Enter the time you want to hold the scraper : "))
    url_name = input('Enter the link: ')


    #module thats makes it run for the desired time
    end_time=time.time() + take_max_run_time
    while time.time() < end_time:
        scraper()
