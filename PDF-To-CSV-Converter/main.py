import tabula  # simple wrapper for tabula-java, read tables from PDF into csv
import os
print("[-+-] starting pdf_csv.py...")
print("[-+-] import a pdf and convert it to a csv")
# -----------------------------------------------------------------------------
print("[-+-] importing required packages for pdf_csv.py...")
# from modules.defaults import df # local module
print("[-+-] pdf_csv.py packages imported! \n")
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------


def pdf_csv():  # convert pdf to csv
    print("[-+-] default filenames:")
    filename = "sample1"
    pdf = filename + ".pdf"
    csv = filename + ".csv"
    print(pdf)
    print(csv + "\n")

    print("[-+-] default directory:")
    print("[-+-] (based on current working directory of python file)")
    defaultdir = os.getcwd()
    print(defaultdir + "\n")

    print("[-+-] default file paths:")
    pdf_path = os.path.join(defaultdir, pdf)
    csv_path = os.path.join(defaultdir, csv)
    print(pdf_path)
    print(csv_path + "\n")

    print("[-+-] looking for default pdf...")
    if os.path.exists(pdf_path) == True:  # check if the default pdf exists
        print("[-+-] pdf found: " + pdf + "\n")
        pdf_flag = True
    else:
        print("[-+-] looking for another pdf...")
        arr_pdf = [
            defaultdir for defaultdir in os.listdir()
            if defaultdir.endswith(".pdf")
        ]
        if len(arr_pdf) == 1:  # there has to be only 1 pdf in the directory
            print("[-+-] pdf found: " + arr_pdf[0] + "\n")
            pdf_path = os.path.join(defaultdir, arr_pdf[0])
            pdf_flag = True
        elif len(arr_pdf) > 1:  # there are more than 1 pdf in the directory
            print("[-+-] more than 1 pdf found, exiting script!")
            pdf_flag = False
            # TODO add option to select from available pdfs
        else:
            print("[-+-] pdf cannot be found, exiting script!")
            pdf_flag = False

    if pdf_flag == True:
        # check if csv exists at the default file path
        # if csv does not exist create a blank file at the default path
        try:
            print("[-+-] looking for default csv...")
            open(csv_path, "r")
            print("[-+-] csv found: " + csv + "\n")
        except IOError:
            print("[-+-] did not find csv at default file path!")
            print("[-+-] creating a blank csv file: " + csv + "... \n")
            open(csv_path, "w")

        print("[-+-] converting pdf to csv...")
        #    print("[-+-] pdf to csv conversion suppressed! \n")
        try:
            tabula.convert_into(pdf_path,
                                csv_path,
                                output_format="csv",
                                pages="all")
            print("[-+-] pdf to csv conversion complete!\n")
        except IOError:
            print("[-+-] pdf to csv conversion failed!")

        print("[-+-] converted csv file can be found here: " + csv_path + "\n")

        print("[-+-] finished pdf_csv.py successfully!")


# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
pdf_csv()  # run the program
# -----------------------------------------------------------------------------
