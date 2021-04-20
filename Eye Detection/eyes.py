
import cv2


capture = cv2.VideoCapture(0)  # To open camera 1

if (capture.isOpened() == False):
    print("Sorry")
while(capture.isOpened()):

    # Load trained cascade classifier
    ret, color_image = capture.read()
    eye_cascade = cv2.CascadeClassifier('./Eye Detection/haarcascade_eye.xml')

    # Convert color image into grayscale
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # Detect Eyes
    eyes = eye_cascade.detectMultiScale(gray_image, 1.1, 5)
    # Count the number of eyes
    a = str(len(eyes))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(color_image, a+" eyes detected", (15, 350),
                font, 2, (0, 0, 0), 2, cv2.LINE_AA)
    # Draw rectangle around the eyes
    for (x, y, w, h) in eyes:
        cv2.rectangle(color_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show image
    cv2.imshow('Image', color_image)
    cv2.imwrite('detect.png', color_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
