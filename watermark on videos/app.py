import cv2
import numpy as np

def add_watermark(input_video_path, output_video_path, watermark_path, position=(10, 10)):
    video_capture = cv2.VideoCapture(input_video_path)
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)
    watermark_height, watermark_width, _ = watermark.shape
    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video = cv2.VideoWriter(output_video_path, fourcc, 30.0, (frame_width, frame_height))

    while True:
        ret, frame = video_capture.read()

        if not ret:
            break

        resized_watermark = cv2.resize(watermark, (frame_width // 4, frame_height // 4))
        roi = frame[position[1]:position[1] + resized_watermark.shape[0], position[0]:position[0] + resized_watermark.shape[1]]

        if watermark.shape[2] == 4:
            mask = resized_watermark[:, :, 3]
            mask_inv = cv2.bitwise_not(mask)
            img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
            img_fg = cv2.bitwise_and(resized_watermark[:, :, :3], resized_watermark[:, :, :3], mask=mask)
            dst = cv2.add(img_bg, img_fg)
            frame[position[1]:position[1] + resized_watermark.shape[0], position[0]:position[0] + resized_watermark.shape[1]] = dst

        else:
            frame[position[1]:position[1] + resized_watermark.shape[0], position[0]:position[0] + resized_watermark.shape[1]] = resized_watermark[:, :, :3]

        output_video.write(frame)

    video_capture.release()
    output_video.release()

    print("Watermark added successfully!")


add_watermark('input_video.mp4', 'output_video_with_watermark.mp4', 'watermark.png')
