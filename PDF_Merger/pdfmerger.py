import PyPDF2


def merge_pdfs(output_filename, input_files):
    pdf_merger = PyPDF2.PdfMerger()

    for file in input_files:
        try:
            with open(file, 'rb') as pdf_file:
                pdf_merger.append(pdf_file)
        except FileNotFoundError:
            print(f"Warning: File '{file}' not found. Skipping...")

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f"PDFs merged successfully! Output file: {output_filename}")


def main():
    print("PDF Merge Tool")
    print("Please enter the names of the two PDF files to merge:")

    pdf1 = input("PDF 1: ")
    pdf2 = input("PDF 2: ")

    output_filename = input("Enter the name for the merged PDF: ")

    input_files = [pdf1, pdf2]

    merge_pdfs(output_filename, input_files)


if __name__ == "__main__":
    main()
