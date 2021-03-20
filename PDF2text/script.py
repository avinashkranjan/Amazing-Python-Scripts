import os
import pdftotext


pdf_path = input("Enter the path of the pdf file : ")

assert os.path.exists(pdf_path), "this pdf file doesn't exist"

with open(pdf_path, 'rb') as f_r:
    pdf_pages = pdftotext.PDF(f_r)

for i, page in enumerate(pdf_pages):
    print('Page {}'.format(i))
    print(page)
    print('*'*100)
