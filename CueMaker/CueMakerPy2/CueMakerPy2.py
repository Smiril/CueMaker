#!/usr/bin/env python

# Import libs
import os
import sys
from os import walk
from os.path import exists
import re

patterns1 = ['Track 1']
patterns2 = ['Track 2']
patterns3 = ['Track 3']
patterns4 = ['Track 4']
patterns5 = ['Track 5']
patterns6 = ['Track 6']
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

cue3 = r"""
FILE "%TRACK3%" BINARY
  TRACK 03 AUDIO
    INDEX 00 00:00:00
    INDEX 01 00:02:00"""

cue4 = r"""
FILE "%TRACK4%" BINARY
  TRACK 04 AUDIO
    INDEX 00 00:00:00
    INDEX 01 00:02:00"""

cue5 = r"""
FILE "%TRACK5%" BINARY
  TRACK 05 AUDIO
    INDEX 00 00:00:00
    INDEX 01 00:02:00"""

cue6 = r"""
FILE "%TRACK6%" BINARY
  TRACK 06 AUDIO
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
                for k1 in patterns1:
                    if re.search (k1, file):
                        fileHandle.write(cue1.replace("%TRACK1%", file))
                    else:
                        continue
                
                for k2 in patterns2:
                    if re.search (k2, file):
                        fileHandle.write(cue2.replace("%TRACK2%", file))
                    else:
                        continue
                        
                for k3 in patterns3:
                    if re.search (k3, file):
                        fileHandle.write(cue3.replace("%TRACK3%", file))
                    else:
                        continue
                                        
                for k4 in patterns4:
                    if re.search (k4, file):
                        fileHandle.write(cue4.replace("%TRACK4%", file))
                    else:
                        continue
                        
                for k5 in patterns5:
                    if re.search (k5, file):
                        fileHandle.write(cue5.replace("%TRACK5%", file))
                    else:
                        continue
                                                        
                for k6 in patterns6:
                    if re.search (k6, file):
                        fileHandle.write(cue6.replace("%TRACK6%", file))
                    else:
                        continue


    fileHandle.close()
                # Output write
    print("Cue created: " + savePath)
                
    # If they dont want to go recursive, get out
    if not recursive:
        break
