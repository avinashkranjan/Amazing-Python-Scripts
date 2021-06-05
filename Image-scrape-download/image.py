# Import Module
from tkinter import *
from tkhtmlview import HTMLLabel
from tkinter import ttk
from tkinter import font as tkFont
import requests
from bs4 import BeautifulSoup
import urllib3
import shutil

# Function to save image to the users file system
def saveImage():
    file_name = search_box.get().replace(" ","")
    image_file = getImage()
    http = urllib3.PoolManager()
    with open(file_name, 'wb') as out:
        r = http.request('GET', image_file, preload_content=False)
        shutil.copyfileobj(r, out)

# Function to scrape image source from bing
def getImage():
    search = search_box.get()
    url = "https://www.bing.com/images/search?q={}".format(search.replace(' ','?'))
    page = requests.get(url)

    # Start scraping resultant html data
    soup = BeautifulSoup(page.content, 'html.parser')
    images_div = soup.find('div',{'id':'mmComponent_images_2'})
    images_ul = images_div.find('ul')

    image = images_ul.find("li")
    link = image.find('img').get('src')

    return link

# Function to show image in the GUI
def showImage():
    link = getImage()
    str_value = '<img src="{}">'.format(link)
    my_label.set_html(str_value)


# Create tkinter Object
root = Tk()
  
# Set Geomerty of window
root.geometry("400x500")
root.title("Image viewer and downloader")

# Set styles
style = ttk.Style()
style.theme_use('alt')
style.map('my.TButton', background=[('active','white')])
style.configure('my.TButton', font=('Helvetica', 16, 'bold'))
style.configure('my.TButton', background='white')
style.configure('my.TButton', foreground='orange')
style.configure('my.TFrame', background='white')  

# Add labels and buttons
my_label = HTMLLabel(root)
  
search_box = Entry(root, font=("Helvetica 15"), bd = 2, width=60)
search_box.pack(side = TOP, pady=5, padx=15, ipadx=5)

search_btn = ttk.Button(text="Scrape Image!",command=showImage,style='my.TButton')
search_btn.pack(side=TOP)

save_btn = ttk.Button(text="Download Image!",command=saveImage,style='my.TButton')
save_btn.pack(side=TOP)

my_label.pack(pady=20, padx=20)
# Execute Tkinter
root.mainloop()
