import os
import argparse
import img2pdf

def convert_images_to_pdf(directory_path, output_file):
    image_files = []
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']

    # Gather the image files from the directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(tuple(allowed_extensions)):
            image_files.append(os.path.join(directory_path, filename))

    # Convert the image files to a PDF
    with open(output_file, "wb") as f:
        f.write(img2pdf.convert(image_files))

def main():
    parser = argparse.ArgumentParser(description="Convert a collection of image files into a single PDF file. Make sure you create a folder (eg 'images') in the same directory as the script")
    parser.add_argument("directory_path", help="Path to the directory containing image files")
    parser.add_argument("output_file", help="Output PDF file name (End it with .pdf)")
    args = parser.parse_args()

    convert_images_to_pdf(args.directory_path, args.output_file)

if __name__ == "__main__":
    main()
