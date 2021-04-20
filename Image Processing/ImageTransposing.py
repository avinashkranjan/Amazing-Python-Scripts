# -*- coding: utf-8 -*-

# Flipping the image
from PIL import Image

# opening the image
filePath = input("Enter the path of your Image : ")
img = Image.open(filePath)

# transpose of the matrix
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

# save it in a new file

transposed_img.save("Corrected.png")

print("Done!")
