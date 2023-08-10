import cv2
import numpy as np
import tkinter as tk
from tkinter.filedialog import *


window = tk.Tk()
window.title("Object finding")
window.geometry('400x100')
label = tk.Label(window, text="Choose an image first and then the object to be found in it").grid(row=0, column=0)
label = tk.Label(window, text="Output is stored in this folder").grid(row=1, column=0)

photo = askopenfilename()
img = cv2.imread(photo)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

temp = askopenfilename()
template = cv2.imread(temp, cv2.IMREAD_GRAYSCALE)
w,h = template.shape[::-1]

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(result>=threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w, pt[1]+h), (0,0,255), 1)

cv2.imshow("output", img)
cv2.imwrite('output.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
window.mainloop()
