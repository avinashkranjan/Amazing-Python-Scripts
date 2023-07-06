import cv2

face_cascade = cv2.CascadeClassifier(
    "./Face-Detection/v3/haarcascade_frontalface.xml")


def detect():
    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray, 1.1, 4)
        a = len(face)
        font = cv2.FONT_HERSHEY_SIMPLEX
        if a <= 1:
            cv2.putText(img, f"{a} face detected", (15, 350),
                        font, 2, (255, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(img, f"{a} faces detected", (15, 350),
                        font, 2, (255, 0, 0), 2, cv2.LINE_AA)

        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Face Detect", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press q to quit
            break

    cap.release()
    cv2.destroyAllWindows()


detect()
