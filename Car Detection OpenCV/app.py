import cv2
import numpy as np


yolo_net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')


class_names = []
with open('coco.names', 'r') as f:
    class_names = f.read().strip().split('\n')


video_capture = cv2.VideoCapture('video_file.mp4')

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        break

    height, width, _ = frame.shape

   
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    yolo_net.setInput(blob)

    layer_names = yolo_net.getUnconnectedOutLayersNames()
    outs = yolo_net.forward(layer_names)

    for out in outs:
        for detection in out:
            scores = detection[5:]

            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 2: 
                center_x = int(detection[0] * width)

                center_y = int(detection[1] * height)
                bbox_width = int(detection[2] * width)

                bbox_height = int(detection[3] * height)

                x = int(center_x - bbox_width / 2)
                y = int(center_y - bbox_height / 2)
                cv2.rectangle(frame, (x, y), (x + bbox_width, y + bbox_height), (0, 255, 0), 2)

                
    resized_frame = cv2.resize(frame, (720, 480))

    cv2.imshow('Car Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
