import requests
from bs4 import BeautifulSoup
import pandas

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

r=requests.get("http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers=headers)
c=r.content
soup=BeautifulSoup(c,"html.parser")
page_nr=soup.find_all("a",{"class":"Page"})[-1].text

l=[]

base_url="http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="

for page in range(0,int(page_nr)*10,10):
    
    r=requests.get(base_url+str(page)+".html", headers=headers)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        d={}
        d["Price"]=item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ","")
        d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text.replace("\n","")
        try:
            d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text.replace("\n","")
        except:
            d["Locality"]=None
        
        try:
            d["Beds"]=item.find("span",{"class","infoBed"}).find("b").text
        except:
            d["Beds"]=None

        try:
            d["Area"]=item.find("span",{"class","infoSqFt"}).find("b").text
            
        except:

            d["Area"]=None

        try:
            d["Full Bath"]=item.find("span",{"class","infoValueFullBath"}).find("b").text
        except:
            d["Full Bath"]=None

        try:

            d["Half Baths"]=item.find("span",{"class","infovalueHalfBath"}).find("b").text
        except:
            d["Half Baths"]=None

        for column_group in item.find_all("div",{"class":"columnGroup"}):
            for feature_group,feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=feature_name.text
        
        l.append(d)

        print(" ")

df=pandas.DataFrame(l)
df.to_csv("output.csv")


