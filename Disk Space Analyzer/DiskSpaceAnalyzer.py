import os


def get_size(path):
    total_size = 0
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
    return total_size


def analyze_disk_space(directory):
    files = []
    folders = []
    for entry in os.scandir(directory):
        if entry.is_file():
            size = get_size(entry.path)
            files.append((entry.name, size))
        elif entry.is_dir():
            size = get_size(entry.path)
            folders.append((entry.name, size))

    sorted_files = sorted(files, key=lambda x: x[1], reverse=True)
    sorted_folders = sorted(folders, key=lambda x: x[1], reverse=True)

    print("Files:")
    for file in sorted_files:
        name, size = file
        print(f"{name}: {size} bytes")

    print("\nFolders:")
    for folder in sorted_folders:
        name, size = folder
        print(f"{name}: {size} bytes")


# Specify the directory to analyze
directory = r"C:\Users\python"  # insert your directory path here

# Analyze the disk space
analyze_disk_space(directory)
