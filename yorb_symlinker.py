# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet ready to be released.
# THIS CODE SHALL NOT BE USED FOR ANY TYPE OF GENERATIVE MODEL TRAINING.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
from os import path, symlink, curdir, remove, makedirs, rmdir
from shutil import move
from psutil import disk_usage
import yorb_indexer
import datetime
import sqlite3


def create_archive():
    vault_path = path.abspath(curdir)
    if int(disk_usage(vault_path).percent) > 98:
        print("Insufficent space in current location to continue. Exiting.")
        exit(1)
    else:
        archive_name = input("Give your archive a name, or just press ENTER:")
        if archive_name == "":
            archive_name = (
                datetime.datetime.now().isoformat(timespec="minutes").replace(":", "-")
            )
        origin_path = input("Please enter the origin path:")
        origin_path = origin_path.strip("'")
        origin_path = origin_path.strip('"')
        dest_path = path.join(vault_path, "archive", archive_name, "")
        dest_file = dest_path + path.basename(origin_path)
        dest_file_basename = path.basename(origin_path)
        path_exists = path.exists(dest_path)
        if path_exists is False:
            makedirs(dest_path)
        move(origin_path, dest_file)
        symlink(dest_file, origin_path)
        current_date_time = datetime.datetime.now()
        archive_db_record = (
            archive_name,
            origin_path,
            dest_file,
            current_date_time,
        )
        yorb_indexer.add_archive_record(archive_db_record)
        print("Done!\a")
        print(f"Symlink created at: {origin_path}")


def delete_archive():
    vault_path = path.abspath(curdir)
    if int(disk_usage(vault_path).percent) > 98:
        print("Insufficent space in current location to continue. Exiting.")
        exit(1)
    else:
        if yorb_indexer.fetch_all_archives() == False:
            return
        else:
            archive_db_record = input("Select Archive to remove:")
            archive_db_record_entry = yorb_indexer.fetch_selected_archive_record(
                archive_db_record
            )
            vault_path = archive_db_record_entry[2]
            origin_path = archive_db_record_entry[1]
            remove(origin_path)
            move(vault_path, origin_path)
            rmdir(path.dirname(vault_path))  # TODO: Errno 39 Directory Not Empty
            # if path.exists(vault_path) == True: # Something like this where there's a
            #     rmdir(path.dirname(vault_path)) # check for contents before executing.
            print(f"File restored to: {origin_path}")
            yorb_indexer.delete_archive_record(archive_db_record)


def check_archive_files():
    vault_path = path.abspath(curdir)
    if int(disk_usage(vault_path).percent) > 98:
        print("Insufficent space in current location to continue. Exiting.")
        exit(1)
    else:
        c = sqlite3.connect("yorb.db")
        cc = c.cursor()
        cc.execute("SELECT * FROM archive")
        fa = cc.fetchall()
        print("DEBUG: " + str(fa))
        for row in enumerate(fa):
            q = row[1]
            print(f"DEBUG:" + q[2])
            path.exists(q[2])
        c.close()


def debug_create_dummy_archive_record():
    archive_name = "null"
    dest_file_basename = "null"
    dest_file = "null"
    current_date_time = datetime.datetime.now()
    archive_db_record = (archive_name, dest_file_basename, dest_file, current_date_time)
    yorb_indexer.add_archive_record(archive_db_record)
