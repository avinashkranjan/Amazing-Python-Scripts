import pytesseract
from PIL import Image
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('4.jpg')

value = pytesseract.image_to_string(img)

print(value)

mytext = value
language = 'en'

output = gTTS(text=mytext, lang=language, slow=True)
output.save('output.mp3')

os.system("start output.mp3")