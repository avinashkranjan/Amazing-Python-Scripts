import os
import numpy as np
import cv2
import pickle
import argparse
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.widgets import PolygonSelector
from matplotlib.collections import PatchCollection
from shapely.geometry import box
from shapely.geometry import Polygon as shapely_poly

points = []
prev_points = []
patches = []
total_points = []
breaker = False


class SelectFromCollection(object):
    def __init__(self, ax):
        self.canvas = ax.figure.canvas

        self.poly = PolygonSelector(ax, self.onselect)
        self.ind = []

    def onselect(self, verts):
        global points
        points = verts
        self.canvas.draw_idle()

    def disconnect(self):
        self.poly.disconnect_events()
        self.canvas.draw_idle()


def break_loop(event):
    global breaker
    global globSelect
    global savePath
    if event.key == 'b':
        globSelect.disconnect()
        if os.path.exists(savePath):
            os.remove(savePath)

        print("Data saved in " + savePath + " file")
        with open(savePath, 'wb') as f:
            pickle.dump(total_points, f, protocol=pickle.HIGHEST_PROTOCOL)
        exit()


def onkeypress(event):
    global points, prev_points, total_points
    if event.key == 'n':
        pts = np.array(points, dtype=np.int32)
        if points != prev_points and len(set(points)) == 4:
            print("Points: " + str(pts))
            patches.append(Polygon(pts))
            total_points.append(pts)
            prev_points = points


def process_video(video_path, out_file):
    global globSelect
    global savePath
    savePath = out_file if out_file.endswith(".p") else out_file + ".p"

    print("\n> Select a region in the figure by enclosing it within a quadrilateral.")
    print("> Press the 'f' key to go full screen.")
    print("> Press the 'esc' key to discard the current quadrilateral.")
    print("> Try holding the 'shift' key to move all of the vertices.")
    print("> Try holding the 'ctrl' key to move a single vertex.")
    print("> After marking a quadrilateral, press 'n' to save the current quadrilateral, and then press 'q' to start marking a new quadrilateral.")
    print("> When you are done, press 'b' to exit the program.\n")

    video_capture = cv2.VideoCapture(video_path)
    cnt = 0
    rgb_image = None
    while video_capture.isOpened():
        success, frame = video_capture.read()
        if not success:
            break
        if cnt == 5:
            rgb_image = frame[:, :, ::-1]
        cnt += 1
    video_capture.release()

    fig, ax = plt.subplots()
    image = rgb_image
    ax.imshow(image)

    p = PatchCollection(patches, alpha=0.7)
    p.set_array(10 * np.ones(len(patches)))
    ax.add_collection(p)

    globSelect = SelectFromCollection(ax)
    bbox = plt.connect('key_press_event', onkeypress)
    break_event = plt.connect('key_press_event', break_loop)
    plt.show()
    globSelect.disconnect()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('video_path', help="Path of the video file")
    parser.add_argument(
        '--out_file', help="Name of the output file", default="regions.p")
    args = parser.parse_args()

    video_path = args.video_path
    out_file = args.out_file

    process_video(video_path, out_file)
