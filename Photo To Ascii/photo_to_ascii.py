from PIL import Image

# ascii characters used to build the output text
CHARS = [".", ".", ".", "1", "1", "1", "1", "1", "0", "0", "0"]
# convert each pixel to grayscale


def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# convert pixels to a string of ascii characters


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([CHARS[pixel//23] for pixel in pixels])
    return(characters)


def photoascii():

    # attempt to open image from user-input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)
    except Exception:
        print("Invalid path")
        return
    # Fetching the name of the image
    image_name = ""
    flag = 0
    for i in path[::-1]:
        if i == "/":
            break
        if flag == 1:
            image_name = i+image_name
        if i == '.':
            flag = 1

    # Resizing of image
    new_width = 100
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))

    # convert image to ascii
    new_image_data = pixels_to_ascii(grayify(resized_image))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)]
                            for index in range(0, pixel_count, new_width)])

    # save result to "ascii_image.txt"
    with open("./Photo To Ascii/{}(ASCII).txt".format(image_name), "w") as f:
        f.write(ascii_image)


# run program
if __name__ == '__main__':
    photoascii()
