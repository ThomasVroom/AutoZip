Short python script for easily adding a mix of files and directories to a zip folder.
Directories are added recursively, meaning all files and subdirecties (and the subdirectories in there, etc.) are added to the zip.

Wanted to automate the process of creating backups of certain files and folders, but found there was no simple tool that supported (1) both files and directories, and (2) recursively adding subdirectories.
This script should do the trick.

### Example Usage
```python
createzip("backup.zip", [
    "C:/Documents/Work", # adds everything in this directory
    "C:/Documents/Schedule.csv" # only adds this file
], comp_level=9) # maximum compression, slowest

createzip("backup.zip", [ # replaces the previous zip
    "C:/Documents", # adds everything, including subdirectories
], comp_level=0) # minimum compression, fastest
```
