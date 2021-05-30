# PDF-Watermark-Remover

The script PDF-Watermark-Remover will remove the watermark from the PDF files. The watermark is selected based on ranges of RGB color and based on selected pixels it will remove the watermark from the pages.

## Setup instructions
1. Download the python script file ("PDF-Watermark-Remover.py")
2. Open the cmd/powershell/shell and type below line & hit return
    - For windows
        ```
        python <path of "PDF-Watermark-Remover.py">
        ```
    - For mac/linux
        ```
        python3 <path of "PDF-Watermark-Remover.py">
        ```

## Output

| Original Page | Output Page |
| --- | --- |
| <image src= "Sample\sample001.png" width = 2000px> | <image src= "Results\img1.jpg" width = 2000px> |
| <image src= "Sample\sample002.png" width = 2000px> | <image src= "Results\img2.jpg" width = 2000px> |
| <image src= "Sample\sample003.png" width = 2000px> | <image src= "Results\img3.jpg" width = 2000px> |
| <image src= "Sample\sample004.png" width = 2000px> | <image src= "Results\img4.jpg" width = 2000px> |
| <image src= "Sample\sample005.png" width = 2000px> | <image src= "Results\img5.jpg" width = 2000px> |
| <image src= "Sample\sample006.png" width = 2000px> | <image src= "Results\img6.jpg" width = 2000px> |

## Author(s)
Zankrut Goyani <br>
M.Sc. (Agri.)

## Disclaimers, if any
Script will not removed base color watermarks like Red (255, 0, 0), Green (0, 255, 0) and Blue (0, 0, 255)