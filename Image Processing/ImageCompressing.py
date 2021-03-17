# -*- coding: utf-8 -*-

# Python Imaging Library PIL
from PIL import Image as ig

#open the image from directory , in my case its in same directory
img=ig.open("Home/Pictures/default.jpg") # Here we have to provide complete address of image from file which contains your py file 

#Apply the compressing
img.save("Compressed.jpg",optimize=True,quality=30)


print("Done!")
