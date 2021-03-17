#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open('test_image.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "Amazing Python Scripts"

font = ImageFont.truetype('arial.ttf', 60 )
textwidth, textheight = draw.textsize(text, font )

# calculate the x,y coordinates of the text
margin = 30
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font )
im.show()

#Save watermarked image
im.save('New_test_image.png')

