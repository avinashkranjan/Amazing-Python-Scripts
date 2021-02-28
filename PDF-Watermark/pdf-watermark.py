from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileReader

input_File = input(
    "Enter File Name You want to add Watermark too[Include .pdf extension]: ")
watermark = input("Enter Watermark File Name [Include .pdf extension]: ")

ori_pdf = PdfFileReader(input_File)
mark = PdfFileReader(watermark)

watermark = mark.getPage(0)
original_pdf = ori_pdf.getPage(0)

ori_page_count = ori_pdf.getNumPages()

output = open('watermarked.pdf', 'wb')
final = PdfFileWriter()

for i in range(ori_page_count):
    each_page = ori_pdf.getPage(i)
    each_page.mergePage(watermark)
    final.addPage(each_page)

with output as page:
    final.write(page)

output.close()
