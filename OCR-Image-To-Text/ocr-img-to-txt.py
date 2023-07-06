import pytesseract
from PIL import Image

# path to the Tessaract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def convert():
    img = Image.open(
        r"E:\Python-Programs\PythonProjects\OCR-Image-To-Text\Img-To-Convt\img.jpg"
    )
    text = pytesseract.image_to_string(img)
    print(text)


convert()
