# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet ready to be released.
# THIS CODE SHALL NOT BE USED FOR ANY TYPE OF GENERATIVE MODEL TRAINING.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import sqlite3
from os import path


db_exists = path.exists("yorb.db")
if db_exists is False:
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute(
        """CREATE TABLE "archive" (
	"archive_name"	TEXT,
	"origin_path_name"	TEXT,
	"link_path_name"	TEXT,
	"date_added"	TIMESTAMP
    )"""
    )
    cc.execute(
        """CREATE TABLE "vault" (
	"bundle_name"	TEXT,
	"archive_name"	TEXT,
	"date_added"	TIMESTAMP
    )"""
    )
    c.commit()
    c.close()
    print("Database initialized. Run me again.")
    exit(0)


def add_archive_record(archive_db_record):
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute("INSERT INTO archive VALUES (?,?,?,?)", archive_db_record)
    c.commit()
    c.close()


def debug_list_archives():
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute("SELECT * FROM archive")
    links = cc.fetchall()
    for link in links:
        print(format(link[0]) + "\t" + format(link[1]) + "\t" + format(link[3]))
    c.close()


def fetch_all_archives():
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
        print("The database is empty!")
        c.close()
        return False
    else:
        c.close()
        return True


def fetch_selected_archive_record(archive_db_record):
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute("SELECT * FROM archive WHERE _rowid_ = ?", (archive_db_record))
    archive_db_record_entry = cc.fetchone()
    c.close()
    return archive_db_record_entry


def delete_archive_record(archive_db_record):
    c = sqlite3.connect("yorb.db")
    cc = c.cursor()
    cc.execute("DELETE FROM archive WHERE _rowid_ = ?", (archive_db_record))
    c.commit()
    c.close()
