import os


def search_files(directory, extension):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                found_files.append(os.path.join(root, file))
    return found_files


def main():
    print("File Search")
    print("-----------")
    directory = input("Enter the directory to search: ")
    extension = input(
        "Enter the file extension to search for (e.g., .txt, .jpg): ")

    found_files = search_files(directory, extension)

    if found_files:
        print("Found files:")
        for file in found_files:
            print(file)
    else:
        print("No files with the specified extension were found.")


if __name__ == "__main__":
    main()
