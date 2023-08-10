import os
import shutil


def automated_backup(source_dir, destination_dir):
    try:
        # Check if the source directory exists
        if not os.path.exists(source_dir):
            print(f"Source directory '{source_dir}' does not exist.")
            return

        # Create the destination directory if it doesn't exist
        os.makedirs(destination_dir, exist_ok=True)

        # Copy files and folders from source to destination
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_file = os.path.join(root, file)
                destination_file = os.path.join(
                    destination_dir, os.path.relpath(source_file, source_dir))
                shutil.copy2(source_file, destination_file)

        print("Backup completed successfully!")
    except Exception as e:
        print(f"An error occurred during backup: {e}")


if __name__ == '__main__':
    source_directory = input("Enter the source directory to be backed up: ")
    destination_directory = input(
        "Enter the destination directory for the backup: ")

    automated_backup(source_directory, destination_directory)
  '''
  To use the script, copy the code into a Python file (e.g., backup_script.py) and run it using a Python interpreter. The script will prompt you to enter the source and destination directories. After entering the directories, it will initiate the backup process and copy the files and folders from the source directory to the specified destination directory.
  '''
