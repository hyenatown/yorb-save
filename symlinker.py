# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023

#Includes
import json
from os import path, symlink, curdir
from shutil import move
from psutil import disk_usage

# TODO: If the operation lasts longer than two seconds, display a progress bar. Find out what module could print a progress bar.
# TODO: Check if paths have enough disk space to perform a switcheroo. 

# Simply asks the user to put in a path.
# Path of the 'working directory' - a.k.a. where the files and index are
archive_path = path.abspath(curdir)
# The path to the file being moved and symlinked.
origin_path = input('Please enter the origin path:')
# The working directory again, however, formatted so the original file name acts as the final destination.
dest_path = path.join(archive_path, '') + path.basename(origin_path)

############################################################################################
# Exits with error if remaining disk space is only 2%.
# TODO: Exit if the remaining disk space is larger than the working directory free space.
############################################################################################
if disk_usage(archive_path).percent > 98:
    exit("Insufficent space in archive location to continue. Exiting.")
else:
    print('Moving file(s), creating symlink...')

# TODO: Imports the index.json
def file_tracker_read():
    file_index = open(index.json, 'r')
    json.loads(file_index)
    file_index.close()

# TODO: Saves the index.json (overwrites)
def file_tracker_delete():
    file_index = open('index.json', 'w')
    json.dumps(file_index)
    file_index.close()

# Move the origin to the destination, and then replace the origin with a symlink.
move(origin_path,dest_path)
symlink(dest_path,origin_path)
print('Done!')
print('Symlink created at: ' + origin_path)
exit()