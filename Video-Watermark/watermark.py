from cv2 import cv2

# take the input video
cap = cv2.VideoCapture('videos/input.mp4')

# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_width, frame_height)

# get the frame rate of the input video
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'videos/output' file.
result = cv2.VideoWriter('videos/output.avi', cv2.VideoWriter_fourcc(*'MJPG'),
                         fps, size)

print("processing started...")

# continue till the video is not over...
while (cap.isOpened()):

    # Capture frame-by-frame from the video
    ret, frame = cap.read()
    if ret == True:

        # describe the type of font to be used.
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Use putText() method for inserting text on video
        # Parameters:-
        # frame: current running frame of the video.
        # Text: The text string to be inserted.
        # org: bottom-left corner of the text string
        # font: the type of font to be used.
        # color: the colour of the font.
        # thickness: the thickness of the font

        cv2.putText(frame, 'HELLO WORLD', (50, 50), font, 1, (0, 255, 255), 2,
                    cv2.LINE_4)
        # write in the output file
        result.write(frame)

        # Display the resulting frame
        cv2.imshow('video', frame)

        # creating 'q' as the quit button for the video
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release the cap object
cap.release()
result.release()

# close all windows
cv2.destroyAllWindows()

print("Video successfully saved inside the videos folder")
