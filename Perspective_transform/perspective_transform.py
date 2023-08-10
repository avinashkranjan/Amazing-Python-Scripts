import cv2
import numpy as np
import tkinter as tk
from tkinter.filedialog import *

photo = askopenfilename()  # reading the input image
img = cv2.imread(photo)
img = cv2.resize(img, (500, 500))

window = tk.Tk()
window.title("Perspective transform")
window.geometry('350x200')


# pts1 is an array storing coordinates of 4 points on the original image
pts1 = np.float32([[103, 97], [390, 93], [85, 351], [412, 352]])
# pts2 is an array storing coordinates of 4 positions where the above points should be after the transformation
pts2 = np.float32([[103, 97], [390, 93], [133, 400], [390, 400]])

Mat = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, Mat, (500, 500))

label = tk.Label(window, text="Points chosen on original image: " +
                 str(pts1)).grid(row=0, column=1)
label = tk.Label(window, text="Points on transformed image: " +
                 str(pts2)).grid(row=1, column=1)
label = tk.Label(window, text="The coordinates can be changed in the code ").grid(
    row=2, column=1)
# displaying the images
cv2.imshow("Original Image", img)
cv2.imshow("Transformed Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

window.mainloop()
