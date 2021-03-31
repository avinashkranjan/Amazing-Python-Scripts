from gtts import gTTS
import os


file = open(r'./Imagetospeech/Text/text.txt')
mytext = file.read().replace("\n"," ")
language = 'en'
output = gTTS(text=mytext, lang=language, slow=False)
output.save('./Imagetospeech/sound/imagetospeech.mp3')
file.close()
os.system("start ./Imagetospeech/sound/imagetospeech.mp3")

