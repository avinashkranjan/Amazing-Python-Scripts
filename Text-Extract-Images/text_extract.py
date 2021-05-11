from PIL import Image
import pytesseract as pt
import os
from pathlib import Path

current_location = (os.getcwd() + '\\')


def extract():
    """
    Function for extracting text from images.
    Additional it saves the text extracted as a txt file.
    """
    image_location = input("Enter the Folder name containing Images: ")
    image_path = os.path.join(current_location, image_location)

    # Enter the name of folder which would contain respective txt files
    destination = input("Enter your desired output location: ")
    destination_path = os.path.join(current_location, destination)

    # Path to Tesseract
    tesseract_path = input("Enter the Path to Tesseract: ")
    print(
        '\nNOTE: '
        'It is preferable to setup the PATH variable to Tesseract, see README. \n'
    )

    #  = r'C:\Program Files\Tesseract-OCR\tesseract'
    pt.pytesseract.tesseract_cmd = tesseract_path

    # iterating over the images in the folder
    for imageName in os.listdir(image_path):

        # Join the path and image name to obtain absolute path
        inputPath = os.path.join(image_path, imageName)
        img = Image.open(inputPath)

        # OCR
        text = pt.image_to_string(img, lang="eng")

        # Removing extensions
        img_file = Path(inputPath).stem
        print(img_file)

        # The output text file
        text_file = img_file + ".txt"
        output_path = os.path.join(destination_path, text_file)

        # saving the  text for every image in a separate .txt file
        with open(output_path, "w") as file:
            file.write(text)


if __name__ == '__main__':
    extract()
