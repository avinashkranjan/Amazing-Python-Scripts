# DownTube.

DownTube is an on-to-go downloader for any bundle of Youtube links you want to download. Make it be a single video, an entire playlist, or even a file that contains a couple of youtube links.

# Setup Instructions

The script depends on Pytube and Regex libraries to do Its work.

> pip3 install regex pytube

Download the script from Github, or you can clone the whole repository.

> git clone https://github.com/avinashkranjan/Amazing-Python-Scripts

# Usage

1) For downloading a single video, use "-u \<link>" or "--url \<link>" argument.
> python3 DownTube.py -u https://www.youtube.com/watch?v=D6VnOIgnLr8
2) For downloading a complete playlist, add the "-p" or "--playlist" flag.
> python3 DownTube.py -u https://www.youtube.com/playlist?list=PLsRxtLB5dnMaX54r-INR_HQlDtNomT_xa -p
3) For downloading urls from a text file, use the "-f \<path>" or "--file \<path>" argument.
> python3 DownTube.py -f C:\file.txt
4) For downloading only the audio source add the "-a" or "--audio-only" flag.
> python3 DownTube.py -f C:\file.txt -a

# Output

Download Videos and Audio from Youtube, so that a user can enjoy it offline.

# Authors

Written by <a href="https://github.com/XZANATOL" target="_blank">XZANATOL</a>

Mentored by <a href="https://github.com/avinashkranjan" target="_blank">Avinash Kr. Ranjan</a>

This project was built under the mentorship of <a href="https://gssoc.girlscript.tech/" target="_blank">GSSOC21</a>

# Notes

1) You can't pass -f and -u arguments at the same time. only use one at a time.
2) If a file that exists has the same name of a file to be downloaded, the current file WILL NOT be overwritten.
3) Use double quotes on links and file_paths when using Windows CMD.