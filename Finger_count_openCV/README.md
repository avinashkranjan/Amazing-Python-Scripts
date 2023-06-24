# Number of fingers using OpenCV

Counts the number of fingers shown by user using OpenCV library in Python

## Setup instructions



Navigate to the folder and run the following command to install the required python libraries

    pip install -r requirements.txt

Then run the command

    python main.py
   

## Working behind Hand gesture recogonition:

### grey filter

    grey = cv2.cvtColor(crop_image,cv2.COLOR_BGR2GRAY)

It is a very important step that needs to be performed in order to get the desired result


### Gaussian Blur

    blur = cv2.GaussianBlur(grey,(35,35),0)

In Gaussian Blur operation, the image is convolved with a Gaussian filter instead of the box filter. The Gaussian filter is a low-pass filter that removes the high-frequency components are reduced.

You can perform this operation on an image using the Gaussianblur() method of the imgproc class. Following is the syntax of this method −

    GaussianBlur(src, dst, ksize, sigmaX)

- src − A Mat object representing the source (input image) for this operation.

- dst − A Mat object representing the destination (output image) for this operation.

- ksize − A Size object representing the size of the kernel.

- sigmaX − A variable of the type double representing the Gaussian kernel standard deviation in X direction.


### Thresholding the Image

Here, the matter is straight-forward. For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value. The function cv.threshold is used to apply the thresholding. The first argument is the source image, which should be a grayscale image. The second argument is the threshold value which is used to classify the pixel values. The third argument is the maximum value which is assigned to pixel values exceeding the threshold. OpenCV provides different types of thresholding which is given by the fourth parameter of the function. Basic thresholding as described above is done by using the type cv.THRESH_BINARY. All simple thresholding types are:

- cv2.THRESH_BINARY
- cv2.THRESH_BINARY_INV
- cv2.THRESH_TRUNC
- cv2.THRESH_TOZERO
- cv2.THRESH_TOZERO_INV

In this project cv2.THRESH_BINARY_INV is used

    ret,thresh= cv2.threshold(blur,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
 ### Binary threshold inverted

![binary](https://user-images.githubusercontent.com/93030904/208385197-96bb4e66-e4eb-439f-bf25-5008b22704d0.jpg)



### Otsu's Binarization

In global thresholding, we used an arbitrary chosen value as a threshold. In contrast, Otsu's method avoids having to choose a value and determines it automatically.

Consider an image with only two distinct image values (bimodal image), where the histogram would only consist of two peaks. A good threshold would be in the middle of those two values. Similarly, Otsu's method determines an optimal global threshold value from the image histogram.

In order to do so, the cv.threshold() function is used, where cv.THRESH_OTSU is passed as an extra flag. The threshold value can be chosen arbitrary. The algorithm then finds the optimal threshold value which is returned as the first output.

Check out the example below. The input image is a noisy image. In the first case, global thresholding with a value of 127 is applied. In the second case, Otsu's thresholding is applied directly. In the third case, the image is first filtered with a 5x5 gaussian kernel to remove the noise, then Otsu thresholding is applied. See how noise filtering improves the result.

![otsu](https://user-images.githubusercontent.com/93030904/168461709-9bdf4f63-0e6f-4c8a-892b-0e47fbbffd0e.jpeg)

### Contours

Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.

For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
Since OpenCV 3.2, findContours() no longer modifies the source image but returns a modified image as the first of three return parameters.
In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Finding the contour with maximum area
    contour = max(contours, key=lambda x: cv2.contourArea(x))
    
    # Drawing the contour on the image
    cv2.drawContours(drawing, [contour], -1, (0, 255, 0), 0)

### contour approximation method

This is the third argument in cv2.findContours function. What does it denote actually?

Above, we told that contours are the boundaries of a shape with same intensity. It stores the (x,y) coordinates of the boundary of a shape. But does it store all the coordinates ? That is specified by this contour approximation method.

If you pass cv.CHAIN_APPROX_NONE, all the boundary points are stored. But actually do we need all the points? For eg, you found the contour of a straight line. Do you need all the points on the line to represent that line? No, we need just two end points of that line. This is what cv.CHAIN_APPROX_SIMPLE does. It removes all redundant points and compresses the contour, thereby saving memory.

Below image of a rectangle demonstrate this technique. Just draw a circle on all the coordinates in the contour array (drawn in blue color). First image shows points I got with cv2.CHAIN_APPROX_NONE (734 points) and second image shows the one with cv2.CHAIN_APPROX_SIMPLE (only 4 points). See, how much memory it saves!!!


![Chain Approximattion](./approx.jpg "Approximation simple")


### Convex Hull

    hull = cv2.convexHull(contour, returnPoints=False)
    
Finds the convex hull of a point set.

The function cv2.convexHull finds the convex hull of a 2D point set using the Sklansky's algorithm [194] that has O(N logN) complexity in the current implementation.

Parameters
- points	Input 2D point set, stored in std::vector or Mat.
- hull	Output convex hull. It is either an integer vector of indices or vector of points. In the first case, the hull elements are 0-based indices of the convex hull points in the original array (since the set of convex hull points is a subset of the original point set). In the second case, hull elements are the convex hull points themselves.
- clockwise	Orientation flag. If it is true, the output convex hull is oriented clockwise. Otherwise, it is oriented counter-clockwise. The assumed coordinate system has its X axis pointing to the right, and its Y axis pointing upwards.
- returnPoints	Operation flag. In case of a matrix, when the flag is true, the function returns convex hull points. Otherwise, it returns indices of the convex hull points.

### Convexity Defects

    defects = cv2.convexityDefects(contour, hull)


![Convexity Defects](https://user-images.githubusercontent.com/93030904/168461387-94120ae1-553a-4516-9913-e956b959e9fd.png "Convexity defect")

Parameters
- contour:	Input contour.
- convexhull:	Convex hull obtained using convexHull that should contain indices of the contour points that make the hull.
- convexityDefects:	The output vector of convexity defects. In C++ and the new Python/Java interface each convexity defect is represented as 4-element integer vector (a.k.a. Vec4i): (start_index, end_index, farthest_pt_index, fixpt_depth), where indices are 0-based indices in the original contour of the convexity defect beginning, end and the farthest point, and fixpt_depth is fixed-point approximation (with 8 fractional bits) of the distance between the farthest contour point and the hull. That is, to get the floating-point value of the depth will be fixpt_depth/256.0.


### Math for calculating the angles between fingers

     for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])
         
        # calculating the angle using cosine formula
        
            a = math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
            b = math.sqrt((-start[0] + far[0]) ** 2 + (-start[1] + far[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b**2 + c**2 - a**2) / (2*b*c)))*57

            if angle <= 90:
                count_defects += 1
                cv2.circle(crop_image, far, 1, [0, 0, 255], -1)
            cv2.line(crop_image, start, end, [0, 255, 0], 2)
        
Two fingers will create a angle less than 90 deg between them, Thus we count the number of angles less than 90 in the contours and add one to get the number of fingers. 

## Author(s)

Sohil Khan
<br> Github Username: sohil1234

