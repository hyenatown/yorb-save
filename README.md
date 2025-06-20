# Yorb
## Project Status
Working on it. Gonna get CLI working before I implement a Qt front-end.
- CLI menu [In Progress]
- Symlinking [In Progress]
- File index [In Progress]
- Qt GUI
- Documentation

### What is this?
My idiot son who is ruining my life.

I found that having my save files scattered around the system was becoming a pain to keep track of, while also maintaining a file backup system.
My preferred backup software will search recursively through several directories unnecesarily, when I could make it skip game directories and save the parts that actually matter to me - the save and config files. This solves that problem.

### So what will it do?
First, it creates a place to store the save data ("the Archive").
Next, the user selects a directory located elsewhere ("Source Directory") which will be added to the Archive.
The user can tick boxes in a list for what files/folders within that directory they wish to have symlinked.
This is process moves the files to the Archive, and in their place, symlinks.
Ticking a directory will place a symlink at that location.

### What else can it do?
Beyond that, it should compress unused save files in a separate directory ("The Vault"), with a timestamped file name.
This is sort of like a snapshot system, with the option of creating the parent directories for the original file locations if they don't yet exist.

### What happens to my files?
Files in the Archive are nested per Source Directory selected, with a config database stored in the root of the Archive's directory.
This means you don't need to configure Yorb separately from the Archive, as your preferences will already be in place. All you need to do is open the Archive's location in Yorb.
It doesn't connect to the network or cache anything, ideally so you can store your Archive in a cloud sync folder or fuse mount.

### What if related files are stored in multiple places?
To keep it simple, just name Archives in a way that makes sense to you. This also helps compartmentalize save backups.

### What if I move the Archive?
Not yet implemented, but you could click a button and Yorb will just recreate the necessary symlinks.

### Conflicts. What about them?
If a Source Directory already exists (and is populated), the application will hold off on finalizing the action until the user tells it what to do. Retry, Cancel, Skip.

### What can't it do?
Yorb doesn't replace cloud or backup software. It's meant to consolidate user files in a way that makes file management easier. Vaulting/compression of data is meant to be a secondary feature to store unused data or create snapshots.

### Personal waffling about Yorb.
I want to pair Yorb with my home cloud instance so that I can move from one machine to another, without needing to copy files around by hand.
I'd also like so I can work without it, if I lose access to the program. Along side the database could be a human readable list of links so you can reproduce what it does by hand.
