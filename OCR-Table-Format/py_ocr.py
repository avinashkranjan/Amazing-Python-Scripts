# alternate approach using pyocr
from PIL import Image
import sys

import pyocr
import pyocr.builders

import codecs

tool = pyocr.get_available_tools()[0]
builder = pyocr.builders.TextBuilder()

txt = tool.image_to_string(
    Image.open('file.tiff'),
    lang="eng",
    builder=builder
)
# txt is a Python string

with codecs.open("toto.txt", 'w', encoding='utf-8') as file_descriptor:
    builder.write_file(file_descriptor, txt)
# toto.txt is a simple text file, encoded in utf-8