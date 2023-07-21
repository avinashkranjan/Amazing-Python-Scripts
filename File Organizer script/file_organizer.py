import os
import shutil


def organize_files(source_directory, destination_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_directory, file)

            # Create destination directory if it doesn't exist
            os.makedirs(destination_directory, exist_ok=True)

            # Move the file to the destination directory
            shutil.move(source_path, destination_path)

            print(f"Moved {file} to {destination_directory}")


# Example usage: Organize files from source directory to destination directory
source_directory = '/path/to/source_directory'
destination_directory = '/path/to/destination_directory'

organize_files(source_directory, destination_directory)
