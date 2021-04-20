# -*- coding: utf-8 -*-

# Python Imaging Library PIL
from PIL import Image as ig

# Here we have to provide complete address of image from file which contains your py file
filePath = input("Enter the path of your Image : ")
img = ig.open(filePath)
# Apply the compressing
img.save("Compressed.jpg", optimize=True, quality=30)


print("Done!")
