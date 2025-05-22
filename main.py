# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import symlinker

print(
    "Yorb 0.0.1-dev\n"
    "Welcome! What do you wish to do?\n"
    "[1] Check Paths\n"
    "[2] Link a Path\n"
    "[3] Delete Path\n"
    "[4] Open Existing Archive\n"
    "[q] Exit"
)


def job_selection():
    job = ["q", "1", "2", "3", "4"]
    job_key = input("Choose an option: ")
    if job_key == job[0]:
        print("Bye.")
        exit(0)
    if job_key == job[1]:
        print("This job is Check Paths")
        exit(0)
    if job_key == job[2]:
        symlinker.add_symlink()
    if job_key == job[3]:
        symlinker.rem_symlink()
    if job_key == job[4]:
        print("This job is Open Existing Archive")
        exit(0)
    else:
        print("Try again.")
        job_selection()


job_selection()
