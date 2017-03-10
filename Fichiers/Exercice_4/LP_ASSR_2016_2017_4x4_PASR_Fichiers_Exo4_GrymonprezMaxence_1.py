# -*- coding: UTF-8 -*-

#! /usr/bin/env python3.5

# ---------------------------------------------------------------------
# Title: Fichiers _ Exercice 4
# This Python script generates report with lines from each files
# in a selected directory (inlcude sub-directories) starting with
# a specific string given by user.
#
# Author: Grymonprez Maxence
# Email: maxgrymonprez@live.fr
# ---------------------------------------------------------------------
# All libs are part of standard distribution for python 3.5

import os, sys
from datetime import datetime
from tkinter import Tk, filedialog, messagebox

def main():
	root = Tk().withdraw()

	# Inputs
	inputDir = filedialog.askdirectory()
	if not inputDir:
		sys.exit() # Exit
	stringStart = str(input("Report lines beginning with : "))

	# Typical report file name : YYYYmmddHHMM_report ("YYYYmmddHHMM" is datetime)
	ReportFileName = "{0}_report".format(datetime.now().strftime("%Y%m%d%H%M"))
	# Open report file stream
	with open(ReportFileName, 'w') as reportFileStream:
		reportFileStream.write("Datetime: {0}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M")))
		reportFileStream.write("Root Directory: {0}\n".format(inputDir))
		reportFileStream.write("Lines start with: {0}\n\n".format(stringStart))
		# Recursive files scan in directory
		for root, subdirs, files in os.walk(inputDir):
			for file in files:
				# Get absolute file path
				fileAbsPath = os.path.abspath(os.path.join(root, file))
				reportFileStream.write("<FilePath> {0}\n".format(fileAbsPath))
				# Parse file content and fill in report 
				try:
					# Read file
					with open(fileAbsPath, "r") as fileStream:
						fileContent = fileStream.read().splitlines()
					lineCount = int(0)
					linesFoundCount = int(0)
					for line in fileContent:
						lineStriped = line.strip() # Remove whitespaces on the both sides
						lineCount += 1
						# If line starts with var "stringStart"
						if lineStriped.lower().startswith(stringStart.lower()):
							linesFoundCount += 1
							reportFileStream.write("<Line {0}> {1}\n".format(lineCount, lineStriped))
					if not linesFoundCount:
							reportFileStream.write("<No result>\n")
				# Catch exception and write it in report
				except Exception as err:
					reportFileStream.write("<Error> {0}\n".format(err))
				reportFileStream.write("\n")
	messagebox.showinfo("Info" , "Report file has been generated\n{0}".format(os.path.abspath(ReportFileName)))

if __name__ == "__main__":
	main()
