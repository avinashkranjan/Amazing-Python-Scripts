import requests
import urllib.request  # only import if you want to display meme in your local device
from PIL import Image  # only import if you want to display meme in your local device


### Main code###
# add /n to get required number of memes (where n is a number)
response = requests.get('https://meme-api.com/gimme')
meme = response.json()
meme_url = meme['url']  # if more than 1 meme accordingly change the code
##############

#### Code to open image####
# change to gif/jpeg,if you get gif/jpeg as a meme
urllib.request.urlretrieve(meme_url, "file.png")
img = Image.open("file.png")
img.show()
#######################
