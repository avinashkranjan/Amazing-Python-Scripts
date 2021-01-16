#run pip install pillow on terminal
from PIL import Image #importing required libraries
from PIL import ImageFont
from PIL import ImageDraw

img = Image.new('RGB', (600, 400), color = 'red')#here we are creating an image which is a simple rectangle of 600*400 dimension but instead we can also have an image 
img.save('pil_red.png')#if we want to add text on the image we have already we do not need to write these two lines of code 
font = ImageFont.truetype("times-ro.ttf", 24)#we have downloaded times new roman font from internet as described in readme file 
img = Image.new('RGB', (600, 400), color = 'red')

draw = ImageDraw.Draw(img)
draw.text((300, 200),"Hello world !",(0,0,0),font=font)#we can choose our font accordingly and the text on the image

img.save('pil.png')#a new image is saved ,which has text on image .