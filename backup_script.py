import os
import time
from zipfile import ZipFile, ZIP_DEFLATED

# progress bar for any iterable
def progressbar(it, prefix="", size=60):
    count = len(it)
    start = time.time()
    def show(j):
        x = int(size*j/count)
        remaining = ((time.time() - start) / (j if j != 0 else 0.1)) * (count - j)        
        mins, sec = divmod(remaining, 60) # limited to minutes
        time_str = f"{int(mins):02}:{sec:03.1f}"
        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count} est. {time_str}{' '*10}", end='\r', flush=True)
    show(0) # show initial state
    for i, item in enumerate(it):
        yield item
        show(i+1)

# recursively add a directory to a zip
def zipdirectory(zip: ZipFile, dir_path: str):
    file_level = len(list(os.walk(dir_path))) <= 99 # display progressbar on file-level if there are not many subdirectories
    for dir, _, files in os.walk(dir_path) if file_level else progressbar(list(os.walk(dir_path)), f"zipping \"{dir_path}\": "):
        if len(files) > 0: # skip folders that only contain folders
            for file in progressbar(files, f"zipping \"{os.path.normpath(dir)}\": ") if file_level else files:
                zip.write(os.path.normpath(os.path.join(dir, file)))
            if file_level: print() # finish progressbar
    if not file_level: print()

# create a zip from a list of paths
def createzip(zip_path: str, paths: list, comp_level: int=1):
    # assert compression level is valid (0 - 9, fastest - smallest)
    assert 0 <= comp_level <= 9, "compression level must be an integer in [0, 9]"

    # remove zip if it already exists
    if os.path.exists(zip_path):
        os.remove(zip_path)

    # create zip
    with ZipFile(zip_path, 'w', compression=ZIP_DEFLATED, compresslevel=comp_level) as zip:
        for path in paths: # add paths
            if os.path.isdir(path): # path is a directory
                zipdirectory(zip, path)
            else: # path is a file
                print(f"zipping \"{path}\"")
                zip.write(path)
    
    # verify that zip was created
    assert os.path.exists(zip_path), f"{zip_path} was not created!"
    print(f"saved {zip_path}")

if __name__ == "__main__":
    # -------------- #
    # YOUR CODE HERE #
    # -------------- #

    # EXAMPLE:
    createzip("backup.zip", [
        "C:/Documents/Work", # adds everything in this directory
        "C:/Documents/Schedule.csv" # only adds this file
    ], comp_level=9) # maximum compression, slowest

    createzip("backup.zip", [ # replaces the previous zip
        "C:/Documents", # adds everything, including subdirectories
    ], comp_level=0) # minimum compression, fastest
