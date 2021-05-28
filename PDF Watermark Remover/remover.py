from skimage import io
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
import numpy as np
import os
from PIL import Image
from fpdf import FPDF
import shutil

pdfFile = input('PDF file location: ')

outputFile = os.path.basename(pdfFile)
outputFile = os.path.splitext(outputFile)[0]
pdf_reader = PdfFileReader(pdfFile)
pages = pdf_reader.getNumPages()
rang = int(pages) + 1

def judge(x,y):
    temp = -(600.0/1575.0) * x
    if y > 1350 + temp and y < 1500 + temp:
        return True
    else:
        return False

def select_pixel(r,g,b):
    if (r == 208 and g == 208 and b == 208 ) or (r == 196 and g == 196 and b == 196) \
        or (r == 206 and g == 206 and b == 206 ):
        return True
    else:
        return False
def select_pixel2(r,g,b):
    if r > 175 and r < 250 and g > 175 and g < 250 and b > 175 and b < 250:
        return True
    else:
        return False
def handle(imgs):
    for  i in range(imgs.shape[0]):
        for j in range(imgs.shape[1]):
            if select_pixel2(imgs[i][j][0],imgs[i][j][1],imgs[i][j][2]):
                imgs[i][j][0] =  imgs[i][j][1] = imgs[i][j][2] = 255
    return imgs

images = convert_from_path(pdfFile)

try:
    os.mkdir('.\img')
except FileExistsError:
    print('Folder exist')
index = 0
for img in images:
    index += 1
    img = np.array(img)
    print(img.shape)
    img = handle(img)
    io.imsave('.\img\img'+str(index)+'.jpg', img)
    print(index)

pdf = FPDF()
sdir = "img/"
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
        pdf.image(image,0,0,w,h)
    else:
        print("File not found:", fname)
    # print("processed %d" % i)
pdf.output(outputFile+'_r.pdf', "F")
print("done")