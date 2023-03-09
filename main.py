# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023

# This is the main bit that asks what you wanna do.
print(
    'Yorb 0.0.1-dev\n'
    'Welcome! What do you wish to do?\n'
    '[1] Check Links\n'
    '[2] Delete Links\n'
    '[3] Create New Archive\n'
    '[4] Open Existing Archive\n'
    '[q] Exit'
)
job_selection()
def job_selection():
    job = ['q','1','2','3','4']
    job_key = input("Choose an option: ")
    if job_key == job[0]:
        exit("Bye.")
    else:
        print("Try again.")
        job_selection()
exit()