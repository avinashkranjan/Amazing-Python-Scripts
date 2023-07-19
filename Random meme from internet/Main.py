import requests 
import urllib.request #only import if you want to display meme in your local device
from PIL import Image #only import if you want to display meme in your local device


###Main code###
response = requests.get('https://meme-api.com/gimme') # add /n to get required number of memes (where n is a number)
meme = response.json()
meme_url = meme['url'] # if more than 1 meme accordingly change the code
##############

####Code to open image####
urllib.request.urlretrieve(meme_url,"file.png") #change to gif/jpeg,if you get gif/jpeg as a meme 
img = Image.open("file.png")
img.show()
#######################                 