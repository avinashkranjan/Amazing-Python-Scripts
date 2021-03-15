<h1 align="center">Invisibility Cloak</h1>
An invisibility cloak is a magical garment which renders whomever or whatever it covers invisible 
<br>
In this project we create an invisibility cloak using python

---------------------------------------------------------------------

## Modules Used
- time
- OpenCv
- numpy

## How it works

- Capture and store static the background frame
- Capture current frames and convert image into HSV colour space
- Detect the defined color (red in our case) using color detection.
- Segment out the color by generating cloak
- Generate the final output by replacing cloak with background to create a resulting frame.
