import cv2
import time
import os
import HandTrackingModule as htm

class fingerCounter():
    def __init__(self):
        self.wCam = 640
        self.hCam = 480
        self.folderPath = "./Finger-Counter/FingerImages"
        self.previousTime = 0
        #self.currentTime = time.time()
        # 4 for thumb, 8 for index, 12 for middle, 16 for ring, 20 for pinky finger
        self.tipIds = [4, 8, 12, 16, 20]
        self.overlayList = []
        self.image_read(self)
        self.process(self, self)

    def image_read(self, overlayList):
        myList = os.listdir(self.folderPath)
        print(myList)

        for imPath in myList:
            image = cv2.imread(f'{self.folderPath}/{imPath}')
            self.overlayList.append(image)
        print(len(self.overlayList))

    def process(self, tipIds, overlayList):
        cap = cv2.VideoCapture(0)
        cap.set(3, self.wCam)
        cap.set(4, self.hCam)
        detector = htm.handDetector(detectionCon=0.75)
        while True:
            success, img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw = False)
            print(lmList)

            if len(lmList) != 0:
                fingers = []

                # Thumb
                if lmList[self.tipIds[0]][1] > lmList[self.tipIds[0] - 1][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                # Four fingers
                for id in range(1,5):
                    if lmList[self.tipIds[id]][2] < lmList[self.tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                totalFingers = fingers.count(1)
                print(totalFingers)

                h, w, c = self.overlayList[totalFingers - 1].shape
                img[0:h, 0:w] = self.overlayList[totalFingers - 1]
                cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
            
            self.currentTime = time.time()
            fps = 1/(self.currentTime - self.previousTime)
            self.previousTime = self.currentTime

            cv2.putText(img, f'FPS: {int(fps)}', (400,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            cv2.imshow("Image", img)
            
            if cv2.waitKey(1) == ord('q') : 
                break
                
cv2.destroyAllWindows()

if __name__ == "__main__":
    counter = fingerCounter()
