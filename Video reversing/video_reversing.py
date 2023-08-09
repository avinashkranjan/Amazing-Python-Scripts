import cv2
import tkinter as tk
from tkinter.filedialog import *

window = tk.Tk()
window.title("Video reversing")
window.geometry('400x200')
label = tk.Label(window, text="Input video file should be in the current folder").grid(
    row=0, column=0)
label = tk.Label(
    window, text="Output/reversed video file is saved in the current folder").grid(row=1, column=0)
label = tk.Label(window, text="Close this dialog box to proceed").grid(
    row=3, column=0)
window.mainloop()


cap = cv2.VideoCapture('sampleVideo.mp4')

frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
size = (int(width*0.5), int(height*0.5))

# defining/writing the output video and its format
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('sampleOutput.mp4', fourcc, fps, size)

print("No. of frames: ", frames)
print("FPS: ", fps)

frameIdx = frames - 1
if (cap.isOpened()):
    # printing the progress
    print("Progress:\n")
    while (frameIdx != 0):  # iterating from last frame to first
        cap.set(cv2.CAP_PROP_POS_FRAMES, frameIdx)  # pointing to last frame
        ret, frame = cap.read()
        frame = cv2.resize(frame, size)
        frameIdx = frameIdx - 1
        if (frameIdx % 100 == 0):  # progress updated every 100 frames
            print(frameIdx)
        out.write(frame)

out.release()
cap.release()
cv2.destroyAllWindows()
