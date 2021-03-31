import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

img = input(r"Enter image: ")
target = Image.open(img)
text = pytesseract.image_to_string(target, config='')

with open(f"./Imagetospeech/Text/text.txt",'w') as f:
    f.write(text)

    

