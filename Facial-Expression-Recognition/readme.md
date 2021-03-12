# Facial Expression Recognition
***


Facial expression recognition is a technology which detects emotions in human faces. More precisely, this technology is a sentiment analysis tool and is able to automatically detect the basic or universal expressions: happiness, sadness, anger, surprise, fear, and disgust etc.


## Dependencies


<code>
    pip install tensorflow
    pip install opencv-python
</code>


## Implementation of OpenCV HAAR CASCADES


Here "Frontal Face Alt" Classifier is used for detecting the presence of Face in the WebCam.
then, load this file which can be found in the label.py


<code>
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
</code>


## ReTraining the Network - Tensorflow Image Classifier


Create an Image classifier that identifies whether a person is sad, happy and so on and then show this text on the OpenCV Window.

- Create a directory named images. In this directory, create six sub directories with names like Happy, Sad, Angry, Surprise, Fear and Disgust.
- Now fill these directories with respective images by downloading them from the Internet or take your own pictures(atleast 100). E.g., In "Happy" directory, fill only those iages of person who are happy.
- Now run the "face-crop.py" program.
- Once you have only cleaned images, you are ready to retrain the network.To run the training, hit the go to the parent folder and open Terminal here and hit the following:


<code>
    python retrain.py --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --architecture=MobileNet_1.0_224 --image_dir=images
</code>


## Importing the ReTrained Model and Setting Everything Up


Now run the "label.py" program by typing the following in Terminal:


<code>
    python label.py
</code>


It will open a new window of OpenCV and then identifies your Facial Expression. ##You can express your emotions and get the results.##


[![Facial-Expression-Recognition](https://i1.wp.com/sefiks.com/wp-content/uploads/2018/01/kid-expressions-cover.png?resize=560%2C9999&ssl=1)]

## Author

[Debashish kumar sahoo](https://github.com/Debashish-hub)