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
    pdf_file_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

    with open('encrypted.pdf', 'wb') as fh:
        pdf_file_writer.write(fh)


def rotate_pages():
    '''Rotate the given PDF left or right by 90 degrees.'''
    input_pdf = input(r"Enter I/P PDF path ")
    pdf_file_writer = PdfFileWriter()
    pdf_file_reader = PdfFileReader(input_pdf)
    orient = input("Specify orientation: clockwise or counterclockwise ")

    # Rotate each page one by one accordingly
    if (orient == "clockwise"):
        for page_num in range(pdf_file_reader.getNumPages()):
            rot_page = pdf_file_reader.getPage(page_num).rotateClockwise(90)
            pdf_file_writer.addPage(rot_page)
    elif (orient == "counterclockwise"):
        for page_num in range(pdf_file_reader.getNumPages()):
            rot_page = pdf_file_reader.getPage(
                page_num).rotateCounterClockwise(90)
            pdf_file_writer.addPage(rot_page)

    with open('rotated.pdf', 'wb') as fh:
        pdf_file_writer.write(fh)


def ifPageExists(total_pages, page_no):
    """
    This function checks whether the given page number is in the specified range
    of total pages.
    """
    if page_no <= total_pages:
        return False
    return True


def reorder_pages():
    input_pdf = input(r"Enter I/P PDF path ")

    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    # get total no.of pages ie length of PDF
    total_pages = pdf_reader.getNumPages()
    # creates a list of of total pages in ascending order
    ordered_pages = [i + 1 for i in range(total_pages)]

    # Taking input that how many pages want to reorder
    n = int(input("Enter the Total Number of pages which you want to reorder:"))

    # Taking user INPUT of page no and location you want to move that page
    print("\nNow enter the Page no which you want to reorder with the expected location")

    # Running a loop to take input
    for i in range(n):
        ans_1 = True
        while ans_1:
            page_no = int(input("Enter the Page No. you want to reorder: "))
            ans_1 = ifPageExists(total_pages, page_no)
            if ans_1:  # if the no. is invalid
                print("Invalid Page No. ")
                print(f"Enter a number below {total_pages}")

        ans_2 = True
        while ans_2:
            expected_location = int(
                input("Enter the location you want to reorder: "))
            ans_2 = ifPageExists(total_pages, expected_location)
            if ans_2:  # if location is in invalid
                print("Invalid Page No. ")
                print(f"Enter a number below {total_pages}")

        # removing the pages from the initial list so that we can
        # move it to the specified location
        ordered_pages.remove(page_no)
        # inserting the page no at the specified location
        ordered_pages.insert(expected_location - 1, page_no)

        print("Pages are going to be in these order: ", end="")
        print(ordered_pages, "\n")

    # if ordered pages are ready in a list then passing it further into write function
    print("\nPDF being prepared !")
    for page in ordered_pages:
        # adding pages in write function page by page
        pdf_writer.addPage(pdf_reader.getPage(page - 1))

    # Saving the PDF with the specified name
    output_file = input(
        "Enter the filename in which you want to save (without .pdf extension): ") + '.pdf'
    with open(output_file, 'wb') as fh:
        pdf_writer.write(fh)

    print(f"Great Success!!! Check your directory for {output_file} file!")


def menu():
    '''Menu for the various functionalities offered'''
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    print(
        "\n Welcome to PDF-Tools \n Store the PDF's in the folder of the script \n Choose from the given options\n"
    )
    print(
        " 1.Merge PDF\n 2.Split PDF\n 3.Rotate PDF\n 4.Add Watermark\n 5.Encrypt PDF\n 6.Reorder PDF Pages\n"
    )
    # Call the necessary function according to the choice provided by the user
    z = int(input())
    if (z == 1):
        merge_pdfs()
    elif (z == 2):
        split_pdfs()
    elif (z == 3):
        rotate_pages()
    elif (z == 4):
        add_watermark()
    elif (z == 5):
        add_encryption()
    elif (z == 6):
        reorder_pages()
    else:
        print("Please select valid choice\n")
        menu()


if __name__ == '__main__':
    menu()
