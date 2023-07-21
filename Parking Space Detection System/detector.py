import argparse
import cv2
import numpy as np
import pickle
from pathlib import Path
from shapely.geometry import Polygon as shapely_poly
from mrcnn.model import MaskRCNN
import mrcnn.utils
import mrcnn.config
import os
import sys
import time


class Config(mrcnn.config.Config):
    NAME = "model_config"
    IMAGES_PER_GPU = 1
    GPU_COUNT = 1
    NUM_CLASSES = 81


def download_model_weights(model_path):
    if not os.path.exists(model_path):
        print("Downloading pre-trained weights...")
        mrcnn.utils.download_trained_weights(model_path)


def load_parking_regions(regions_path):
    regions_file = Path(regions_path)
    if regions_file.exists():
        with open(regions_file, 'rb') as f:
            parked_car_boxes = pickle.load(f)
            return parked_car_boxes
    else:
        print("Error: Could not find the regions file.")
        sys.exit(1)


def get_car_boxes(boxes, class_ids):
    cars = []
    for i, box in enumerate(boxes):
        if class_ids[i] in [3, 8, 6]:
            cars.append(box)
    return np.array(cars)


def compute_overlaps(parked_car_boxes, car_boxes):
    new_car_boxes = []
    for box in car_boxes:
        y1, x1, y2, x2 = box
        p1 = (x1, y1)
        p2 = (x2, y1)
        p3 = (x2, y2)
        p4 = (x1, y2)
        new_car_boxes.append([p1, p2, p3, p4])

    overlaps = np.zeros((len(parked_car_boxes), len(new_car_boxes)))
    for i, park_area in enumerate(parked_car_boxes):
        for j, car_box in enumerate(new_car_boxes):
            polygon1_shape = shapely_poly(park_area)
            polygon2_shape = shapely_poly(car_box)

            polygon_intersection = polygon1_shape.intersection(
                polygon2_shape).area
            polygon_union = polygon1_shape.union(polygon2_shape).area
            iou = polygon_intersection / polygon_union
            overlaps[i][j] = iou

    return overlaps


def draw_parking_area(frame, parking_area, color=(71, 27, 92), thickness=2):
    cv2.drawContours(frame, [np.array(parking_area)],
                     contourIdx=-1, color=color, thickness=thickness)


def draw_overlay(frame, overlay, alpha):
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)


def process_video(video_path, regions_path, output_path):
    parked_car_boxes = load_parking_regions(regions_path)

    config = Config()
    model = MaskRCNN(mode="inference", model_dir=model_dir, config=config)
    model_path = os.path.join(model_dir, "mask_rcnn_coco.h5")
    download_model_weights(model_path)
    model.load_weights(model_path, by_name=True)

    alpha = 0.6
    video_capture = cv2.VideoCapture(video_path)
    video_FourCC = cv2.VideoWriter_fourcc(*'XVID')
    video_fps = video_capture.get(cv2.CAP_PROP_FPS)
    video_size = (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                  int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(output_path, video_FourCC, video_fps, video_size)

    while video_capture.isOpened():
        success, frame = video_capture.read()
        if not success:
            break

        start_time = time.time()
        rgb_image = frame[:, :, ::-1]
        results = model.detect([rgb_image], verbose=0)
        inference_time = time.time() - start_time

        cars = get_car_boxes(results[0]['rois'], results[0]['class_ids'])
        overlaps = compute_overlaps(parked_car_boxes, cars)

        overlay = frame.copy()

        for park_area, overlap_areas in zip(parked_car_boxes, overlaps):
            max_iou_overlap = np.max(overlap_areas)
            if max_iou_overlap < 0.15:
                draw_parking_area(overlay, park_area)

        draw_overlay(frame, overlay, alpha)
        cv2.putText(frame, f"Inference Time: {inference_time:.2f}s", (
            10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv2.imshow('Parking Space Detection', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    out.release()
    cv2.destroyAllWindows()
    print("Output saved as", output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('video_path', help="Video file")
    parser.add_argument('regions_path', help="Regions file")
    parser.add_argument(
        '--output', '-o', help="Output file", default="output.avi")
    args = parser.parse_args()

    video_path = args.video_path
    regions_path = args.regions_path
    output_path = args.output

    process_video(video_path, regions_path, output_path)
