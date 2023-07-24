import os
import cv2

def convert_frames_to_video(img_folder_path, fps):
    images = [os.path.join(img_folder_path, img) for img in os.listdir(img_folder_path)]

    frame = cv2.imread(images[0])
    height, width, layers = frame.shape

    video_name = input("Enter the video name(just the filename): ").strip()
    if not video_name.endswith(".avi"):
        video_name += ".avi"

    video = cv2.VideoWriter(video_name, 0, fps, (width, height))

    for image in images:
        video.write(cv2.imread(image))

    cv2.destroyAllWindows()
    video.release()

if _name_ == "_main_":
    img_folder_path = input("Enter the folder path containing images: ").strip()
    fps = int(input("Enter the fps needed: "))
    convert_frames_to_video(img_folder_path, fps)