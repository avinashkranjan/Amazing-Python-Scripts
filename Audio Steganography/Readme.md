# Audio Steganography

## Description

Here, you can see two diffrent scripts 1. endcoder.py and 2. decoder.py. First, talking about the encoder.py. This script is used to hide the data in the audio by LSB algorithm. First user is requested to enter the file name and then secret message after that script will generate endcoded audio file. Second, decoder.py is used to decode the msg from the encoded audio file. In this script user is requested to enter the name of audio file and script will automatically decode the secret msg in it. Here, I atteched one sample audio file iphone.mp3 .

## Dependencies

In my work, i used pydub (to convert .mp3 file .wav file) and wave (to read and write .wav file). In most of the python installation wave is already installed. So, That you don't have to install it. Installation for pydub given below. While, working with the conversion. I faced one issue regarding that, ffmpeg is not found (in Ubuntu 20.04). If you find the same issue. you can go for second installation in next segment.

## Installation

Installation of pydub.
```bash
pip install pydub
```

Installation of ffmpeg (If required).
```bash
sudo apt install ffmpeg
```

## How to run

To run Encoder File.
```bash
python3 encoder.py
```

To run decoder File.
```bash
python3 decoder.py
```



