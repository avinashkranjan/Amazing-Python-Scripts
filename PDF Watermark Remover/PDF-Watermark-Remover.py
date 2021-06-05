from skimage import io
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
import numpy as np
import os
from PIL import Image
from fpdf import FPDF
import shutil

pdfFile = input('PDF file location: ') 
dirname = os.path.dirname(os.path.normpath(pdfFile))
outputFile = os.path.basename(pdfFile)
outputFile = os.path.splitext(outputFile)[0]
pdf_reader = PdfFileReader(pdfFile)
pages = pdf_reader.getNumPages()
rang = int(pages) + 1

# Select the pixel from the extracted images of pdf pages
def select_pixel(r,g,b):
    if r > 120 and r < 254 and g > 120 and g < 254 and b > 120 and b < 254:
        return True
    else:
        return False

# Handling of images for removing the watermark
def handle(imgs):
    for  i in range(imgs.shape[0]):
        for j in range(imgs.shape[1]):
            if select_pixel(imgs[i][j][0],imgs[i][j][1],imgs[i][j][2]):
                imgs[i][j][0] =  imgs[i][j][1] = imgs[i][j][2] = 255
    return imgs

images = convert_from_path(pdfFile)

try:
    os.mkdir(dirname + '\img')
except FileExistsError:
    print('Folder exist')
index = 0
for img in images:
    index += 1
    img = np.array(img)
    print(img.shape)
    img = handle(img)
    io.imsave(dirname + '\img\img' + str(index) + '.jpg', img)
    print(index)

# Merging images to a sigle PDF
pdf = FPDF()
sdir = dirname + "img/"
w,h = 0,0

for i in range(1, rang):
    fname = sdir + "img%.0d.jpg" % i
    if os.path.exists(fname):
        if i == 1:
            cover = Image.open(fname)
            w,h = cover.size
            pdf = FPDF(unit = "pt", format = [w,h])
        image = fname
        pdf.add_page()
        pdf.image(image, 0, 0, w, h)
    else:
        print("File not found:", fname)
    # print("processed %d" % i)
pdf.output(dirname + outputFile + '_rw.pdf', "F")
print("done")