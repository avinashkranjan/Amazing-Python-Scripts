# run pip install pillow on terminal
from PIL import Image  # importing required libraries
from PIL import ImageFont
from PIL import ImageDraw

# here we are creating an image which is a simple rectangle of 600*400 dimension but instead we can also have an image
img = Image.new('RGB', (600, 400), color='red')
# if we want to add text on the image we have already we do not need to write these two lines of code
img.save('pil_red.png')
# we have downloaded times new roman font from internet as described in readme file
font = ImageFont.truetype("times-ro.ttf", 24)
img = Image.new('RGB', (600, 400), color='red')

draw = ImageDraw.Draw(img)
# we can choose our font accordingly and the text on the image
draw.text((300, 200), "Hello world !", (0, 0, 0), font=font)

img.save('pil.png')  # a new image is saved ,which has text on image .
