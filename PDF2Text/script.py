import PyPDF2

pdf = input(r"Enter the path of PDF file: ")
n = int(input("Enter number of pages: "))
st=""
page = PyPDF2.PdfFileReader(pdf) 
for i in range(n):
    
    st += page.getPage(i).extractText()

with open('./PDF2Text/pages/text.txt','w') as f:
    f.write(st)

