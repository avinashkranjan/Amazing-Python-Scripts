"""
Script that converts any Image into its ASCII representation.
"""

from sys import exit as sysexit
from PIL import Image, ImageEnhance


def pixels_to_ascii(image, char_ramp):
    """
    Function that takes in an image and a character sequence.
    And returns a string containing the ASCII representation of
    the image based on the character sequence provided.
    """

    pixels = image.convert("L").getdata()
    characters = " ".join(
        [char_ramp[int((pixel / 256) * len(char_ramp))] for pixel in pixels]
    )
    pixel_count = len(characters)
    scanline_width = image.width * 2

    return "\n".join(
        [
            characters[index: (index + scanline_width)]
            for index in range(0, pixel_count, scanline_width)
        ]
    )


def input_image():
    """
    Function that asks user for a path to an image file
    and checks for validity. Then it loads and returns the
    image and the path as a tuple(image, path).
    """

    path = input("Enter a valid pathname to an image:\n")

    try:
        image = Image.open(path)
    except IOError:
        print("Invalid Path!")
        sysexit()

    return image, path


def input_ramp():
    """
    Function that asks the user to choose from a set
    of character sequences or to specify their own
    custom sequence and then returns that as a string.
    """

    print("Choose a Character Sequence!")
    print("1 - Basic")
    print("2 - Standard (Short)")
    print("3 - Standard (Long)")
    print("4 - Unicode Blocks")
    print("5 - Unicode Shades")
    print("6 - Enter Custom Sequence")
    choice = input("Input: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid Input!")
        sysexit()

    if choice == 1:
        return list("00011111...")
    if choice == 2:
        return list("@%#*+=-:. ")
    if choice == 3:
        return list(
            "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft"
            + "/\\|()1}{[]?-_+~<>i!lI;:,\"^`'. "
        )
    if choice == 4:
        return ["█", "▉", "▊", "▋", "▌", "▍", "▎", "▏"]
    if choice == 5:
        return ["█", "▓", "▒", "░", " "]
    if choice == 6:
        while True:
            custom_ramp = input("Enter character sequence ['?' for info]: ")
            if custom_ramp == "?":
                print(
                    "The character sequence must start with characters",
                    "that represent high pixel density and end with",
                    "characters that represent low pixel density.",
                )
            else:
                break
        if len(custom_ramp) == 0:
            print("Invalid Input!")
            sysexit()
        return list(custom_ramp)

    print("Invalid Input!")
    sysexit()


def input_contrast():
    """
    Function that asks user for the contrast factor that is to be applied
    on the image before conversion. And returns it.
    """

    while True:
        contrast_factor = input("Enter contrast factor ['?' for info] : ")
        if contrast_factor == "?":
            print(
                "Contrast factor is a value that is used to controle",
                "the contrast of the output. Default value of the contrast",
                "factor is 1. Negative value will invert the output.",
            )
        else:
            break

    try:
        contrast_factor = float(contrast_factor)
    except ValueError:
        print("Invalid Input!")
        sysexit()

    return contrast_factor


def resize_image(image):
    """
    Function that takes in an image and asks the user for a sample size.
    Then returns a resized image with each pixel representing the sample grid.
    """

    while True:
        sample_size = input("Enter the sample size ['?' for info] : ")
        if sample_size == "?":
            print(
                "Sample size refers to the number of pixels",
                "that will be sampled for one character.",
                "Default value of sample size is 4.",
                "Its value must be greater than or equal to 1.",
            )
        else:
            break

    try:
        sample_size = int(sample_size)
    except ValueError:
        print("Invalid Input!")
        sysexit()

    if sample_size <= 0:
        print("Invalid Input!")
        sysexit()

    width, height = image.size
    new_width = width // sample_size
    new_height = (new_width * height) // width

    return image.resize((new_width, new_height))


def get_output_path(path):
    """
    Function that takes in the path of the input image file and returns the
    path of a text file that the ouput will be saved to.
    """

    dot_index = path.rfind(".")
    slash_index = path.rfind("\\")

    if slash_index == -1:
        slash_index = path.rfind("/")

    image_name = path[slash_index + 1: dot_index] + "_" + path[dot_index + 1:]

    return path[:slash_index] + f"/{image_name}_ASCII.txt"


def main():
    """
    The main function.
    """

    image, path = input_image()
    char_ramp = input_ramp()

    contrast_factor = input_contrast()
    if contrast_factor < 0:
        char_ramp.reverse()
        contrast_factor = -contrast_factor

    image = resize_image(ImageEnhance.Contrast(image).enhance(contrast_factor))
    ascii_image = pixels_to_ascii(image, char_ramp)

    with open(get_output_path(path), "w", encoding="utf8") as file:
        file.write(ascii_image)


if __name__ == "__main__":
    main()
