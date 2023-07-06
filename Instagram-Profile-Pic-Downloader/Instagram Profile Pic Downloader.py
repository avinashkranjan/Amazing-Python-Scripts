# It will download image in hd

import requests
from bs4 import BeautifulSoup as soup

if __name__ == '__main__':
    uname = str(input("Enter the username : "))
    new = requests.get('https://www.instadp.com/fullsize/{}'.format(uname))
    imgsoup = soup(new.content, 'lxml')
    imglink = imgsoup.find('img', {'class': 'picture'})['src']
    imgfind = requests.get(imglink)
    photo = open('photo.png', 'wb')
    photo.write(imgfind.content)
    photo.close()
