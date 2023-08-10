import cv2
import numpy as np
import tkinter as tk
from tkinter.filedialog import *

window = tk.Tk()
window.title("Border extraction")
window.geometry('300x100')
label = tk.Label(window, text="Choose an image").grid(row=0, column=0)

photo = askopenfilename()
img = cv2.imread(photo)
n, l, m = img.shape
size = (n, l)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold_value = 20  # this value needs to be adjusted for every image
ret, thresh = cv2.threshold(gray, threshold_value, 255, 0)

kernel = np.ones((5, 5), np.uint8)
# dilation and erosion are applied to binary images
dilated = cv2.dilate(thresh, kernel, iterations=1)
eroded = cv2.erode(thresh, kernel, iterations=1)

bordered = dilated - eroded
bordered = cv2.resize(bordered, size)
cv2.imshow("Border/outline", bordered)
cv2.imwrite("Output.png", bordered)
cv2.waitKey(0)
cv2.destroyAllWindows()

window.mainloop()
