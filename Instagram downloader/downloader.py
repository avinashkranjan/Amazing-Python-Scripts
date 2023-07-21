# import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
from bs4 import BeautifulSoup as bs
import requests
import os


# get instagram account credentials
username = input('Enter Your User Name ')
password = input('Enter Your Password ')

# assign URL
url = 'https://instagram.com/' + \
    input('Enter User Name Of User For Downloading Posts ')

# Get URL path


def path():
    global chrome
    # starts a new chrome session
    # add path if required
    chrome = webdriver.Chrome()

# Extract URL


def url_name(url):
    # the web page opens up
    chrome.get(url)

    # webdriver will wait for 4 sec before throwing a
    # NoSuchElement exception so that the element
    # is detected and not skipped.
    time.sleep(4)

# Login to access post


def login(username, your_password):
    log_but = chrome.find_element_by_class_name("L3NKy")
    time.sleep(2)
    log_but.click()
    time.sleep(4)
    # finds the username box
    usern = chrome.find_element_by_name("username")
    # sends the entered username
    usern.send_keys(username)

    # finds the password box
    passw = chrome.find_element_by_name("password")

    # sends the entered password
    passw.send_keys(your_password)

    # sends the enter key
    passw.send_keys(Keys.RETURN)

    time.sleep(5.5)

    # Find Not Now Button
    notn = chrome.find_element_by_class_name("yWX7d")

    notn.click()
    time.sleep(3)

# Function to get content of first post


def first_post():
    pic = chrome.find_element_by_class_name("kIKUG").click()
    time.sleep(2)

# Function to get next post


def next_post():
    try:
        nex = chrome.find_element_by_class_name(
            "coreSpriteRightPaginationArrow")
        return nex
    except selenium.common.exceptions.NoSuchElementException:
        return 0

# Download contenet of all posts


def download_allposts():

    # open First Post
    first_post()

    user_name = url.split('/')[-1]

    # check if folder corresponding to user name exist or not
    if (os.path.isdir(user_name) == False):

        # Create folder
        os.mkdir(user_name)

    # Check if Posts contains multiple images or videos
    multiple_images = nested_check()

    if multiple_images:
        nescheck = multiple_images
        count_img = 0

        while nescheck:
            elem_img = chrome.find_element_by_class_name('rQDP3')

            # Function to save nested images
            save_multiple(user_name+'/'+'content1.'+str(count_img), elem_img)
            count_img += 1
            nescheck.click()
            nescheck = nested_check()

        # pass last_img_flag True
        save_multiple(user_name+'/'+'content1.' +
                                str(count_img), elem_img, last_img_flag=1)
    else:
        save_content('_97aPb', user_name+'/'+'content1')
    c = 2

    while (True):
        next_el = next_post()

        if next_el != False:
            next_el.click()
            time.sleep(1.3)

            try:
                multiple_images = nested_check()

                if multiple_images:
                    nescheck = multiple_images
                    count_img = 0

                    while nescheck:
                        elem_img = chrome.find_element_by_class_name('rQDP3')
                        save_multiple(user_name+'/'+'content' +
                                                str(c)+'.'+str(count_img), elem_img)
                        count_img += 1
                        nescheck.click()
                        nescheck = nested_check()
                    save_multiple(user_name+'/'+'content'+str(c) +
                                            '.'+str(count_img), elem_img, 1)
                else:
                    save_content('_97aPb', user_name+'/'+'content'+str(c))

            except selenium.common.exceptions.NoSuchElementException:
                print("finished")
                return

        else:
            break

        c += 1

# Function to save content of the current post


def save_content(class_name, img_name):
    time.sleep(0.5)

    try:
        pic = chrome.find_element_by_class_name(class_name)

    except selenium.common.exceptions.NoSuchElementException:
        print("Either This user has no images or you haven't followed this user or something went wrong")
        return

    html = pic.get_attribute('innerHTML')
    soup = bs(html, 'html.parser')
    link = soup.find('video')

    if link:
        link = link['src']

    else:
        link = soup.find('img')['src']
    response = requests.get(link)

    with open(img_name, 'wb') as f:
        f.write(response.content)
    time.sleep(0.9)

# Function to save multiple posts


def save_multiple(img_name, elem, last_img_flag=False):
    time.sleep(1)
    l = elem.get_attribute('innerHTML')
    html = bs(l, 'html.parser')
    biglist = html.find_all('ul')
    biglist = biglist[0]
    list_images = biglist.find_all('li')

    if last_img_flag:
        user_image = list_images[-1]

    else:
        user_image = list_images[(len(list_images)//2)]
    video = user_image.find('video')

    if video:
        link = video['src']

    else:
        link = user_image.find('img')['src']
    response = requests.get(link)

    with open(img_name, 'wb') as f:
        f.write(response.content)

# Function to check if the post is nested


def nested_check():

    try:
        time.sleep(1)
        nes_nex = chrome.find_element_by_class_name('coreSpriteRightChevron ')
        return nes_nex

    except selenium.common.exceptions.NoSuchElementException:
        return 0


# Driver Code
path()
time.sleep(1)

url_name(url)

login(username, password)

download_allposts()

chrome.close()
