# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# THIS CODE SHALL NOT BE USED FOR ANY TYPE OF GENERATIVE MODEL TRAINING.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import yorb_symlinker
import yorb_indexer

print(
    "Yorb 0.0.1-dev\n"
    "Welcome! What do you wish to do?\n"
    "[1] Check Paths\n"
    "[2] Link a Path\n"
    "[3] Delete Path\n"
    "[4] List Links\n"
    "[5] DEBUG: Write blank entry to DB\n"
    "[q] Exit"
)


def job_selection():
    job = ["q", "1", "2", "3", "4", "5"]
    job_key = input("Choose an option: ")
    if job_key == job[0]:
        print("Bye.")
        exit(0)
    if job_key == job[1]:
        print("This job is Check Paths")
        job_selection()
    if job_key == job[2]:
        yorb_symlinker.add_symlink()
        job_selection()
    if job_key == job[3]:
        yorb_symlinker.rem_symlink()
        job_selection()
    if job_key == job[4]:
        yorb_indexer.print_current_links()
        job_selection()
    if job_key == job[5]:
        dest_file_basename = "null"
        dest_file = "null"
        current_date_time = 0
        vault_record = (dest_file_basename, dest_file, current_date_time)
        yorb_indexer.write_to_db(vault_record)
        job_selection()
    else:
        print("Try again.")
        job_selection()


job_selection()
