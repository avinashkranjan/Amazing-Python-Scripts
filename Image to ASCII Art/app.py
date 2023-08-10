from PIL import Image

ASCII_CHARS = '@B%8WM#*oahkbdpwmZO0QCJYXzcvnxrjft/\|()1{}[]-_+~<>i!lI;:,"^`\'. '


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    return image.convert("L")


def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str


def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    ascii_width = image.width

    ascii_img = ""
    for i in range(0, len(ascii_str), ascii_width):
        ascii_img += ascii_str[i:i+ascii_width] + "\n"

    print(ascii_img)


if __name__ == "__main__":
    image_path = "pngwing.com (1).png"
    new_width = 100
    main(image_path, new_width)
