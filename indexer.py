# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet to be released.
# THIS CODE SHALL NOT BE USED FOR ANY TYPE OF GENERATIVE MODEL TRAINING.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import sqlite3
from os import path

db_exists = path.exists("vault.db")
if db_exists is False:
    c = sqlite3.connect("vault.db")
    cc = c.cursor()
    cc.execute(
        """CREATE TABLE links (
    'base_name' TEXT,
    'entry_path' TEXT,
    'date_added' TIMESTAMP
    )"""
    )
    c.commit()
    c.close()
    print("Database initialized. Run me again.")
    exit(0)


def write_to_db(vault_record):
    c = sqlite3.connect("vault.db")
    cc = c.cursor()
    cc.execute("INSERT INTO links VALUES (?,?,?)", vault_record)
    c.commit()
    c.close()


def print_current_links():
    c = sqlite3.connect("vault.db")
    cc = c.cursor()
    cc.execute("SELECT * FROM links")
    links = cc.fetchall()
    for link in links:
        print(link[0] + "\t" + format(link[2]))
