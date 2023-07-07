#!python3
# -*- coding: utf-8 -*-

import openpyxl
import sys

# inputs
print("This programme writes the data in any Comma-separated value file (such as: .csv or .data) to a Excel file.")
print("The input and output files must be in the same directory of the python file for the programme to work.\n")

csv_name = input("Name of the CSV file for input (with the extension): ")
sep = input("Separator of the CSV file: ")
excel_name = input("Name of the excel file for output (with the extension): ")
sheet_name = input("Name of the excel sheet for output: ")

# opening the files
try:
    wb = openpyxl.load_workbook(excel_name)
    sheet = wb.get_sheet_by_name(sheet_name)

    file = open(csv_name, "r", encoding="utf-8")
except:
    print("File Error!")
    sys.exit()

# rows and columns
row = 1
column = 1

# for each line in the file
for line in file:
    # remove the \n from the line and make it a list with the separator
    line = line[:-1]
    line = line.split(sep)

    # for each data in the line
    for data in line:
        # write the data to the cell
        sheet.cell(row, column).value = data
        # after each data column number increases by 1
        column += 1

    # to write the next line column number is set to 1 and row number is increased by 1
    column = 1
    row += 1

# saving the excel file and closing the csv file
wb.save(excel_name)
file.close()
