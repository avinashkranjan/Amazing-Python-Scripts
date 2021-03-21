import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")


def detect():
    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Face Detect", img)

        if cv2.waitKey(1) == 27:
            break

    cap.release()


detect()
