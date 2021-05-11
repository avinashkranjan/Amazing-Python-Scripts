## ORB Algorithm
In this script, we would use the **ORB(Oriented FAST Rotated Brief)** algorithm of `Open CV` for recognition and matching the features of image.

ORB is a fusion of the FAST keypoint detector and BRIEF descriptor with some added features to improve the performance. FAST is Features from the Accelerated Segment
Test used to detect features from the provided image. It also uses a pyramid to produce multiscale features. Now it doesn’t compute the orientation and descriptors for
the features, so this is where BRIEF comes in the role.

## Setup Instructions
- You need to install `OpenCV` and `Python` in your machine.

## Output
<img src="https://i.ibb.co/6Y8Z04s/Robert-input.png" width=400/> <img src="https://i.ibb.co/J7z8nqT/Robert-feature.png" width=400/>
<img src="https://i.ibb.co/XCJjYYW/output-ORB.png"/>

## Author
[Shubham Gupta](https://github.com/ShubhamGupta577)
