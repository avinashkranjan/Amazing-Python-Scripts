# DownTube is a Youtube Video/Audio downloader script written by XZANATOL
# https://www.github.com/XZANATOL
# source code can be found on https://github.com/avinashkranjan/Amazing-Python-Scripts
from pytube.cli import on_progress
from pytube import YouTube, Playlist
from optparse import OptionParser
import sys
import os
import re

# Help menu
usage = """
<Script> [Options]

[Options]:
  -h, --help        show this help message and exit.
  -a, --audio-only  Flag to download only the audio source (True/Flase).
  -p, --playlist    Playlist flag if the provided link is a playlist not a single video.
  -u, --url         Parameter used to add Youtube link.
  -f, --file        Parameter used to add file that contains some Youtube links.

Notes:
1) You can't pass both -f and -u at the same time.
2) If a file that exists has the same name of a file to be downloaded, the current file WILL NOT be overwritten.
"""

# load args
parser = OptionParser()
parser.add_option("-a", "--audio-only", action="store_true", dest="only_audio",
                  help="Flag to download only the audio source (True/Flase).")
parser.add_option("-p", "--playlist",   action="store_true", dest="playlist",
                  help="Playlist flag is the provided link is a playlist not a single video.")
parser.add_option("-u", "--url", dest="url",
                  help="Parameter used to add Youtube link.")
parser.add_option("-f", "--file", dest="file",
                  help="Parameter used to add file that contains some Youtube links.")

pattern = r'res="([0-9]+)p"'  # used for checking available resolutions


def choice_single_link(links):
    """Walkthorugh algorithm if -p/--playlist flag is False"""
    try:
        links = YouTube(links, on_progress_callback=on_progress)
    except:
        raise "Can't verify link, check internet connectivity/provided link."

    if only_audio:  # if -a/--audio-only flag is True
        count = audio_download([links])  # function accepts a list of urls
    else:
        count = is_vid([links])  # function accepts a list of urls

    return count


def choice_playlist(links):
    """Walkthorugh algorithm if -p/--playlist flag is True"""
    try:
        links = Playlist(links)
    except:
        raise "Can't verify playlist, check internet connectivity/provided link."

    if only_audio:  # if -a/--audio-only flag is True
        count = audio_download(links.videos)
    else:
        count = is_vid(links.videos)

    return count


def file_handler(path):
    """Reads file that contains Youtube links and downloads them"""
    try:
        with open(path, "r") as file:
            i = 0  # counter for items
            for line in file.readlines():
                if not "youtube" in line or not line.rstrip("\n"):
                    continue
                choice_single_link(line.rstrip("\n"))
                i += 1
        return i
    except:
        raise "Can't open file, check provided path/read permissions."


def is_vid(lst):
    """Filtering function for video downloading"""
    # Instead of filtring the video on each approach (playlist or single_vid or file scraping),
    # This function takes care of the video filtering for all approaches,
    # Just feed her a list of streams and watch the magic. :D

    # this loop to check the available resolutions for 1 vid (one will apply for all)
    resolutions_mp4 = []
    resolutions_webm = []
    for i in lst:
        mp4_res = i.streams.filter(progressive=True, file_extension="mp4")
        for res in mp4_res:
            resolutions_mp4.append(re.search(pattern, str(res))[1])

        webm_res = i.streams.filter(progressive=True, file_extension="webm")
        for res in webm_res:
            resolutions_webm.append(re.search(pattern, str(res))[1])
        break

    print("Select one of the available resolutions:")
    print("mp4:", resolutions_mp4)
    print("webm:", resolutions_webm)
    ext, res = input("[extension] [resolution] > ").split(" ")

    # check input
    if not res in resolutions_mp4+resolutions_webm or not ext in ["mp4", "webm"]:
        raise "Invalid Input..."

    return video_download(lst, ext, res)


def audio_download(objct):  # objct is a list of urls
    """Function that downloads provided streams as audios"""
    i = 0  # counter for items
    for aud in objct:
        print("Downloading: " + aud.title)
        aud.register_on_progress_callback(on_progress)  # show progress bar
        try:
            aud.streams.filter(type="audio").order_by(
                "abr").desc().first().download()
            i += 1
        except:
            pass
        print()  # add a blank line to seperate intersecting progress bars

    return i


def video_download(objct, ext, res):  # objct is a list of urls
    """Function that downloads provided streams as videos"""
    i = 0  # counter for items
    for vid in objct:
        print("Downloading: " + vid.title)
        vid.register_on_progress_callback(on_progress)  # show progress bar
        try:
            stream = vid.streams.filter(
                progressive=True, type="video", resolution=res+"p", file_extension=ext).order_by("abr").desc()

            if len(stream) == 0:  # That if condition is for in case any videos in the playlist doesn't offer the same stream resolution (common in Mix playlists)
                print(
                    "Couldn't find available resolution for the video, Downloading with the best available one")
                stream = vid.streams.filter(progressive=True, type="video", file_extension=ext).order_by(
                    "resolution").desc().order_by("abr").desc()

            stream.first().download()
            i += 1
        except:
            pass
        print()  # add a blank line to seperate intersecting progress bars

    return i


def check_Download_folder():
    """Checks if Donwloads folder exists.. If not, then it will create one."""
    if os.path.exists("Downloads/"):
        os.chdir("Downloads/")
    else:
        try:
            os.mkdir("Downloads")
        except:
            raise "Couldn't create 'Downloads' folder, Check write permissions"
        os.chdir("Downloads/")


# Start checkpoint
if __name__ == "__main__":
    (options, args) = parser.parse_args()

    # flags
    only_audio = options.only_audio
    playlist = options.playlist
    link = options.url
    file = options.file

    # validate arguments
    if not bool(link) ^ bool(file):  # xor gate
        print(usage)
        sys.exit()

    # prepare Downloads directory
    check_Download_folder()

    if link:
        if playlist:
            count = choice_playlist(link)
        else:
            count = choice_single_link(link)
    else:
        count = file_handler(file)

    # print a small report
    print("\n[+]Downloaded {} items".format(count))
