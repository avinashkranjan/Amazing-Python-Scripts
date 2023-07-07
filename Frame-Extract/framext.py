import os
from os import path
import math
import cv2
import argparse


class Extractor:
    """Extract frames from video file and saves them in a directory

    Arguments:
            vid_filename {str} -- Location of video file
            output_dir {str} -- Output directory to store frames


    """

    global args

    def __init__(self, vid_filename, output_dir, verbose=False):

        self.verbose = verbose
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        print(self.output_dir)
        if path.exists(vid_filename):
            self.vid_filename = vid_filename
        else:
            raise FileNotFoundError(f"File {vid_filename} not found")

        # initialize video capture
        self.cap = cv2.VideoCapture(self.vid_filename)

        # get video fps
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

        # Video length in frames
        self.vid_length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def extractor(self):
        is_ok, frame = self.cap.read()
        count = 0
        print(self.fps)
        while is_ok:
            # is_ok, frame = self.cap.read()
            print(
                f"Extracting frame {count} of {self.vid_length-1}") if self.verbose else {}
            # save current frame
            cv2.imwrite(os.path.join(
                self.output_dir, f"{count}.jpg"), frame)
            print("COMPLETED") if count == self.vid_length-1 else {}

            is_ok, frame = self.cap.read()

            count += 1

    def extract_frames(file):
        global args

        # check whether file is greather than 0 bytes using path
        if os.stat(path.join(args.input_dir, file)).st_size > 0:
            # extract frames
            extractor = Extractor(path.join(args.input_dir, file), path.join(
                args.output_dir, file), args.sampling_rate)
            extractor.extractor()
        else:
            print(f"File {file} is empty")


def main():
    # setup parsers for CLI arguments
    parser = argparse.ArgumentParser("Frame Extractor")
    parser.add_argument("-i", "--video_file", type=str,
                        help="Location of video file", required=True)
    parser.add_argument("-o", "--output_dir", type=str,
                        help="Output directory to store frames", required=True)
    parser.add_argument("-v", "--verbose", type=bool,
                        help="Display details of extraction of frames", default=False)
    args = parser.parse_args()
    # print(args)
    # Extract frames from video file
    if args.video_file:
        name = args.video_file.split(".")[0]
        ext = args.video_file.split(".")[1]
        if ext != "mp4":
            raise argparse.ArgumentTypeError(
                f"File {args.video_file} is not a video(.mp4) file")
        output_dir = os.path.join(args.output_dir, name)
        extract = Extractor(args.video_file, args.output_dir,  args.verbose)
        extract.extractor()


if __name__ == '__main__':
    main()
