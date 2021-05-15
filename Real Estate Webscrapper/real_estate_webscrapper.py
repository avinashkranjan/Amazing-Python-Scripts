import requests
from bs4 import BeautifulSoup
import pandas


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

r=requests.get("https://www.magicbricks.com/ready-to-move-flats-in-new-delhi-pppfs", headers=headers)
c=r.content
soup=BeautifulSoup(c,"html.parser")


l=[]


all=soup.find_all("div",{"class":"flex relative clearfix m-srp-card__container"})
for item in all:
    d={}
    try:
        Price=item.find("div",{"class":"m-srp-card__price"}).text.replace("\n","").replace(" ","").replace("₹","")
        p=Price.split()
        d["Price"]=p[0]

    except:
        Price=item.find("span",{"class":"luxury-srp-card__price"}).text.replace("\n","").replace(" ","").replace("₹","")
        p=Price.split()
        d["Price"]=p[0]
       

    try:
        Pricepersqft=item.find("div",{"class":"m-srp-card__area"}).text.replace("₹","")
        pr=Pricepersqft.split()
        d["Pricepersqft"]=pr[0]

    except:
        try:
            Pricepersqft=item.find("span",{"class":"luxury-srp-card__sqft"}).text.replace("\n","").replace(" ","").replace("₹","")
            pr=Pricepersqft.split()
            d["Pricepersqft"]=pr[0]
        except:
            d["Pricepersqft"]=None

    try:
        d["Size"]=item.find("span",{"class":"m-srp-card__title__bhk"}).text.replace("\n","").strip()[0:5]
    except:
        d["Size"]=None

    
    title=item.find("span",{"class":"m-srp-card__title"})
    
    words=(title.text.replace("in","")).split()
        
    for i in range(len(words)):
        if words[i]=="sale" or words[i]=="Sale":            
            break
    s=""
    for word in range(i+1,len(words)):
        s=s+words[word]+" "

    d["Address"]=s

    try:
        d["Carpet Area"]=item.find("div",{"class":"m-srp-card__summary__info"}).text
    except:
        d["Carpet Area"]=item.find("div",{"class":"luxury-srp-card__area__value"}).text
    
    
    l.append(d)
    
    

df=pandas.DataFrame(l)
df.to_csv("output2.csv")
