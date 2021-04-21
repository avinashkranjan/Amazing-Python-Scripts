import cv2

# Load the Cascade Classifier
body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
videopath = input("Enter the video Path : ")
# Capture the video
cap = cv2.VideoCapture(videopath)

while True:

    # read image from video
    response, frame = cap.read()

    if response == False:
        break

    # Convert to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the full body
    faces = body_cascade.detectMultiScale(gray_img, 1.1, 1)

    # display rectangle
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # display video
        cv2.imshow('img', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Enter q to quit
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
