#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
# Title: CTP_PYTHON_GRYMONPREZ_Maxence_Exo3.py
#
# Copyright 2017
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
# ----------------------------------------------------------------------
# Description: CTP Exercice 3
#
# Organization: LP ASSR 4/4 - IUT Senart
# Author: Maxence GRYMONPREZ
# Email: maxgrymonprez@live.fr
# ----------------------------------------------------------------------

def getmatchedlines(regexp, lines):
    """
        Get matched lines by using regex.
        
        Return all lines that match with a given regular expression.

        :regexp: regular expression
        :ptype: string
        :lines: lines to compare with regular expression
        :ptype: string

        :return: matched lines
        :rtype: list
        
        ::seealso:: re
        ::note:: Before using it, import re module.
    """
    matchedLines = list()
    for line in lines:
        if re.search(regexp, line):
            matchedLines.append(line)
    return matchedLines

def main(args):
	# Report files dict
	# keys = report file name
	# values = regular expresssion
	reportsDict = collections.OrderedDict([
			("install.txt", '\\binstall\\b'),
            ("start.txt", '\\bstart\\b'),
            ("restart.txt", '\\brestart\\b'),
            ("poweroff.txt", 'poweroff'),
            ("stop.txt", '\\bstart\\b')
	])
	# Open file as "reading mode"
	with open(LOG_FILE_NAME, "r") as fileStream:
		# Get file content
		fileContent = fileStream.read().splitlines()
	# Generate report files
	for reportFileName, regexp in reportsDict.items():
		matchedLines = getmatchedlines(regexp, fileContent)
		try:
			with open(reportFileName, "w") as fileStream:
				for line in matchedLines:
					fileStream.write(line + "\n")
				print("Report {} generated ({} lines written)".format(reportFileName, len(matchedLines)))
		except Exception as err:
			print("<Error> {}".format(err))
			sys.exit()
		
if __name__ == '__main__':
	# Global variables
	LOG_FILE_NAME = "log_sudo.txt"
	# All libs are part of standard distribution for python 3.5
	import re
	import sys
	import collections
	# Execute main function
	sys.exit(main(sys.argv))
