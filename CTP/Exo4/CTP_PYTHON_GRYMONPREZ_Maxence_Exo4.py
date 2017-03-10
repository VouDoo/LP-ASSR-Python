#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
# Title: CTP_PYTHON_GRYMONPREZ_Maxence_Exo4.py
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
# Description: CTP Exercice 4
#
# Organization: LP ASSR 4/4 - IUT Senart
# Author: Maxence GRYMONPREZ
# Email: maxgrymonprez@live.fr
# ----------------------------------------------------------------------

def main(args):
	# Open file as "reading mode"
	with open(LOG_FILE_NAME, "r") as fileStream:
		# Get file content
		fileContent = reversed(fileStream.read().splitlines())
	# Generate report file
	with open(REPORT_FILE_NAME, "w") as fileStream:
		for line in fileContent:
			curApp = line.split()[3]
			curPID = re.search('ovpn-client\[(\d+)\]', line).group(1)
			if(re.search('timeout', line)):
				fileStream.write("<Application={}; PID={}> {}\n".format(curApp, curPID, line))
		print("Report {} generated".format(REPORT_FILE_NAME))
				
if __name__ == '__main__':
	# Global variables
	LOG_FILE_NAME = "openvpn_log.txt"
	REPORT_FILE_NAME = "anomalies_VPN.txt"
	# All libs are part of standard distribution for python 3.5
	import sys
	import re
	# Execute main function
	sys.exit(main(sys.argv))
