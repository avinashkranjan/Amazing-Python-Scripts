# PDF Merger

A Python script that allows users to merge two PDF files into a single consolidated PDF document. It offers a user-friendly command-line interface, making PDF merging tasks quick and efficient.

## Description

nput files, ensuring that both files are accessible. If either or both files are not found, the script provides a warning message and proceeds to merge the available files.

Upon successfully merging the PDFs, the script prompts the user to specify the desired name for the output merged PDF file. The merged PDF is then created, combining the pages from the input PDFs in the order they were entered.

The script utilizes the PyPDF2 library to perform the PDF merging, ensuring compatibility with various PDF versions. Additionally, it includes basic error handling to notify the user of any issues with the input files.

## Usage

1. Make sure you have Python and the PyPDF2 library installed.
2. Run the script and follow the prompts to enter the names of the two PDF files you want to merge.
3. Specify the desired name for the output merged PDF file.
4. The script will create the merged PDF with the specified name in the current directory.

## Requirements

- Python
- PyPDF2 library

