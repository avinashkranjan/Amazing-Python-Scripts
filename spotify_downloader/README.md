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
## Usage (Instructions for v3)

- To download a song, run:

  ```
  $ spotdl [trackUrl]
  ```

  ex. `spotdl https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b?si=1stnMF5GSdClnIEARnJiiQ`


- To download an album, run:

  ```
  $ spotdl [albumUrl]
  ```

  ex. `spotdl https://open.spotify.com/album/4yP0hdKOZPNshxUOjY0cZj?si=AssgQQrVTJqptFe7X92jNg`


- To download a playlist, run:

  ```
  $ spotdl [playlistUrl]
  ```

  ex. `spotdl https://open.spotify.com/playlist/37i9dQZF1E8UXBoz02kGID?si=oGd5ctlyQ0qblj_bL6WWow`


- To search for and download a song, run, __with quotation marks__:  
  _Note: This is not accurate and often causes errors._

  ```
  $ spotdl '[songQuery]'
  ```

  ex. `spotdl 'The Weeknd - Blinding Lights'`


- To resume a failed/incomplete download, run:

  ```
  $ spotdl [pathToTrackingFile]
  ```

  ex. `spotdl 'The Weeknd - Blinding Lights.spotdlTrackingFile'`

  _`.spotdlTrackingFile`s are automatically created when a download starts and deleted on completion_


You can queue up multiple download tasks by separating the arguments with spaces:

```
$ spotdl [songQuery1] [albumUrl] [songQuery2] ... (order does not matter)
```

ex. `spotdl 'The Weeknd - Blinding Lights' https://open.spotify.com/playlist/37i9dQZF1E8UXBoz02kGID?si=oGd5ctlyQ0qblj_bL6WWow ...`



_spotDL downloads up to 4 songs in parallel, so for a faster experience, download albums and playlist, rather than tracks._
