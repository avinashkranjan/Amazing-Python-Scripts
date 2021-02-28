import cv2
img_file = "Human.jpg"
# trained human data  Link:"https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_fullbody.xml"
classifier_Human = 'car_dect.xml'
img = cv2.imread(img_file)  # create image reader
# convert image black and white i.e. grayscale
black_and_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Human_detect = cv2.CascadeClassifier(classifier_Human)  # create classifier
humans = Human_detect.detectMultiScale(black_and_white)  # detect cars

for (
        x, y, w, h
) in cars:  # the above variable will return 4 cordinates i.e height,width,postionx,positiony
    # this loop will create grren rectangle when car is detected
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow('Human image', img)  # display image
cv2.waitKey()
