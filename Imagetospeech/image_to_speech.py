import pytesseract
from PIL import Image
from gtts import gTTS
import os


pytesseract.pytesseract.tesseract_cmd = input(r'Enter the path: ')

img = input(r"Enter image: ")
target = Image.open(img)
text = pytesseract.image_to_string(target, config='')

with open(f"./Imagetospeech/Text/text.txt",'w') as f:
    f.write(text)

file = open(r'./Imagetospeech/Text/text.txt')
mytext = file.read().replace("\n"," ")
language = 'en'
output = gTTS(text=mytext, lang=language, slow=False)
output.save('./Imagetospeech/sound/imagetospeech.mp3')
file.close()
os.system("start ./Imagetospeech/sound/imagetospeech.mp3")

question = input("Do you want to delete the files (Y/N): ")
if question=='Y'or question=='y':
    os.remove('./Imagetospeech/Text/text.txt')
    os.remove('./Imagetospeech/sound/imagetospeech.mp3')

elif question=='N'or question=='n':
    print("Files saved")
