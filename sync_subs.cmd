@echo off
cls
cmd /k "cd /d C:\path_to_virtualenv\venv\Scripts & activate & cd /d    C:\path_to\sync_subs & python sync_subs.py %*
pause

