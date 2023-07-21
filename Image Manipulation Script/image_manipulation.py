from PIL import Image


def resize_image(input_image, output_image, new_size):
    image = Image.open(input_image)
    resized_image = image.resize(new_size)
    resized_image.save(output_image)
    print("Image resized and saved successfully.")


def rotate_image(input_image, output_image, degrees):
    image = Image.open(input_image)
    rotated_image = image.rotate(degrees)
    rotated_image.save(output_image)
    print("Image rotated and saved successfully.")


def flip_image(input_image, output_image, flip_mode):
    image = Image.open(input_image)
    flipped_image = image.transpose(flip_mode)
    flipped_image.save(output_image)
    print("Image flipped and saved successfully.")


# Example usage: Resize, rotate, and flip an image
input_file = 'input_image.jpg'
resized_file = 'resized_image.jpg'
rotated_file = 'rotated_image.jpg'
flipped_file = 'flipped_image.jpg'

new_size = (800, 600)
degrees_to_rotate = 90
flip_mode = Image.FLIP_LEFT_RIGHT

resize_image(input_file, resized_file, new_size)
rotate_image(input_file, rotated_file, degrees_to_rotate)
flip_image(input_file, flipped_file, flip_mode)
