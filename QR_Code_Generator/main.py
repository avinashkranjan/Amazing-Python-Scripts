# Installing required libraries
pip install pyqrcode
pip install pypng

# Importing the libraries
import pyqrcode
import png

# Importing QRCode from pyqrcode.
from pyqrcode import QRCode

# Link Which represents the QR Code.
link = "www.google.com"

# Generating QR Code.
url = pyqrcode.create(s)

# Creating and Saving the file as SVG.
url.svg("my_qr.svg", scale=10)

# Creating and Saving the file as PNG.
url.png("my_qr.png", scale=12)
