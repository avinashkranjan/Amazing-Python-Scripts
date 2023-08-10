import cv2
import numpy as np
import tkinter as tk
from tkinter.filedialog import *

photo = askopenfilename() # reading the input image
img = cv2.imread(photo)
rows, columns, ch = img.shape
window = tk.Tk() 
window.title("Perspective transform")
window.geometry('350x200')


# pts1 is an array storing coordinates of 3 points on the original image
pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 is an array storing coordinates of 3 positions where the above points should be after the transformation
pts2 = np.float32([[10,100],[200,50],[100,250]])

Mat = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img, Mat, (500,500))

label = tk.Label(window, text="Points chosen on original image: " + str(pts1)).grid(row=0, column=1)
label = tk.Label(window, text="Points on transformed image: " + str(pts2)).grid(row=1, column=1)
label = tk.Label(window, text="The coordinates can be changed in the code ").grid(row=2, column=1)
# displaying the images
cv2.imshow("Original Image", img)
cv2.imshow("Transformed Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

window.mainloop()
