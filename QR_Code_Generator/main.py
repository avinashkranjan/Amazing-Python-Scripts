# Installing required libraries
import png
import pyqrcode
# pip install pyqrcode
# pip install pypng

# Importing the libraries

# Link Which represents the QR Code.
link = "www.google.com"

# Generating QR Code.
url = pyqrcode.create(link)

# Creating and Saving the file as SVG.
url.svg("my_qr.svg", scale=10)

# Creating and Saving the file as PNG.
url.png("my_qr.png", scale=12)
