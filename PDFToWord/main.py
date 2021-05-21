from pdf2docx import Converter
import os 
import sys

# Take PDF's path as input 
pdf = input("Enter the path to your file: ")
assert os.path.exists(pdf), "File not found at, "+str(pdf)
f = open(pdf,'r+')

#Ask for custom name for the word doc
doc_name_choice = input("Do you want to give a custom name to your file ?(Y/N)")

if(doc_name_choice == 'Y' or doc_name_choice == 'y'):
    # User input
    doc_name = input("Enter the custom name : ")+".docx"
    
else:
    # Use the same name as pdf
    # Get the file name from the path provided by the user
    pdf_name = os.path.basename(pdf)
    # Get the name without the extension .pdf
    doc_name =  os.path.splitext(pdf_name)[0] + ".docx"

    
# Convert PDF to Word
cv = Converter(pdf)

#Path to the directory
path = os.path.dirname(pdf)

cv.convert(os.path.join(path, "", doc_name) , start=0, end=None)
print("Word doc created!")
cv.close()