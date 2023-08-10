import os
import shutil
import tkinter as tk
from tkinter import filedialog


class file_sorter:
    def __init__(self, root):
        self.root = root
        self.root.title("File Sorter")
        self.root.configure(bg="#333")

        self.select_button = tk.Button(
            root, text="Select Directory", command=self.select_directory, bg="#555", fg="white")
        self.select_button.pack(pady=10)

        self.sort_button = tk.Button(
            root, text="Sort Files", command=self.sort_files, bg="#555", fg="white")
        self.sort_button.pack(pady=5)

        self.status_label = tk.Label(root, text="", bg="#333", fg="white")
        self.status_label.pack(pady=10)

    def select_directory(self):
        self.dir_path = filedialog.askdirectory()
        self.status_label.config(text="Selected directory: " + self.dir_path)

    def sort_files(self):
        if hasattr(self, "dir_path"):
            for filename in os.listdir(self.dir_path):
                if os.path.isfile(os.path.join(self.dir_path, filename)):
                    ext = filename.split(".")[-1]
                    target_dir = os.path.join(self.dir_path, ext)

                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)

                    source_path = os.path.join(self.dir_path, filename)
                    target_path = os.path.join(target_dir, filename)

                    shutil.move(source_path, target_path)

            self.status_label.config(text="Files sorted successfully.")
        else:
            self.status_label.config(text="Please select a directory first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = file_sorter(root)
    root.mainloop()
