# Project Description
About: "Detecting Color and using colored marker to draw virtually."

It is an OpenCV application that can track an object’s movement, using which a user can draw on the screen by moving the object around — I call it Webcam Paint.

## Code Explanation

### Step 1: Initialize Some Stuff
Firstly, I need to import the necessary libraries.

Then I initialize variables that are used in the following steps.

The *lower* and the *upper* numpy arrays help us in finding the colored cap. The *myColors* and *myColorValues* are used to create list of colors. The *myPoints* helps to set the coordinates of each of the color.

### Step 2: Start Reading The Video (Frame by Frame)
Now I use the OpenCV function **cv2.VideoCapture()** method to read a video, frame by frame (using a while loop), either from a video file or from a webcam in real-time. In this case, I pass 0 to the method to read from a webcam.

### Step 3: Find The Contour-Of-Interest
Once I start reading the webcam feed, I constantly look for a color object in the frames with the help of **cv2.inRange()** method and use the *upper* and *lower* variables initialized in Step 1. Once I find the contour(the if condition passes when a contour is found), I do a series of image operations and make it smooth. I use the center of the contour to draw on the screen as it moves. The **cv2.circle()** method draws a circle around it.

### Step 4: Start Drawing And Store The Drawings
Now I start tracking coordinates of each and every point the center of the contour touches on the screen, along with its color.

I have created a *drawOnCanvas()* function to store the points in its respective color.

### Step 5: Show The Drawings On The Screen
So far I stored all the points in their respective color. Now I just join all the points in each and every frame with a line and put it on a window we created using **cv2.imshow()** method and it all fits perfectly to work!

That’s it! I have successfully used a bunch of basic image processing tools and operations in OpenCV!