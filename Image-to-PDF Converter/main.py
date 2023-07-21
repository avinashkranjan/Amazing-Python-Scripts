import os
import img2pdf

# path tot the directory which contains the files
path = ""

images = [imgs for imgs in os.listdir(path) if imgs.endswith(
    ('.jpg', '.jpeg', '.png', '.gif'))]

images.sort()

# List to store image bytes of images present in the directory
images_bytes = list()

# converting all the images to image-bytes and appending them to a list for further processing
for i in images:
    with open(os.path.join(path, i), "rb") as im:
        images_bytes.append(im.read())

# To convert image bytes to pdf-bytes

pdf_bytes = img2pdf.convert(images_bytes)

with open('Output.pdf', "wb") as pdfFile:
    pdfFile.write(pdf_bytes)
