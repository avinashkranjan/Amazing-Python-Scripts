# PDF Watermark Remover

A python script to remove gray watermarks from the PDFsA python script to remove gray watermarks from the PDFs.

- The script work in two steps:
1. it extract the pages after removing watermark as an image
2. Merge the images in single PDF file according to its order

## Setup instructions

1. Download 'remover.py' 
2. Open cmd/command shell and run the remover.py by following code
``` python <path of remover.py> ```
3. Give the PDF file path and hit return
4. Output file will generated into the same directory of original PDF File

## Output

| Sample Image | Output Image |
| --- | --- |
| <image src= "sample1.png" width = 2000px> | <image src= "img\img1.jpg" width = 2000px> |
| <image src= "sample2.png" width = 2000px> | <image src= "img\img2.jpg" width = 2000px> |

## Author(s)
Zankrut Goyani
M.Sc. (Agri.)

## Disclaimers: Colourful watermark partially removed