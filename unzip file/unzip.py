# importing required modules 
from zipfile import ZipFile 

# specifying the zip file name 
file_name = "Enter your zip file here"

# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
	# printing all the contents of the zip file 
	zip.printdir() 

	# extracting all the files 
	print('Extracting all the files now...') 
	zip.extractall() 
	print('Done!') 
    