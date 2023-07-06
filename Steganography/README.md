# Steganography

* Steganography is the method of hiding secret data in any image/audio/video.
* This Python Script Can hide text under image and can retrive from it with some simple commands

## Setup Instructions
* install OpenCV using following command

```
pip install opencv-python
```
* using following commands to encode and decode Images
```
python steganography.py <image_file> --encode
python steganography.py <image_file> --decode
python steganography.py -h   
```
## Detailed Explanation of Script
Each letter is represented using 8bits, or 1 byte. Each pixel in the image has three bits, one each for RGB frames. Each pixel can hold 3 bits. We will encode three pixels together, making a place for 9 bits. Out of the 9 bits, we will store 1 letter in the 8 bits and one (End Of File)EOF bit. If the EOF bit is high, then it indicates that the end of the message has been reached. Otherwise, it indicates the program to read more pixels for decoding.