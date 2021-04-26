from pdf2docx import Converter

pdf_file = 'sample.pdf'
docx_file = 'sample.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()