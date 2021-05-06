import cv2
import label_image

size = 4


# We load the xml file
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

webcam = cv2.VideoCapture(0)  # Using default WebCam connected to the PC.

while True:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)  # Flip to act as a mirror

    # Resize the image to speed up detection
    mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))

    # detect MultiScale / faces
    faces = classifier.detectMultiScale(mini)

    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
        cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 4)

        # Save just the rectangle faces in SubRecFaces
        sub_face = im[y:y+h, x:x+w]

        # Saving the current image from the webcam for testing.
        FaceFileName = "test.jpg"
        cv2.imwrite(FaceFileName, sub_face)

        # Getting the Result from the label_image file, i.e., Classification Result.
        text = label_image.main(FaceFileName)
        text = text.title()  # Title Case looks Stunning.
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(im, text, (x+w, y), font, 1, (0, 0, 255), 2)

    # Show the image
    cv2.imshow('Capture',   im)
    key = cv2.waitKey(10)
    # if Esc key is press then break out of the loop
    if key == 0:  # The Esc key
        break
