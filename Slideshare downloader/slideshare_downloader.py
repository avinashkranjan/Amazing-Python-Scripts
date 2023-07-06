# slideshare downloader
from bs4 import BeautifulSoup
import requests
import itertools
import threading
import time
import sys
import urllib.request
import img2pdf
import os

task = False
process = "getting the slides "


def animate():
    for i in itertools.cycle(['|', '/', '-', '\\']):
        if task:
            break
        sys.stdout.write('\r' + process + i)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)


def get_image_list(url):
    code = requests.get(url)
    soup = BeautifulSoup(code.text, "html.parser")
    print(f"Title: {soup.title.get_text()}")
    imgs = soup.find_all("img")
    img_urls = []
    for temp_url in imgs:
        temp_link = temp_url.get("data-full")
        if temp_link is not None:
            img_urls.append(temp_link)
    return img_urls


def slides_capture(links):
    pg_no = 1
    os.makedirs(".cache", exist_ok=True)
    all_slides = []
    for link in links:
        print(f"fetching (slide{pg_no})")
        file = f"slide{pg_no}.jpg"
        urllib.request.urlretrieve(link, ".cache/"+file)
        all_slides.append(".cache/"+file)
        pg_no = pg_no+1
    return all_slides


def combine(all_slides):
    output_name = input(
        "\n\n Enter the name for pdf file of slides (without extension):")
    with open(output_name+".pdf", "wb") as f:
        f.write(img2pdf.convert(all_slides))
    for i in all_slides:
        os.remove(i)


print("Enter the URL of slides below:")
main_link = input()
t.start()
all_urls = get_image_list(main_link)
if len(all_urls) == 0:
    print("Sorry no downloadable slides found")
    task = True
else:
    print(f"Total no of Slides found: {len(all_urls)}")
    all_slides = slides_capture(all_urls)
    task = True
    combine(all_slides)
print("All set your file is ready")
