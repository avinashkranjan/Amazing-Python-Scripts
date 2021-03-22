import os
import pdftotext


pdf_path = input("Enter the path of the pdf file : ")

assert os.path.exists(pdf_path), "this pdf file doesn't exist"

with open(f"./PDF2text/pages/{i}.txt", "w") as f:
    f.write(page)

for i, page in enumerate(pdf_pages):
    print('Page {}'.format(i))
    print(page)
    print('*'*100)
