Short script for easily adding a mix of files and directories to a zip folder.
Directories are added recursively, meaning all files and subdirecties (and the subdirectories in there...) are added to the zip.

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
