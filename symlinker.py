# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
from os import path, symlink, curdir, remove
from shutil import move
from psutil import disk_usage
import json

# TODO: If the operation lasts longer than two seconds, display a progress bar; Find out what module could print a progress bar.
# TODO: Add exception for linking to a path WITHIN archive_path.
# TODO: Add exception when a linked path is trying to be linked a second time.
# TODO: Exit if the path is larger than the working directory free space.
# TODO: Ask if user wants to link another file before trying to exit.
# TODO: Make a -y switch maybe, or better yet just skipping to the part where the input is automagic.

# Exits with error if remaining disk space is only 2%.
def add_symlink():
    archive_path = path.abspath(curdir)
    if disk_usage(archive_path).percent > 98:
        exit("Insufficent space in current location to continue. Exiting.")
    else:
        origin_path = input('Please enter the origin path:')
        dest_path = path.join(archive_path, '') + path.basename(origin_path)
        move(origin_path,dest_path)
        symlink(dest_path,origin_path)
        print('Done!\a')   
        exit('Symlink created at: ' + origin_path)

# TODO: Not finished pseudocode thing. Do not use.
def remove_symlink():
    if disk_usage(archive_path).percent > 98:
        exit("Insufficent space in current location to continue. Exiting.") # <-- This is fine.
    else:
        json.loads(thing_to_load) 
        unlink_question = print("Do you want to restore {} to its original location? Y/N:")
        if unlink_question == "yes" or "Y": # <-- What?
            move((archive_path + path.basename(origin_path)), origin_path)

