# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Distribution, copying, or forking is still to be determined, so cool your jets.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.

#Includes
import os
import shutil

# TODO: Currently doesn't copy files between devices because you need shutil to do that.

# Simply asks the user to put in a path. FIXME: Replace dest_name with working directory later on.
origin_name = input('Please enter the path of the ORIGIN file or directory:')
dest_name = input('Please enter the path of the DESTINATION file or directory:')

# TODO: Check if paths have enough disk space to perform a switcheroo. 
# Exits with error if remaining space is only 5% bigger than the total size of the files(s).
# Skipped if same-filesystem.

#Print if the checks pass.
print('Moving file(s), creating symlink...')

# TODO: Copy information regarding the original file (permissions, ownership, attributes) to the Archive's file-tracker-JSON.
# TODO: Find a module that makes reading JSON files EZ.
# TODO: I really need to come up with a better name than 'Archive'.
# Exits with error if it somehow can't access or edit the JSON.

# TODO: If the operation lasts longer than two seconds, display a progress bar.
# TODO: Find out what module could print a progress bar.

# Move the origin to the destination, and then replace the origin with a symlink.
# shutil.move(origin_name,dest_name) # TODO: Replace below line with this after reading up on it.
os.rename(origin_name,dest_name)
os.symlink(dest_name,origin_name)
print('Done!')
print('Symlink created at: ' + origin_name)
exit()