import PyPDF2

pdf = input(r"Enter the path of PDF file: ")
n = int(input("Enter number of pages: "))

page = PyPDF2.PdfFileReader(pdf)
for i in range(n):
    st = ""
    st += page.getPage(i).extractText()

    with open(f'./PDF2Text/text{i}.txt', 'w') as f:
        f.write(st)
