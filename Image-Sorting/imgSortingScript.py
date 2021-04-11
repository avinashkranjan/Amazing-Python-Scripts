#cv2 is an Image processing library 		

import cv2
#for os manipulation
import os,glob	 

#Initializing counts for each resolution category 
im_4k = 0		
im_1080 = 0 
im_720 = 0 

#Creating directories for each resolution type
os.system("mkdir 4K")	 
os.system("mkdir 1080p") 
os.system("mkdir 720p") 
 #Selecting images one by one 
for image in glob.glob('*.jpg'):	
	print(image)
	#Reading the image 
	img = cv2.imread(image)
	#getting the image resolution 
	height, width, channel = img.shape
	#Comparing image resolutions and grouping them accordingly to move to folders
	if(width>=3840 and height>=2160):	 
		os.system("move "+image+" 4K") 
		im_4k = im_4k+1 
		continue 
	if(width>=1920 and height>=1080): 
		os.system("move "+image+" 1080p") 
		im_1080 = im_1080+1 
		continue 
	if(width>=1280 and height>=720): 
		os.system("move "+image+" 720p") 
		im_720 = im_720+1 
		continue
#displaying the counts for each type
print(im_4k," 4K images moved to 4K folder")	
print(im_1080," 1080p images moved to 1080p folder")	 
print(im_720," 720p images moved to 720p folder")
