# -*- coding: utf-8 -*-

#Flipping the image
from PIL import Image

#opening the image
img = Image.open('default.jpg')

#transpose of the matrix
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)

#save it in a new file

transposed_img.save("Corrected.png")

print("Done!")
