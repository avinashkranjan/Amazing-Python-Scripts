# Number plate detection

## Methodology:

License plate of the vehicle is detected using various features of image processing library openCV and recognizing the text on the license plate using python tool named as tesseract.

To recognize the license plate we are using the fact that license plate of any vehicle has rectangular shape. So, after all the processing of an image we will find the contour having four points inside the list and consider it as the license plate of the vehicle.
 
</br>

## Dependencies
- OpenCV
- Numpy and Pandas
- [Tesseract 4](https://github.com/tesseract-ocr/tesseract/wiki)

</br>

## Preprocessing

Grayscale images are much easier to work within a variety of tasks like In many morphological operations and image segmentation problems, it is easier to work with the single-layered image (Grayscale image)than a three-layered image (RGB color image ).

</br>

After gray scaling we will blur the gray image to reduce the background noise. I had used the bilateral filter to blur the image because it actually preserves all strength, it removes noise quite well and strengthens the edges in the image when we deal with a single-layered image.

</br>

After blurring we will do edge detection. Canny Edge Detection follows the series of steps and is a very powerful edge detection method. We will use the Canny edge detection to extract the edges from the blurred image because of its optimal result, well-defined edges, and accurate detection.

</br>

After finding edges we will find the contours from and edged image. There are mainly two important types of contours Retrieval Modes. The first one is the `cv2.RETER_LIST`  which retrieves all the contours from an image and second is `cv2.RETER_EXTERNAL`  which retrieves external or outer contours from an image. There are two types of Approximation Methods. The first method is the `cv2.CHAIN_APPROX_NONE`  stores all the boundary points. But we don't necessarily need all bounding points. If the points form a straight line, we only need the start and ending points of that line. The second method is the `cv2.CHAIN_APPROX_SIMPLE`  instead only provides these start and endpoints of bounding contours, thus resulting in much more efficient storage of contour information.

</br>

After finding contours we will sort the contours. Sorting contours is quite useful when doing image processing. We will sort contours by area which will help us to eliminate some small and useless contours made by noise and extract the large contours which contain the number plate of a vehicle.

</br>

## Detecting Plate

After we sort the contours we will now take a variable plate and store a value none in the variable recognizing that we did not find number plate till now. Now we iterate through all the contours we get after sorting from the largest to the smallest having our number plate in there so we should be able to segment it out. Now to that, we will look through all the contours and going to calculate the perimeter for the each contour. Then we will use `cv2.approxPolyDP()`  function to count the number of sides. 

</br>

The `cv2.approxPolyDP()`  takes three parameters. First one is the individual contour which we wish to approximate. Second parameter is Approximation Accuracy Important parameter is determining the accuracy of the approximation. Small values give precise- approximations, large values give more generic approximation. A good rule of thumb is less than 5% of the contour perimeter. Third parameter is a Boolean value that states whether the approximate contour should be open or closed.

</br>

I had used contour approximation and it approximate a contour shape to another shape with less number of that is dependent on the position I specify so the 0.02 is the precision that worked.

</br>

## Usage

- `data.csv`  contains the date, time and vehicle license number.
- Tesseract is a library which uses OCR engine.
- Tesseract contain more than hundred languages to choose, if you want to change:
  - Open `number_plate.py` and change the `config` variable.
  - In `config` variable change **'eng'** to your preferred language.
- Use Tesseract 4 as this is the latest version which uses LSTM network.

</br>

Run the following:

    python number_plate.py
    
 
