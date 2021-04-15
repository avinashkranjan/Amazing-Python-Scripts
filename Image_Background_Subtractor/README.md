# Image Background Subtraction using OpenCV.

This python script lets you remove background form image by keeping only foreground in focus. 
By using [Grabcut Algorithm](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_grabcut/py_grabcut.html) it makes easy to do the task.

We make use of OpenCV, numpy libraries of Python.

This Script: 
1. Takes image as input and
2. Asks user to select ROI by dragging mouse pointer.
3. Performs background subtraction.
4. Displaying the updated image.
5. Saving the processed image in your current directory.

![Gif](https://media.giphy.com/media/DZCjZKyNHzsOktHqvI/giphy.gif)

## Setting up:

- Create a virtual environment and activate it.

- Install the requirements

```sh
  $ pip install -r requirements.txt
```

## Running the script:

```sh
  $ python BG_Subtractor.py
```

1. Enter valid file location/path.
2. Select ROI by using mouse pointer on the window <b>BG Subractor</b>.
3. Then script will process the image.
4. Image <b>Bg_removed.jpg</b> will be stored in your current directory.

![Gif](https://media.giphy.com/media/GVxM1xt46gDS5biPSr/giphy.gif)


## Output:
![Image](https://i.imgur.com/SCf4XRj.jpg)

## Author
[🛡 Akhil Bhalerao 🛡 ](https://linktr.ee/iamakkkhil)