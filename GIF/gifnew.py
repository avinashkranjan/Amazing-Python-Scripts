from PIL import Image
import glob


def convert_to_gif(image_folder, gif_name, duration):
    # Change the file extension if necessary
    images = glob.glob(image_folder + "/*.jpg")

    frames = []
    for image in images:
        with Image.open(image) as img:
            frames.append(img.convert("RGBA"))

    frames[0].save(gif_name, format="GIF", append_images=frames[1:],
                   save_all=True, duration=duration, loop=0)
    print("GIF created successfully!")


def main():
    image_folder = "Image-Slideshow"  # Path to the folder containing the images
    gif_name = "output.gif"  # Name of the output GIF file
    duration = 500  # Duration between frames in milliseconds

    convert_to_gif(image_folder, gif_name, duration)


if __name__ == "__main__":
    main()
