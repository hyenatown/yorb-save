# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# THIS CODE SHALL NOT BE USED FOR ANY TYPE OF GENERATIVE MODEL TRAINING.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023

import sqlite3
from os import path

c = sqlite3.connect("vault.db")
cc = c.cursor()
base_name = 0
entry_path = "null"
date_added = 0
date_updated = 0
vault_record = (base_name, entry_path, date_added, date_updated)


def db_init():
    db_exists = path.exists("vault.db")
    if db_exists is True:
        cc.execute(
            """CREATE TABLE links (
        'base_name' TEXT,
        'entry_path' TEXT,
        'date_added' INTEGER,
        'date_updated' INTEGER
        )"""
        )
        c.commit()
        c.close()
        print("Database initialized.")
        exit(0)
    else:
        print("The database was either deleted or closed before executing. Exiting.")
        exit(0)


def write_to_db():
    cc.execute("INSERT INTO links VALUES (?,?,?,?)", vault_record)
    c.commit()
    c.close()
