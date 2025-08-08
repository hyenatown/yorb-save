# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# THIS CODE SHALL NOT BE USED FOR ANY TYPE OF GENERATIVE MODEL TRAINING.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import yorb_symlinker
import yorb_indexer


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
    job = ["m", "q", "1", "2", "3", "4", "5", "6"]
    job_key = input("Choose an option: ")
    if job_key == job[0]:
        print_menu()
    if job_key == job[1]:
        print("Bye.")
        exit(0)
    if job_key == job[2]:
        print("This job is Check Links in Archive")
        job_selection()
    if job_key == job[3]:
        yorb_symlinker.create_archive()
        job_selection()
    if job_key == job[4]:
        yorb_symlinker.delete_archive()
        job_selection()
    if job_key == job[5]:
        yorb_indexer.debug_list_archives()
        job_selection()
    if job_key == job[6]:
        print("Store Archive To Vault")
        job_selection()
    if job_key == job[7]:
        yorb_symlinker.debug_create_dummy_archive_record()
        job_selection()
    else:
        print("Try again.")
        job_selection()


job_selection()
