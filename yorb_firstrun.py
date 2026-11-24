import os
import json

def situ_test():
    if os.path.exists("settings.json") is True:
        pass
    else:
        defaults = {
            "archive_loc": "archive",
            "vault_loc": "vault"
            }
        dir_fd = os.open('.', os.O_RDONLY)
        def opener(path, flags):
            return os.open(path, flags, dir_fd=dir_fd)
        with open('settings.json','w', opener=opener) as f:
            print(json.dumps(defaults), file=f)
        os.close(dir_fd)