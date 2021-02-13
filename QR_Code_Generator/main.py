# Installing required libraries
pip install pyqrcode
pip install pypng

# Importing the libraries
import pyqrcode
import png

# Link Which represents the QR Code.
link = "www.google.com"

# Generating QR Code.
url = pyqrcode.create(link)

# Creating and Saving the file as SVG.
url.svg("my_qr.svg", scale=10)

# Creating and Saving the file as PNG.
url.png("my_qr.png", scale=12)
