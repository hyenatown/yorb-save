# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
from os import path, symlink, curdir, remove, makedirs
from shutil import move
from psutil import disk_usage

def add_symlink():
	archive_path = path.abspath(curdir)
	if int(disk_usage(archive_path).percent) > 98:
		exit("Insufficent space in current location to continue. Exiting.")
	else:
		origin_path = input('Please enter the origin path:')
		determined_origin_dir_name = "dummy" # TODO: Create additional method that creates a name based on stuff like location and date.
		dest_path = path.join(archive_path, 'vault', determined_origin_dir_name, '')
		dest_file = dest_path + path.basename(origin_path)
		path_exists = path.exists(dest_path)
		if path_exists is False:
			makedirs(dest_path)
		move(origin_path,dest_file)
		symlink(dest_file,origin_path)
		print('Done!\a')   
		exit(f'Symlink created at: {origin_path}')
