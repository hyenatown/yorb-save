# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet ready to be released.
# THIS CODE SHALL NOT BE USED FOR ANY TYPE OF GENERATIVE MODEL TRAINING.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import os
import json
import sqlite3
import yorb_symlinker
import yorb_indexer

def situ_test():
    if os.path.exists("settings.json") is True:
        pass
    else:
        defaults = {"firstrun": True, "archive_loc": "archive", "vault_loc": "vault"}
        dir_fd = os.open(".", os.O_RDONLY)
        def opener(path, flags):
            return os.open(path, flags, dir_fd=dir_fd)
        with open("settings.json", "w", opener=opener) as f:
            print(json.dumps(defaults), file=f)
        os.close(dir_fd)

    if os.path.exists("yorb.db") is True:
        pass
    else:
        c = sqlite3.connect("yorb.db")
        cc = c.cursor()
        cc.execute("""CREATE TABLE "archive" (
    	"archive_name"	TEXT,
    	"origin_path_name"	TEXT,
    	"link_path_name"	TEXT,
    	"date_added"	TIMESTAMP
        )""")
        cc.execute("""CREATE TABLE "vault" (
    	"bundle_name"	TEXT,
    	"archive_name"	TEXT,
    	"date_added"	TIMESTAMP
        )""")
        c.commit()
        c.close()
situ_test()

def print_menu():
    print(
        "Yorb 0.0.2-dev\n"
        "Welcome! What do you wish to do?\n"
        "[m] Print This Menu\n"
        "[1] Check Links In Archive\n"
        "[2] Create An Archive\n"
        "[3] Delete An Archive\n"
        "[4] DEBUG: List All Archives\n"
        "[5] Store Archive To Vault\n"
        "[6] DEBUG: Write blank entry to DB\n"
        "[q] Exit"
    )
print_menu()

def job_selection():
    job = ["m", "q", "1", "2", "3", "4", "5", "6", "exit", "quit"]
    job_key = input("Choose an option: ")
    if job_key == job[0]:
        print_menu()
    if job_key == job[1] or job_key == job[8] or job_key == job[9]:
        print("Bye.")
        exit(0)
    if job_key == job[2]:
        yorb_symlinker.archive_check_files()
        job_selection()
    if job_key == job[3]:
        yorb_symlinker.archive_create()
        job_selection()
    if job_key == job[4]:
        yorb_symlinker.archive_delete()
        job_selection()
    if job_key == job[5]:
        yorb_indexer.debug_list_archives()
        job_selection()
    if job_key == job[6]:
        print("Store Archive To Vault")
        job_selection()
    if job_key == job[7]:
        yorb_symlinker.debug_create_dummy_record()
        job_selection()
    else:
        print("Try again.")
        job_selection()
job_selection()
