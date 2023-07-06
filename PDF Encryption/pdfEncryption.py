# PyPDF2 helps to read, write and many other functionalities with PDF's
# Install PyPDF2 if not in your system.
# Use `pip install PyPDF2` command to install the package from pip installer.
from PyPDF2 import PdfFileWriter, PdfFileReader

print("The file should be in same FOLDER as this script")

pdf_File_Name = input("Enter EXACT name of the PDF in this FOLDER: ")
pdf_File = pdf_File_Name + ".pdf"

# Reading the pdf
pdf = PdfFileReader(pdf_File)

# Object for writing the file
write_Obj = PdfFileWriter()

# Getting the number of pages and writing each page in the writer object
for i in range(pdf.getNumPages()):
    page = pdf.getPage(i)
    write_Obj.addPage(page)

# Encrypting by the password
owner_Password = input("Enter Password for OWNER: ")
user_Password = input("Enter Password for USER: ")
write_Obj.encrypt(user_pwd=user_Password,
                  owner_pwd=owner_Password,
                  use_128bit=True)

# Naming and creating the encrypted PDF
new_PDF_Name_Input = input("Enter new ENCRYPTED PDF name: ")
new_PDF_Name = new_PDF_Name_Input + '.pdf'
encrypted_PDF = open(new_PDF_Name, 'wb')
write_Obj.write(encrypted_PDF)
