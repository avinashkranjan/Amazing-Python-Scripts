import os
import shutil


def separate_files():
    source_folder = os.getcwd()  # Current working directory as the source folder
    destination_folder = os.path.join(source_folder, "separated_files")

    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    for filename in files:
        # Ignore directories and the script file itself
        if os.path.isdir(os.path.join(source_folder, filename)) or filename == "file_separator.py":
            continue

        # Get the file extension
        _, ext = os.path.splitext(filename)

        # Determine the category based on the file extension
        category = get_category(ext)

        # Create a subfolder for the category if it doesn't exist
        subfolder = os.path.join(destination_folder, category)
        os.makedirs(subfolder, exist_ok=True)

        # Move the file to the appropriate subfolder
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(subfolder, filename)
        shutil.move(source_path, destination_path)

        print(f"Moved '{filename}' to '{subfolder}'")


def get_category(file_extension):
    # Mapping of file extensions to categories
    extension_mapping = {
        ".doc": "documents",
        ".docx": "documents",
        ".txt": "documents",
        ".pdf": "documents",
        ".xls": "documents",
        ".xlsx": "documents",
        ".ppt": "documents",
        ".pptx": "documents",
        ".jpg": "images",
        ".jpeg": "images",
        ".png": "images",
        ".gif": "images",
        ".bmp": "images",
        ".mp4": "videos",
        ".avi": "videos",
        ".mov": "videos",
        ".mkv": "videos",
        ".wmv": "videos",
        ".mp3": "audio",
        ".wav": "audio",
        ".flac": "audio",
        ".zip": "archives",
        ".rar": "archives",
    }

    # Return the category based on the file extension
    return extension_mapping.get(file_extension, "others")


if __name__ == "__main__":
    # Call the function to separate the files
    separate_files()
