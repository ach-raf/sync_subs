import subprocess
import sys

_paths = sys.argv[1:]
for _path in _paths:
    _command = ['ffs',
                _path,
                '-i', f'{_path[:-4]}.srt',
                '-o', f'{_path[:-4]}.srt',
                '--encoding', 'utf-8']
    subprocess.run(_command)


