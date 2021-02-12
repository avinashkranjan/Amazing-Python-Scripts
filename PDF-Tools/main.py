import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_pdfs():
    ''' Merge multiple PDF's into one combined PDF '''

    input_paths = input(r"Enter comma separated list of paths to the PDFs ")
    paths = input_paths.split(',')
    pdf_file_writer = PdfFileWriter()

    # Pick each pdf one by one and combined to one single pdf
    for path in paths:
        pdf_file_reader = PdfFileReader(path)
        for page in range(pdf_file_reader.getNumPages()):
            pdf_file_writer.addPage(pdf_file_reader.getPage(page))

    # Output the merged pdf
    with open('merged.pdf', 'wb') as out:
        pdf_file_writer.write(out)


def split_pdfs():
    '''Split PDF to multiple PDF's of 1 Page each'''

    input_pdf = input(r"Enter I/P PDF path ")
    pdf = PdfFileReader(input_pdf)
    for page in range(pdf.getNumPages()):
        pdf_file_writer = PdfFileWriter()
        pdf_file_writer.addPage(pdf.getPage(page))

        # Append page num to each new pdf
        output = 'split{page}.pdf'.format(page=page)
        with open(output, 'wb') as output_pdf:
            pdf_file_writer.write(output_pdf)


def add_watermark():
    ''' Adds watermark to given PDF. 
    Note: The watermark PDF should be a image with transparent background '''

    input_pdf = input(r"Enter I/P PDF path ")
    watermark = input(r"Enter watermark PDF path ")
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_file_reader = PdfFileReader(input_pdf)
    pdf_file_writer = PdfFileWriter()

    # Watermark all the pages
    for page_num in range(pdf_file_reader.getNumPages()):
        page = pdf_file_reader.getPage(page_num)
        page.mergePage(watermark_page)
        pdf_file_writer.addPage(page)

    with open('watermarked-pdf.pdf', 'wb') as out:
        pdf_file_writer.write(out)


def add_encryption():
    ''' Encrypts the given PDF with the provided password '''

    input_pdf = input(r"Enter I/P PDF path ")
    password = input(r"Enter password ")
    pdf_file_writer = PdfFileWriter()
    pdf_file_reader = PdfFileReader(input_pdf)

    for page_num in range(pdf_file_reader.getNumPages()):
        pdf_file_writer.addPage(pdf_file_reader.getPage(page_num))
    # Encrypt using the password
    pdf_file_writer.encrypt(user_pwd=password, owner_pwd=None,
                            use_128bit=True)

    with open('encrypted.pdf', 'wb') as fh:
        pdf_file_writer.write(fh)


def rotate_pages():
    '''Rotate the given PDF left or right by 90 degrees.'''

    input_pdf = input(r"Enter I/P PDF path ")
    pdf_file_writer = PdfFileWriter()
    pdf_file_reader = PdfFileReader(input_pdf)
    orient = input("Specify orientation: clockwise or counterclockwise ")

    # Rotate each page one by one accordingly
    if(orient == "clockwise"):
        for page_num in range(pdf_file_reader.getNumPages()):
            rot_page = pdf_file_reader.getPage(page_num).rotateClockwise(90)
            pdf_file_writer.addPage(rot_page)
    elif(orient == "counterclockwise"):
        for page_num in range(pdf_file_reader.getNumPages()):
            rot_page = pdf_file_reader.getPage(
                page_num).rotateCounterClockwise(90)
            pdf_file_writer.addPage(rot_page)

    with open('rotated.pdf', 'wb') as fh:
        pdf_file_writer.write(fh)


def menu():
    '''Menu for the various functionalities offered'''

    # Change Current working directory to where the script is located.
    # This is done to enable use of relative paths from base folder.
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    print("\n Welcome to PDF-Tools \n Store the PDF's in the folder of the script \n Choose from the given options\n")
    print(" 1.Merge PDF\n 2.Split PDF\n 3.Rotate PDF\n 4.Add Watermark\n 5.Encrypt PDF\n")
    # Call the necessary function according to the choice provided by the user
    z = int(input())
    if(z == 1):
        merge_pdfs()
    elif(z == 2):
        split_pdfs()
    elif(z == 3):
        rotate_pages()
    elif(z == 4):
        add_watermark()
    elif(z == 5):
        add_encryption()
    else:
        print("Please select valid choice\n")
        menu()


if __name__ == '__main__':
    menu()
