# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023

import sqlite3
import os
from time import time
# from symlinker import origin_path

#### BEGIN Pseudocode ####
db_key = (
    f'testing_name',
    float(f'{time():.2f}'),
    float(f'{time():.2f}'),
    1000
    )
# db_conn = sqlite3.connect('repo.db')
db_conn = sqlite3.connect(':memory:')
db_c = db_conn.cursor()
db_c.execute("""
            CREATE TABLE files (
            origin_path text,
            time_added float,
            time_modified float,
            size float
            )""")
db_conn.commit()
db_conn.close()
#### END Psudocode ####