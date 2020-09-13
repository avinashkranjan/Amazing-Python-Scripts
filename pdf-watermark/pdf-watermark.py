from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileReader


ori_pdf = PdfFileReader('inputfile.pdf')
mark = PdfFileReader('watermark2.pdf')


watermark = mark.getPage(0)
original_pdf = ori_pdf.getPage(0)

ori_page_count = ori_pdf.getNumPages()

output = open('finalfile.pdf','wb')
final = PdfFileWriter()

for i in range(ori_page_count):
    each_page = ori_pdf.getPage(i)
    each_page.mergePage(watermark)
    final.addPage(each_page)


with output as page:
    final.write(page)

output.close()







