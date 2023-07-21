import argparse
from stegano import lsb
import os


def hide_text_in_image(image_path, text, output_path):
    secret_image = lsb.hide(image_path, text)
    secret_image.save(output_path)


def reveal_text_from_image(image_path):
    try:
        secret_text = lsb.reveal(image_path)
        # here 1 and 0 are used to enhance script quality
        return (secret_text, 1)
    except UnicodeDecodeError:
        return ("Unable to reveal text. Decoding error occurred.", 0)
    except IndexError:
        return ("Failed to find message in this file format, Try using different file format like png", 0)
    except Exception as e:
        return (f"Contact the owner! {e}", 0)


def main():
    print("\n[Welcome to Image text hider this script can hide text inside image]\n")
    print("To Hide the text inside image\nUSAGE: python img_text_hider.py hide img_name_with_path.jpg 'This is my secret msg' output_file_name.jpg\n")
    print("To reveal the hidden text inside image\nUSAGE: python img_text_hider.py reveal hidden_img_name.jpg\n")
    parser = argparse.ArgumentParser(description="Image Text Hider")

    subparsers = parser.add_subparsers(
        dest="command", help="Available commands")

    # Hide command
    hide_parser = subparsers.add_parser(
        "hide", help="Hide text behind an image")
    hide_parser.add_argument("image", help="Path to the image file")
    hide_parser.add_argument("text", help="Text to hide")
    hide_parser.add_argument(
        "output", help="Output path for the image with hidden text")

    # Reveal command
    reveal_parser = subparsers.add_parser(
        "reveal", help="Reveal text from an image")
    reveal_parser.add_argument("image", help="Path to the image file")

    args = parser.parse_args()

    if args.command == "hide":
        if os.path.exists(args.image):
            hide_text_in_image(args.image, args.text, args.output)
            print(
                "Text hidden in the image successfully. Output image saved at", args.output)
        else:
            print("Image path you specified does not exist, Make sure to check image path and file name with extention")
    elif args.command == "reveal":
        if os.path.exists(args.image):

            revealed_text, check = reveal_text_from_image(args.image)

            if check == 1:  # if works out well
                print(f"Revealed text: [{revealed_text}]")
            else:       # else display with error so that user can troubleshot the problem easily
                print(f'Error!,{revealed_text}')

        else:
            print("Image path you specified does not exist, Make sure to check image path and file name with extention")


if __name__ == "__main__":
    main()
