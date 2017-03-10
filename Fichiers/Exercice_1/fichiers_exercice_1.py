# -*- coding: UTF-8 -*-

#! /usr/bin/env python3.5

# ---------------------------------------------------------------------
# Title: Fichiers _ Exercice 1
# A program to manage files
#
# Author: Grymonprez Maxence
# Email: maxgrymonprez@live.fr
# ---------------------------------------------------------------------
# All libs are part of standard distribution for python 3.5

import os
import tkinter as tk
from tkinter import filedialog

def copywithlinenumber(filePath):
    
    # Collect file content
    with open(filePath, "r") as fileStream:
        fileContent = fileStream.readlines()

    # Create and fill the new file
    filePathSplitted = os.path.split(filePath)
    newFilePath = os.path.join(filePathSplitted[0], "copy_" + filePathSplitted[1])
    with open(newFilePath, "w") as fileStream:
        lineCount = int(0)
        for line in fileContent:
            lineCount += 1
            fileStream.write(str(lineCount) + "\t" + line)

def main():
    root = tk.Tk().withdraw()
    inputFileName = filedialog.askopenfilename()
    if not inputFileName:
        print("file not selected")
    elif os.path.isfile(inputFileName):
        fileAbsPath = os.path.abspath(inputFileName)
        copywithlinenumber(fileAbsPath)
    else:
        print(inputFileName, " is not a file or does not exist")

if __name__ == "__main__":
    main()
