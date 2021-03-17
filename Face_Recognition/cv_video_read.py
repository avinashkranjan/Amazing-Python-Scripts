# Read a video Stream from Camera  ( Frame by frame )

import cv2
cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	if ret==False:
		continue
	
	cv2.imshow("Video Frame", frame)
	cv2.imshow("gray frame", gray_frame)

	# wait for user inqut -q, then u will stop the loop

	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
