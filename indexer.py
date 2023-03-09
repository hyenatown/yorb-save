# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import json

# JSON Import/Export
def file_tracker_read(): # TODO: Import
    file_index = open('index.json', 'r')
    json.loads(file_index)
    file_index.close()
def file_tracker_delete(): # TODO: Export (overwrites)
    file_index = open('index.json', 'w')
    json.dumps(file_index)
    file_index.close()
