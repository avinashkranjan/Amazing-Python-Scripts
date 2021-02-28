# How To Download Audio Of A YouTube Video?

1. Setup python and pip if you haven’t already

2. Install virtualenv

`pip install virtualenv`

3. Create Virtual environment

`virtualenv venv`

4. Activate virtual environment

- `source venv/bin/activate` (Linux)
- `venv\Scripts\activate` (Windows)

5. Install requirements

`pip install -r requirements.txt`

6. Specify url of the YouTube video whoose audio you want (in YouTubeAudioDownloader.py)

ex: `url = "https://www.youtube.com/watch?v=ZSXN_dpG5jk"`

7. Run YouTubeAudioDownloader.py

![YouTubeAudioDownloader.py Output](https://i.postimg.cc/htwd362f/Output.png)

You will find file of .webm format downloaded in the same folder.

## How To convert .webm to .mp3 format?

1. Install moviepy in the same environment

`pip install moviepy==1.0.3`

2. Specify path of .webm file (in WebmToMp3.py)

ex: `clip = mp.AudioFileClip("C:/Users/sejal/Desktop/YouTube Audio Downloader/Rainbow.webm").subclip()`

3. Specify path where .mp3 file should be saved (in WebmToMp3.py)

ex: `clip.write_audiofile("C:/Users/sejal/Desktop/YouTube Audio Downloader/rainbow.mp3")`

4. Run WebmToMp3.py

![YouTube Audio Downloader Folder](https://i.postimg.cc/zG3h78Ss/Folders.png)
