# This software is under a Yet-To-Be-Licensed (YTBL) meta-license.
# Contribution is encouraged, but code is not yet ready to be released.
# THIS CODE SHALL NOT BE USED FOR ANY TYPE OF GENERATIVE MODEL TRAINING.
# That said, please feel free to contribute to the main project ("yorb-save"), until a license is finalized.
# Written by Collyn Townley, (ytbl) 2023
import os
import json
import sqlite3


def situ_test():
    if os.path.exists("settings.json") is True:
        pass
    else:
        defaults = {"firstrun": True, "archive_loc": "archive", "vault_loc": "vault"}
        dir_fd = os.open(".", os.O_RDONLY)

        def opener(path, flags):
            return os.open(path, flags, dir_fd=dir_fd)

        with open("settings.json", "w", opener=opener) as f:
            print(json.dumps(defaults), file=f)
        os.close(dir_fd)
    db_exists = os.path.exists("yorb.db")
    if db_exists is True:
        pass
    else:
        c = sqlite3.connect("yorb.db")
        cc = c.cursor()
        cc.execute("""CREATE TABLE "archive" (
    	"archive_name"	TEXT,
    	"origin_path_name"	TEXT,
    	"link_path_name"	TEXT,
    	"date_added"	TIMESTAMP
        )""")
        cc.execute("""CREATE TABLE "vault" (
    	"bundle_name"	TEXT,
    	"archive_name"	TEXT,
    	"date_added"	TIMESTAMP
        )""")
        c.commit()
        c.close()
        print("Database initialized. Run me again.")
        exit(0)
