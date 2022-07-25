# sync_subs

Script to use the subsync [library](https://github.com/smacke/ffsubsync)

# Usage:

Right click on any video file or files, send to sync_subs.cmd.

The script assumes the subtitle is in the same location and the same name as the video .srt

The output replaces the old subtitle.

(you can change any of this behaviour inside the script)

# Requirements:

-Windows. (just for the send to part)

-Python 3.

# Setup:

```
pip install -r requirements.txt
```

Download the sync_subs.py file.

On windows "Ctrl+R" and run "shell:sendto"
this will open the "send to" directory so we can add our bash script.

To run the python script you must create sync_subs.cmd (this name will show on the send to menu)

sync_subs.cmd script that sends the path of the selected file or files to our python script

```
@echo off
cls
python3 path_to_script\sync_subs.py %*
pause
```

Ps:
In case of errors, please remember to have "windows build tools" installed.
