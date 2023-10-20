#A simple python program to scrap and download images form web url

from bs4 import *
import requests
import os

#Creating the folder
def folder_create(images):
    try:
        folder_name = input("[+] Enter folder name: ")
        #creating folder
        os.mkdir(folder_name)
    except:
        print("A folder exists with this name!")
        folder_create()
        
    #start downloading images
    download_images(images, folder_name)
    
#Download all images from that url
def download_images(images, folder_name):
    count = 0
    print(f"[+] Total {len(images)} images found!")
    user_ch = input("[+] Do you want to continue (y/n)?")
    if user_ch == 'y':
        user_img_ch = int(input("How many images do you want to download (default 0 -> all): "))
        if user_img_ch == 0:
            if len(images) != 0:
                for i, image in enumerate(images):
                    try:
                        image_link = image["data-srcset"]
                    except:
                        try:
                            image_link = image["data-src"]
                        except:
                            try:
                                image_link = image["data-fallback-src"]
                            except:
                                try:
                                    image_link = image["src"]
                                except:
                                    pass
                                
                    try:
                        r = requests.get(image_link).content
                        try:
                            r = str(r, 'utf-8')
                        except UnicodeDecodeError:
                            with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
                                f.write(r)
                                
                            count += 1
                            
                    except:
                        pass
            
        if user_img_ch != 0 and user_img_ch <= len(images):
            if len(images) != 0:
                count_img = 0
                for i, image in enumerate(images):
                    try:
                        image_link = image["data-srcset"]
                    except:
                        try:
                            image_link = image["data-src"]
                        except:
                            try:
                                image_link = image["data-fallback-src"]
                            except:
                                try:
                                    image_link = image["src"]
                                except:
                                    pass
                                
                    try:
                        r = requests.get(image_link).content
                        try:
                            r = str(r, 'utf-8')
                        except UnicodeDecodeError:
                            with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
                                f.write(r)
                            
                    except:
                        pass
                        
                    count_img += 1
                    if(count_img == user_img_ch):
                        break
                 
        if count == len(images):
                print("All Images Downloaded!")
                
        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")
    else:
        print("[+] Thanks for visiting! Come back again.")
        
def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img')
    folder_create(images)
    
url = input("[+] Enter url: ")
main(url)
                                