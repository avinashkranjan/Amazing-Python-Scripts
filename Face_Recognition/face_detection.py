# Read a video Stream from Camera  ( Frame by frame )

import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")  # classifier
while True:
	ret, frame = cap.read()    # we read 1 img 
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	if ret==False:
		continue
# now we read the img
										# (gray_frame, scaling factor, no of neighbors)
	faces = face_cascade.detectMultiscale(gray_frame,1.3,5)   # 1.3 means img will shrink by 30% 
 	cv2.imshow("Video Frame",frame)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		# (frame , coordinates , opposite coordinate of rect , color , boundries)
	key_pressed = cv2.waitKey(1) & 0xFF  # wait for user inqut -q, then u will stop the loop
	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()




""" Scaling Factor -- parameter specifying how much the image size is reduced at each image scale. Basically the scale factor is used to create your scale pyaramid. 
1.05 is a good possible value for this, which means you use a small step for resizing i.e. reduce size

Min Neighh -- Parameter specifying how many neigh each candidate rectangle should have to retain it.
this parameter will affect the quality of the detected faces. Higher value results in less detection but with higher quality. 3~6 is a good value for it. """

''' detectMultiscale() - if the imag has 2 faces then this method going to returns the coordinates, the starting of the face (x1,y1), width, height 
then there are multiple faces present then it will return tuple of [(x,y,w,h)] '''