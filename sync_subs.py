import subprocess
import sys

_paths = sys.argv[1:]  # list of arguments sent to the script
for _path in _paths:
    # using subsync library to do the magic
    _command = ['ffs',
                _path,  # path to the video
                '-i', f'{_path[:-4]}.srt',  # the subtitle for input, using the same name as the film + .srt
                '-o', f'{_path[:-4]}.srt',  # the output replaces the original subtitle
                '--encoding', 'utf-8']  # encoding
    subprocess.run(_command)


