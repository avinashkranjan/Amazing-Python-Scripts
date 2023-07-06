import cv2
import numpy as np

# drawn act as a flag variable to see if ROI has been selected or not
drawn = False
ix, iy = -1, -1
# To store ROI values
rectangle = (0, 0, 0, 0)


def open_image(path):
    """
    It opens the image when a valid path is given.
    :param path: image location path
    :return:
    """
    img = cv2.imread(path)
    dim = (512, 512)
    resized_image = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized_image


# mouse callback function
def draw_rectangle(event, x, y, flags, params):
    """
    Its a mouse callback function called automatically whenever
    any event is happened on the image that is clicking any button on
    mouse or keyboard.
    """
    global ix, iy, drawn, rectangle
    if event == cv2.EVENT_LBUTTONDOWN:
        # When you click DOWN with left mouse button
        # Then we take note of where that mouse was located
        ix, iy = x, y
        cv2.circle(img, (ix, iy), 4, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        # Once you lift the mouse button
        # we complete the rectangle ie ROI is selected.
        drawn = True
        rectangle = (ix, iy, x - ix, y - iy)
        print("\nROI Selected Successfully!")


def background_sub(image):
    """
    This function:
    1. Takes image as input and
    2. Asks user to select ROI by dragging mouse pointer.
    3. Performs background subtraction.
    4. Displaying the updated image.
    5. Saving the processed image in your current directory.

    GrabCut Algorithm is used
    link : https://www.geeksforgeeks.org/python-foreground-extraction-in-an-image-using-grabcut-algorithm/

    :param image: Image on which Background subtraction is to be performed.
    :return:
    """
    global drawn

    # This names the window so we can reference it
    cv2.namedWindow(winname='BG Subractor')
    # Connects the mouse button to our callback function
    cv2.setMouseCallback('BG Subractor', draw_rectangle)

    print("\nSelect ROI from mouse pointer.")

    # Creating mask, background and foregound models for Grabcut Algorithm
    black_mask = np.zeros(image.shape[:2], np.uint8)
    background = np.zeros((1, 65), np.float64)
    foreground = np.zeros((1, 65), np.float64)

    while True:  # Runs forever until we break with Esc key on keyboard

        # If ROI is selected
        if drawn:
            print("\nPerforming Background Subtraction")
            # Using Grabcut Algorithm only when ROI is drawn and saved in
            # variable named rectangle
            cv2.grabCut(image, black_mask, rectangle,
                        background, foreground,
                        5, cv2.GC_INIT_WITH_RECT)

            # mask with 1 and 4 denotes foreground
            # mask with 2 and 0 denotes background so converting the bg pixels into black
            mask2 = np.where((black_mask == 2) | (
                black_mask == 0), 0, 1).astype('uint8')

            # multiplying mask2 with original image so that we can get our resultant
            image = image * mask2[:, :, np.newaxis]

            # For saving the file
            cv2.imwrite('Bg_removed.jpg', image)
            print(f'\nBg_removed.jpg saved in your current directory!')
            print('Great Success!!!')

            # Once the processing has been done setting drawn to False
            drawn = False

        # Shows the resultant image in image window
        cv2.imshow('BG Subractor', image)

        # Press ESC to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # It closes all windows (just in case you have multiple windows called)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    loc = input('Enter image path: ')
    img = open_image(loc)
    background_sub(img)
