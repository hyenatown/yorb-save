# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023

import sqlite3 as db
import os
from time import time
from symlinker import origin_path

#### Psudocode Begins Here ####
def databaseManager():
    db_key = { f'{origin_path}': {
        "time_added" : float(f'{time():.2f}'),
        "time_modified" : origin_path.time_modified,
        "size" : origin_path.size
    }}
    open('repo.db', 'w')
    