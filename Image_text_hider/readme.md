# Image Text Hider

This script allows you to hide text inside an image using steganography. It utilizes the LSB (Least Significant Bit) technique to embed the text into the image without visibly altering the image.

## Requirements

- Python 3.6 or above
- Install the required packages by running `pip install -r requirements.txt`.

## Usage

To hide text inside an image:
python img_text_hider.py hide <image_path> <text> <output_path>

- `<image_path>`: Path to the image file.
- `<text>`: Text to hide inside the image.
- `<output_path>`: Output path for the image with hidden text.

To reveal the hidden text from an image:
python img_text_hider.py reveal <image_path>

- `<image_path>`: Path to the image file with hidden text.

## Example

Hide text inside an image:
python img_text_hider.py hide my_image.jpg "This is my secret message" output_image.jpg

Reveal the hidden text from an image:
python img_text_hider.py reveal output_image.jpg