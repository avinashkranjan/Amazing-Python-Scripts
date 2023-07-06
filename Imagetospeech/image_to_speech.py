import pytesseract
from PIL import Image
from gtts import gTTS
import os


pytesseract.pytesseract.tesseract_cmd = input(
    r'Enter the path for pytesseract: ')

img = input(r"Enter the path for image: ")
target = Image.open(img)
text = pytesseract.image_to_string(target, config='')

with open(f"./Imagetospeech/text.txt", 'w') as f:
    f.write(text)

file = open(r'./Imagetospeech/text.txt')
mytext = file.read().replace("\n", " ")
language = 'en'
output = gTTS(text=mytext, lang=language, slow=False)
output.save('./Imagetospeech/imagetospeech.mp3')
file.close()
os.system("start ./Imagetospeech/imagetospeech.mp3")

question = input("Do you want to delete the files (Y/N): ")
if question == 'Y' or question == 'y':
    os.remove('./Imagetospeech/text.txt')
    os.remove('./Imagetospeech/imagetospeech.mp3')

elif question == 'N' or question == 'n':
    print("Files saved")
