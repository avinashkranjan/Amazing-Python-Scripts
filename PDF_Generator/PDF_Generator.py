import os
import img2pdf
from pdf2image import convert_from_path

# *.jpg to output_filename.pdf convertor
with open("output_filename.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir(".") if i.endswith(".jpg")]))

# file.pdf to output_images_folder_name/page_no.jpg convertor
pages = convert_from_path("input_filename.pdf", 500)
page_no = 0
for page in pages:
    # output_images_folder_name = folder needs to be created manually to store all images
    pages[page_no].save(
        "output_images_folder_name/output_page_{}.jpg".format(page_no + 1), "JPEG"
    )
    page_no += 1