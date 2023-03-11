# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import json
import symlinker
import indexer
# This is the main bit that asks what you wanna do.
print(
    'Yorb 0.0.1-dev\n'
    'Welcome! What do you wish to do?\n'
    '[1] Check Paths\n'
    '[2] Delete Path\n'
    '[3] Link a Path\n'
    '[4] Open Existing Archive\n'
    '[q] Exit'
)
# TODO: This is turning into an if-tree mess so I'll redo it later. It technically works.
def job_selection():
    job = ['q','1','2','3','4']
    job_key = input("Choose an option: ")
    if job_key == job[0]:
        exit("Bye.")
    if job_key == job[1]:
        print("This job is Check Paths")
        exit()
    if job_key == job[2]:
        print("This job is Delete Path")
        exit()
    if job_key == job[3]:
        print("This job is Link a Path")
        exit()
    if job_key == job[4]:
        print("This job is Open Existing Archive")
        exit()
    else:
        print("Try again.")
        job_selection()
job_selection()