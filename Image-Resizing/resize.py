import cv2
import os
from PIL import Image

# inputting dimensions (in Pixels) from user
width = int(input("Enter Width in Pixels: "))
height = int(input("Enter Height in Pixels: "))
dimensions = (width, height)

# inputting Horizontal and Vertical resolutions
horizontal_dpi = int(input("Enter Horizontal Dots Per Inches (DPI): "))
vertical_dpi = int(input("Enter Vertical Dots Per Inches (DPI): "))

# for each file in the images folder
for filename in os.listdir('images'):
    img = cv2.imread(os.path.join('images', filename))
    # if the image is read successfully
    if img is not None:
        resized = cv2.resize(img, dimensions, interpolation=cv2.INTER_CUBIC)
        if resized is not None:
            cv2.imwrite(os.path.join('resized-images', filename), resized)
            im = Image.open(os.path.join('resized-images', filename))
            # if resizing is successful, now proceeding to DPI
            if im is not None:
                im.save(os.path.join('resized-images', filename),
                        dpi=(horizontal_dpi, vertical_dpi))
