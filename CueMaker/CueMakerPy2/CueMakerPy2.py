#!/usr/bin/env python

# Import libs
import os
import sys
from os import walk
from os.path import exists
import re

patterns1 = ['Track 1']
patterns2 = ['Track 2']
# Define path to search
# mypath is a literal string so you dont have to escape path
mypath = r"./roms";
recursive = True

# Get input
trues = ("Y", "Yes", "True", "T", True)
rawt = ("Y", "Yes", "True", "R", True)
rawf = ("N", "No", "False", "T", False)
if (sys.version_info > (3, 0)):
    #py3 code
    mypath = input("Please enter path to scan ["+mypath+"]:") or mypath
    trecursive = input("Search Recursive? ["+str(recursive)+"]:").strip().title() or recursive
    traw = input("Raw or Truncated? [R/T]:")
    filenamex = input("Please enter Project Name [filename]:")
    recursive = trecursive in trues
else:
    #py2 code
    mypath = raw_input("Please enter path to scan ["+mypath+"]:") or mypath
    trecursive = raw_input("Search Recursive? ["+str(recursive)+"]:").strip().title() or recursive
    traw = raw_input("Raw or Truncated? [R/T]:")
    filenamex = raw_input("Please enter Project Name [filename]:")
    recursive = trecursive in trues


if (traw == rawt):
    # Define cue file
    cue1 = r"""FILE "%TRACK1%" BINARY
  TRACK 01 MODE1/2352
    INDEX 01 00:00:00"""
else:
    # Define cue file
    cue1 = r"""FILE "%TRACK1%" BINARY
  TRACK 01 MODE1/2336
    INDEX 01 00:00:00"""
    
cue2 = r"""
FILE "%TRACK2%" BINARY
  TRACK 02 AUDIO
    INDEX 00 00:00:00
    INDEX 01 00:02:00"""

# For each (sub)folder
for (dirpath, dirnames, filenames) in walk(mypath):
    # For each file
    for file in filenames:
        # Get extension
        filename, file_extension = os.path.splitext(file)

        # If its a bin
        if (exists((file_extension.lower()==".bin" or file_extension.lower()==".iso" or file_extension.lower()==".img"))):
            # Search for a cue
            if (filenamex + ".cue").lower() not in (name.lower() for name in filenames):
                # None found, create one
                savePath = os.path.join(dirpath,filenamex+ ".cue")
                fileHandle = open(savePath, "a")
                for i in patterns1:
                    if re.search (i, file):
                        fileHandle.write(cue1.replace("%TRACK1%", file))
                    else:
                        print("no match!")
                        
                for k in patterns2:
                    if re.search (k, file):
                        fileHandle.write(cue2.replace("%TRACK2%", file))
                    else:
                        print("no match!")
                        
            fileHandle.close()
                # Output write
            print("Cue created: " + savePath)
                
    # If they dont want to go recursive, get out
    if not recursive:
        break
