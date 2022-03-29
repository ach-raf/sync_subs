import subprocess
import sys
import os
import shutil


CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def sync_subs_srt(_reference_srt, _unsync_srt, _output):
    _command = [
        shutil.which("ffs"),
        {_reference_srt},
        "-i",
        {_unsync_srt},
        "-o",
        {_output},
    ]
    subprocess.call(_command)


def sync_subs_audio(_path):
    # using subsync library to do the magic
    _command = [
        shutil.which("ffs"),
        rf"{_path}",  # path to the video
        "-i",
        rf"{_path[:-4]}.srt",  # the subtitle for input, using the same name as the film + .srt
        "-o",
        rf"{_path[:-4]}.srt",  # the output replaces the original subtitle
        "--encoding",
        "utf-8",
    ]  # encoding
    subprocess.call(_command)


def main():
    _paths = sys.argv[1:]  # list of arguments sent to the script
    for _path in _paths:
        clean_path = os.path.normpath(_path)
        sync_subs_audio(clean_path)


if __name__ == "__main__":
    main()
