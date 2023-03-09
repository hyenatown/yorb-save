# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.

#Includes
import os
import json
from shutil import move
from psutil import disk_usage

# TODO: If the operation lasts longer than two seconds, display a progress bar. Find out what module could print a progress bar.
# TODO: Check if paths have enough disk space to perform a switcheroo. 

# Simply asks the user to put in a path.
# Path of the 'working directory' - a.k.a. where the files and index are
archive_path = os.path.abspath(os.curdir)
# The path to the file being moved and symlinked.
origin_path = input('Please enter the path of the ORIGIN file or directory:')
# The working directory again, however, formatted so the original file name acts as the final destination.
dest_path = os.path.join(archive_path, '') + os.path.basename(origin_path)

############################################################################################
# Exits with error if remaining disk space is only 2%.
# TODO: Exit if the remaining disk space is larger than the working directory free space.
############################################################################################
if disk_usage(archive_path).percent > 98:
    exit("Insufficent space in archive location to continue. Exiting.")
else:
    print('Moving file(s), creating symlink...')

# TODO: Tracks a file
def file_tracker_add():
    file_index = open(index.json, 'a')
    pass
    file_index.close()

# TODO: Reads the tracked file list
def file_tracker_read():
    file_index = open(index.json, 'r')
    pass
    file_index.close()

# TODO: Deletes an existing entry
def file_tracker_delete():
    file_index = open('index.json', 'a')
    pass
    file_index.close()

# Move the origin to the destination, and then replace the origin with a symlink.
move(origin_path,dest_path)
os.symlink(dest_path,origin_path)
print('Done!')
print('Symlink created at: ' + origin_path)
exit()