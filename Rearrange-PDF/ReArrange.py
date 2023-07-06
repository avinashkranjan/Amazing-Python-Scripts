from pdfrw import PdfReader, PdfWriter
from pathlib import Path
import os
import ntpath

# This is a simple function to get only the file name as a string from absolute path of the file.


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def input_and_parse(n):
    """
    The function input_and_parse gathers the inputs and parses and then sorts them in
    the order required by reorder(path,dic) function
    Parameters:
        n (int):No. of pages in the PDF file.
    Returns:
       dic :A parsed dictionary.
    """
    print(
        "enter the current page and the page you want it to be on seperate values by a comma ',' \n"
    )
    # store the input in a list and then convert the input string into
    # using map function to convert the data in lists into int values
    lst = list(
        map(lambda x: [int(x[0]), int(x[1])],
            [input().split(',') for _ in range(n)]))
    # Swapping the position of the lst values to better parse it in dictionary
    lst = [[x[1], x[0]] for x in lst]
    lst.sort(key=lambda x: x[0])
    dic = {curr: new for curr, new in lst}
    # now I have sorted the dic to the required needs of reorder function
    return dic


def re_arrange(file_path, output_file_name, dic):
    """
    The function reorder takes two arguments path and dic
    path is the path of the source pdf file which is in wrong
    order and then creates a modified pdf file with pages in the right order.
    Parameters:
        path : Path of the pdf file to be modified
        dic  : A dictionary with key value pairs of pages.
    Returns:
        None    
    """
    file_path = Path(file_path)
    # create a pdf object using PdfReader that could be read
    pdf_obj = PdfReader(file_path)
    # pdf_obj.pages attribute gives the length of the pages in pdf
    total_pages = len(pdf_obj.pages)
    print("Total Pages in PDF are:", total_pages)
    # Initialising the writer object using the PdfWriter class,from this we would create a new modified Pdf
    writer = PdfWriter()

    # new and old here mean the new position of the "old" page location
    for new, old in dic.items():
        # indexing pages list
        writer.addpage(pdf_obj.pages[old - 1])
        print(f"page{new} added from {old}")

    # accesing the name of the file without .pdf to save it with a new one
    writer.write(Path(os.path.dirname(file_path) + "\\" + output_file_name))


if __name__ == "__main__":
    file_path = input("Enter the path of the pdf file:")
    print("\n")
    output_file_name = path_leaf(file_path)[:-4] + "_modified.pdf"
    dic = input_and_parse(len(PdfReader(file_path).pages))
    re_arrange(file_path, output_file_name, dic)
    print("New modified pdf file created succesfully!")
"""
I have added a wrong.pdf file which has pages in wrong order for testing purposes.

pairs of pages with right,wrong format you can use this in pdf_reorder.py script
1,5
2,2
3,3
4,1
5,4
"""
