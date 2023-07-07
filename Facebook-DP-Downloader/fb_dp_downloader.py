"""
    Facebook-DP-Downloader
        Download the profile picture of any public profile on Facebook
        by just having it's Facebook id 
    
"""

import os
import requests

url = "https://graph.facebook.com/{}/picture?type=large"

""" This url is the url provided by the Facebook graph api
which helps to get to the profile picture of the corresponding Facebook id 
{}==Facebook id 
Facebook id  denotes the unique user id of the Facebook profile
whose profile we are requesting
"""

path = os.getcwd()
# get the path of the current working directory

if not "fb_dps" in os.listdir(path):
    os.mkdir("fb_dps")

"""checks if the folder exists in the current working directory.
If it does not exist, then it gets created
"""

fbid = int(input("Enter the Facebook-id to download it's profile picture: "))
# the number should be a valid Facebook user id

try:
    result = requests.get(url.format(fbid))
    with open("fb_dps/{}_img.jpg".format(fbid), "wb") as file:
        file.write(result.content)

except:
    print("There was some error")
