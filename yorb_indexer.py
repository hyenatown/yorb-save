# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet ready to be released.
# THIS CODE SHALL NOT BE USED FOR ANY TYPE OF GENERATIVE MODEL TRAINING.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import sqlite3
from os import path

def archive_record_add(archive_db_record):
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute("INSERT INTO archive VALUES (?,?,?,?)", archive_db_record)
    c.commit()
    c.close()

def archive_record_delete(archive_db_record):
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute("DELETE FROM archive WHERE _rowid_ = ?", (archive_db_record))
    c.commit()
    c.close()

def archive_fetch_all():
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute("SELECT _rowid_, * FROM archive")
    links = cc.fetchall()
    for link in links:
        print(
            format(link[0])
            + "\t"
            + format(link[1])
            + "\t"
            + format(link[2])
            + "\t"
            + format(link[4])
        )
    if links == []:
        print("You have no archives!")
        c.close()
        return False
    else:
        c.close()
        return True, links

def archive_fetch_all_noprint():
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute("SELECT _rowid_, * FROM archive")
    links = cc.fetchall()
    if links == []:
        print("You have no archives!")
        c.close()
        return False
    else:
        c.close()
        return True, links

def archive_fetch_selected(archive_db_record):
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute("SELECT * FROM archive WHERE _rowid_ = ?", (archive_db_record))
    archive_db_record_entry = cc.fetchone()
    c.close()
    return archive_db_record_entry

def debug_list_archives():
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute("SELECT * FROM archive")
    links = cc.fetchall()
    for link in links:
        print(format(link[0]) + "\t" + format(link[1]) + "\t" + format(link[3]))
    c.close()