import moviepy.editor as pyeditor
import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("-v", "--videoFile", required=True,
                        help="Video Filename with the complete path.")
arg_parser.add_argument('-p', "--path", required=True,
                        help="Audio Filename with absolute or relative path")

args = vars(arg_parser.parse_args())

try:
    Video_clip = pyeditor.VideoFileClip(r"{}".format(args['videoFile']))
    Video_clip.audio.write_audiofile(r"{}".format(args['path']))
except Exception:
    print("Error!!! Something is worng.")
