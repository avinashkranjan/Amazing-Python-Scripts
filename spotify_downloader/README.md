- Downloads music from Spotify as an MP3 file.
- Applies basic on metadata like track name, track number, album, genre and more.
<br><br>
You need to download ffmpeg to use this tool, download it from:
1. [MacOs](https://evermeet.cx/ffmpeg/)
2. [Windows](https://www.gyan.dev/ffmpeg/builds/)
3. [Linux](https://johnvansickle.com/ffmpeg/)
4. [Central Release Page](https://ffmpeg.org/download.html)
<br><br>
# Installation
```
pip install -r requirements.txt
```
   OR
```
pip3 install -r requirements.txt 
```
# Usage
To download a song run,

    python3 spotify.py $trackUrl
    python3 spotify.py https://open.spotify.com/track/08mG3Y1vljYA6bvDt4Wqkj?si=SxezdxmlTx-CaVoucHmrUA

To download an album run,
    
    python3 spotify.py $albumUrl
    python3 spotify.py https://open.spotify.com/album/2YMWspDGtbDgYULXvVQFM6?si=gF5dOQm8QUSo-NdZVsFjAQ

To download a playlist run,
    
    python3 spotify.py $playlistUrl
    python3 spotify.py https://open.spotify.com/playlist/37i9dQZF1DWXhcuQw7KIeM?si=xubKHEBESM27RqGkqoXzgQ
