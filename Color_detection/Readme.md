
# Colour Detection using Pandas and OpenCV

In this color detection Python project, we are going to build an application through which you can automatically get the name of the color by clicking on them. So for this, we will have a data file that contains the color name and its values. Then we will calculate the distance from each color and find the shortest one.

# Steps Used
- ##Importing required package and load the image.</br>
Package used - Pandas and cv2 for OpenCV bindings.</br>
- ##Reading the CSV file with pandas.</br>
- ##Set a mouse callback event on a window</br> 
First, we created a window in which the input image will display. Then, we set a callback function which will be called when a mouse event happens.</br>
**draw_function** -
In the function, we check if the event is double-clicked then we calculate and set the r,g,b values along with x,y positions of the mouse.</br>
- ##Calculate distance to get color name</br>
d = abs(Red — ithRedColor) + (Green — ithGreenColor) + (Blue — ithBlueColor)</br>
- ##Display image on the window</br>
Whenever a double click event occurs, it will update the color name and RGB values on the window.