# Face and Eye Detection
import cv2

# PATH of the FILE
CLASSIFIER_PATH = "./Facedetection/v2/haarcascade_frontalface_default.xml"
EYEDETECTION_PATH = "./Facedetection/v2/haarcascade_eye.xml"

# Live video capturing
cam = cv2.VideoCapture(0)

# Initializing classifier
face_classifier = cv2.CascadeClassifier(CLASSIFIER_PATH)
EYE_DETECTION = cv2.CascadeClassifier(EYEDETECTION_PATH)

while (True):

    _, frame = cam.read()

    # Converting to grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Returns coordinates of all faces in the frame
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    # Cycle through each coordinate list
    for (x, y, w, h) in faces:

        # Extracting mid points of bounding box
        mid_x = int(x + h/2)
        mid_y = int(y + h/2)

        # Drawing - "bounding box"
        frame = cv2.rectangle(frame, (x, y), (x + h, y + h), (255, 0, 0), 2)
        # 'x-coordinate' on live feed
        frame = cv2.putText(frame, str(x), (x, y),
                            cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 255), 2)
        # "." represent mid part in face
        frame = cv2.putText(frame, ".", (mid_x, mid_y),
                            cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 255), 2)

        # Detects The Eyes
        eyes = EYE_DETECTION.detectMultiScale(gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex, ey), (ex+eh, ey+eh), (0, 255, 0), 2)

    # Displaying video feed with detected faces
    cv2.imshow('Frame', frame)

    # Reading for keyboard interrupts
    key = cv2.waitKey(1)
    if (key == 27):
        break

cam.release()
cv2.destroyAllWindows()
