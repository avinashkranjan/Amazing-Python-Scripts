from pdfrw import PdfWriter, PdfReader
import os


def delete(path, del_page):
    """
    The function delete takes two arguments path and del_page
    path is the path of the source pdf file.
    This function deletes the pages from the pdf file.

        Parameters:
        path      : Path of the pdf file.
        del_page  : A list of pages to be deleted.

           Returns:
               None    
    """
    # create a pdf object using PdfReader that could be read
    pdf_obj = PdfReader(path)
    # pdf_obj.pages attribute gives the length of the pages in pdf
    total_pages = len(pdf_obj.pages)
    print("Total Pages in PDF are:", total_pages)
    # Initialising the writer object using the PdfWriter class
    writer = PdfWriter()

    # Adding only those pages that we need to this list excluding del_page
    page_list = [
        page for page in range(1, total_pages + 1) if page not in del_page
    ]

    # Index of pdf_obj.pages starts from 0.
    for page in page_list:
        writer.addpage(pdf_obj.pages[page - 1])

    # removing the original pdf
    os.remove(path)
    # writing the modified file to the memory
    writer.write(path)


path = input("enter the path(full or relative) of the pdf file:")
del_page = input(
    "Enter the pages to be deleted seperated by comma(,):").strip().split(",")
del_page = [int(i) for i in del_page]
delete(path, del_page)
print("\n\t pages", *del_page, "have been deleted successfully!!!")
