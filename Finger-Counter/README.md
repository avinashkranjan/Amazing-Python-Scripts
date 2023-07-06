# Finger Counter using hand tracking

We will first look into hand tracking and then we will use the hand landmarks to count the fingers and all of this will be happening in real time.

A system which detects a human hand, segments the hand, counts the number of fingers being held up and displays the finger count, from a live video input.

## Dependencies
- OpenCV
- Mediapipe

<br>

## Hand tracking in real time

We will first write the bare minimum code to run and then learn how to convert it into a module.
The framework we will be using is called the `media pipe` which is developed by google, they created these amazing models that allow us to quickly get started with some of the very fundamental problems such as face detection, facial landmarks hand tracking object detection and quite a bit more of these as well.

<br>

It uses two main modules at the back end so one of them is the palm detection and the other one is hand landmarks now the palm detection basically works on complete image and it basically provides a cropped image of the hand from there the hand landmark module finds 21 different landmarks on this cropped image of the hand to train this hand landmark they manually annotated 30,000 images of different hands so that is a lot of work and this is one of the reasons it works so well and the best part is that it is cross platform and we do not have to dive deep into the sea of configurations and installations so within just two clicks we will be up and running.

<br>

![hand_landmarks](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png)

<br>

So let's have a look.

The first thing we will do here, `import cv2` and then we will `import media pipe as mp` and then we will `import time` so this is to check the frame rate so first we are going to create our video object. This is basically what we always do to run a webcam. Now, we are going to detect a hand so the first thing we have to do is we have to create an object from our class hands and getting the values of these different points or the landmarks is a little bit tricky but we will create a module so that we can just say I want the point number five of the hand so tell me the location so that will become quite easy to use.

<br>

Now this is you can say a formality that you have to do before you can start using this model so you will write `mp.solutions.hands` and then we have to create an object called hands, so here the first thing is the static image mode, they have this configuration where they will track and detect so if you put this as false then sometimes it will detect and sometimes it will track based on the confidence level but if you put it as static mode then the whole time it will do the detection part which will make it quite slow so we will keep it false so that it detects and if it has a good tracking confidence it will keep tracking so this way it will be much faster whenever the tracking confidence goes lower than a certain range then it will do the detection again.

<br>

Then you have the maximum number of hands, so here we have two and then we have the minimum detection confidence so this is 50 and then minimum tracking confidence which is 50, so it means if it goes below 50 it will do the detection again.

<br>

Then in the loop we are going to send in our rgb image to this object, we have to first convert it so we will write `imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`. So this is our idea that we want to convert it into rgb because this class or this object only uses rgb images so we need to convert that first so we will write that `results = hands.process(imgRGB)`. So there is a method inside this object called process that will process the frame for us and it will give us the results so that's how simple this is. Now all we need to know is how to extract this information and use it.

<br>

Then we are going to open this object up the one that we have received and we are going to extract the information within so as we have seen the parameters we can have multiple hands so what we can do is we can extract these multiple hands and we will have to put in a for loop to check if we have multiple hands or not and we have to extract them one by one. Now before we do that we have to make sure that there is something in the results so we can print out the results and we can run it.

<br>

To check if something is detected or not we can write `if self.results.multi_hand_landmarks:` . We will have each hand and then we will get the information or extract the information of each hand so once we do that we have a method provided by the media pipe that actually helps us draw all these points because there are a lot of them.

<br>

## Finger counter

Firstly, there is folder here you can see that it says `FingerImages` so basically what this isthat we have the images of different fingers so when it is one, two, three, four, five, and one it is zero so for simplicity we are just going to
use these six scenarios but if you want to add more later on you can do that and it will pretty much use the same code and you can keep adding on to it.

<br>

The first thing we will do is to import our cv2 the opencv library then we will import time and also import os.

<br>

Now the first thing, we will turn on our webcam so here we will write `cap = cv2.VideoCapture(1)`. Then you have the option of giving the size so we need to define the width and height so the width of the cam and the height of the camera is equals to 640 by 480.

<br>

Then we have to write our while loop, inside that at the end we have to give it a delay so `cv2.waitKey(1)` this will give it a one millisecond delay so that we can see our images. 

<br>

Next we are going to do something new here and that will be to import our images so what we need to do is we need to get them one by one and then we want to store them so that later on whenever we have the certain amount of fingers shown then we can display that image. For that we need to store them first so how do you store it, you will use `os`, we can do is we can write `myList = os.listdir(folderPath)`. We want to list all the files that are present in finger images so we will say that our `folderPath = "FingerImages"`.

<br>

To create a list of images, we can say list of images or let's say overlay because we want to overlay this image on our main image. Now we can loop through our list so we can say that for image path in our list we want to create (we want to import) our image so we will write `image = cv2.imread(f'{folderPath}/{imPath}')`.

<br>

Now we have imported it but we didn't save it so we need to save it in our list so we will say `overlayList.append(image)` and that will give us our image list. Now to confirm that everything is working fine we can write here length of our overlay list and we can write `print` so if that list is six then we should be good to go and there you go.
