# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import json
from os import path, symlink, curdir
from shutil import move
from psutil import disk_usage

# TODO: If the operation lasts longer than two seconds, display a progress bar; Find out what module could print a progress bar.
# TODO: Add exception for linking to a path WITHIN archive_path.
# TODO: Add exception when a linked path is trying to be linked a second time.
# TODO: Exit if the path is larger than the working directory free space.

# Exits with error if remaining disk space is only 2%.
archive_path = path.abspath(curdir) # Defines the working directory
if disk_usage(archive_path).percent > 98:
    exit("Insufficent space in archive location to continue. Exiting.")
else:
    origin_path = input('Please enter the origin path:')    # Path being moved and symlinked.
    dest_path = path.join(archive_path, '') + path.basename(origin_path)    # Working dir + path basename.
    print('Moving file(s), creating symlink...')

# JSON Import/Export
def file_tracker_read(): # TODO: Import
    file_index = open(index.json, 'r')
    json.loads(file_index)
    file_index.close()
def file_tracker_delete(): # TODO: Export (overwrites)
    file_index = open('index.json', 'w')
    json.dumps(file_index)
    file_index.close()

# Move the origin to the destination, and then replace the origin with a symlink.
move(origin_path,dest_path)
symlink(dest_path,origin_path)
print('Done!')
print('Symlink created at: ' + origin_path)
exit()