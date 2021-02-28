import cv2
import time

imgcapture = cv2.VideoCapture(0)
result = True

while (result):
    ret, frame = imgcapture.read()
    name = int(round(time.time() * 1000))
    name = 'E:/Python-Programs/PythonProjects/WebCam/Images-Captured/{}.jpg'.format(
        name)
    cv2.imwrite(name, frame)
    result = False
    print("Image Captured.. ")

imgcapture.release()
