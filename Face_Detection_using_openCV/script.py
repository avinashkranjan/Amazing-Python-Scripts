
import time
from datetime import datetime

import cv2
import pandas

video = cv2.VideoCapture(0)
first_frame = None
status_list = [None, None]
time = []
df = pandas.DataFrame(columns=["Start", "End"])
cnts = [[0, 0], [255, 0], [255, 255], [0, 255]]
while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if first_frame is None:
        first_frame = gray
        continue
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_data = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_data, None, iterations=5)
    (cnts, _) = cv2.findContours(thresh_data.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0:
        time.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        time.append(datetime.now())
    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_data)
    cv2.imshow("Colour Frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            time.append(datetime.now())
        break


print(time)
for i in range(0, len(time), 2):
    df = df.append({"Start": time[i], "End": time[i+1]}, ignore_index=True)
df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows
