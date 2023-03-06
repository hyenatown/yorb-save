# Yorb

## Abstract
Recently I found that having my save files scattered around the system, either if because they're in a Steam install folder, the configuration or local data directories, or simply somewhere less conventional like /etc - that this was becoming a bit of a pain to keep track of while also maintaining a file backup system that needs to seek out these locations as well.

When my preferred backup software runs, it will search recursively through several directories unnecesarily, when I could simply instruct it to skip game directories and simply save the parts that actually matter to me - the save and config files. On top of that, however, I found the process of selecting files and creating symlinks to be tiring. This is the part of the process I would like to automate with this tool.

## So what will it do?
I like to imagine the scope is more for keeping track of files that change often such as save data.
First the creation of a place to store the save data ("the Archive"). Next, the user adds a directory located elsewhere ("Remote Folder") to the Archive. The user can tick off boxes in a list for what files/folders within that directory they wish to have symlinked. This is process will move the files to the Archive, and in their place, symlinks. Ticking a directory will place a symlink at that location (alternatively, the top-most dir that has been ticked, ignoring any ticked files/folders within it, as it will move all files within).
By doing this, all relevant files to the user can stay in one place.

## What else can it do?
Beyond the basic use, I'd like to have it compress unused save files in a separate directory ("The Vault"), timestamped in the file name. This quick backup solution can allow the user to restore saves in the Archive with one from the Vault, with the option of creating the parent directories for the original file locations if they don't yet exist. This trivializes restoring data after restoring or reinstalling an operating system.

## What happens to my files?
Files in the Archive are nested per Remote Folder selected, with some config data stored in the root of the Archive directory. This means you don't need to configure Yorb separately from the Archive as your preferences will already be in place. All you need to do is open the Archive's location in Yorb. Another note is that it does not connect to the network, so ideally you can store your Archive in a cloud sync folder or fuse mount.

## What if files are stored in multiple places?
To keep it simple, I'd just name Archive directories in a way that makes sense to you. This also helps compartmentalize save backups.

## Further waffling about Yorb.
Primarily, I'd like to pair Yorb with my Nextcloud instance so that I can move from one machine to another without needing to copy files around by hand. I'd also like to have it so I can work without it if I happen to lose access to the program. Ideally, config files will be human readable so you can reproduce what it does by hand.
