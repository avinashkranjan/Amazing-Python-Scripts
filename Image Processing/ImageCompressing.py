# -*- coding: utf-8 -*-

# Python Imaging Library PIL
from PIL import Image as ig

#open the image from directory , in my case its in same directory
img=ig.open("default.jpg")

#Apply the compressing
img.save("Compressed.jpg",optimize=True,quality=30)


print("Done!")