#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
# Title: regex.py
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
# Description: TP09 Exercice 2 - TP portant sur l'utilisation basique des expressions régulières
#
# Organization: LP ASSR 4/4 - IUT Senart
# Author(s): Maxence GRYMONPREZ, Alexandre GVOZDENOVIC
# Email(s): maxgrymonprez@live.fr, alexandre.gvozdenovic@gmail.com
# ----------------------------------------------------------------------

def getfilepathtk():
    """
        Get file path with tkinter.
        
        This gets file path by using filedialog from tkinter and return
        this one to string type.
        
        :return: file path
        :rtype: string
        
        :Example:
        
        >>> print(getfilepathtk())
        /path/to/file
        
        ::seealso:: tkinter
        ::warning:: This function requires graphical environement.
        ::note:: Before using it, import tkinter module ("Tk" and "filedialog" parts).
    """
    root = Tk().withdraw()
    inputFilePath = filedialog.askopenfilename()
    if not inputFilePath:
        raise ValueError("File not selected")
    else:
        return inputFilePath

def framestring(stringToFrame):
    """
        Return framed string.
        
        Frame a string with "*" and return it.

        :stringToFrame: string to frame
        :ptype: string

        :return: framed string
        :rtype: string
        
        :Example:
        
        >>> print(frameString("Hello World !"))
        *************
        Hello World !
        *************
        
        ::seealso:: len(), format()
    """
    return "{charFrame:*^{stringLen}}\n{framedString}\n{charFrame:*^{stringLen}}".format(charFrame="*", stringLen=len(stringToFrame), framedString=stringToFrame)

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
    # Initialize global variables
    # Report file name : YYYYmmddHHMM_sortie.txt (which "YYYYmmddHHMM" is datetime)
    reportFileName = "{}_sortie.txt".format(datetime.now().strftime("%Y%m%d%H%M"))
    # Regular expressions ordered dict definition
    # (key = title, value = regular expression)
    regexpDict = collections.OrderedDict([
            ("1.a : lignes contenant des chiffres ou des majuscules", '[0-9]|[A-Z]'),
            ("1.b : lignes contenant des points", '\.'),
            ("1.c : lignes contenant trois points", '\.{3}'),
            ("1.d : lignes contenant des nombres hexadecimaux separes par des blancs", '\s[a-fA-F0-9]+\s|^[a-fA-F0-9]+\s'),
            ("1.e : lignes contenant un mot d'au moins 12 caracteres alphanumeriques", '[a-zA-Z0-9]{12,}'),
            ("1.f : lignes contenant exactement 5 lettres a (pas nécessairement successives)", '^([^a]*a[^a]*){5}$'),
            ("1.g : lignes contenant des crochets ( ] ou [ )", '\[|\]'),
            ("1.h : lignes ne contenant que des lettres a et des espaces", '^[a ]+$'),
            ("1.i : lignes contenant quelque chose qui ressemble a une adresse IP", '(\d+\.){3}'),
            ("2.a : lignes vides", '^$'),
            ("2.b : lignes blanches", '^\s+$'),
            ("2.c : lignes non vides", '.+'),
            ("3.a : lignes qui ne contiennent pas de a", '^[^a]*$'),
            ("3.b : lignes qui ne contiennent pas des espaces", '^[^ ]*$'),
            ("3.c : lignes qui ne contiennent pas des chiffres décimaux", '^[^0-9]*$'),
            ("4 : lignes qui débutent par un numéro de téléphone au format 01 23 45 67 89", '^([0-9]{2} ){4}[0-9]{2}'),
            ("5 : idem 4 mais on peut avoir . ou - a la place des espaces", '^([0-9]{2}[ -.]){4}[0-9]{2}'),
            ("6 : idem 5 mais le 0 peut être entoure de parentheses", '^(0|(\(0\)))[0-9][ .-]([0-9]{2}[ .-]){3}[0-9]{1}'),
            ("7 : terminent par un tel au format 0 123 456 789, espaces, - ou . et (0)", '(0|(\(0\))) ([0-9]{3}[ .-]){2}[0-9]{3}$')
        ])
    # Start process
    try:
        #  Select a file and get its content
        with open(getfilepathtk(), "r") as fileStream:
            fileContent = fileStream.read().splitlines()
        #  Create and fill report file
        with open(reportFileName, "w") as fileStream:
            fileStream.write(framestring("Python : Fichier de sortie de l'exercice 2 du TP9"))
            for title, regexp in regexpDict.items():
                fileStream.write("\n\n" + framestring(title))
                matchedLines = getmatchedlines(regexp, fileContent)
                for line in matchedLines:
                    fileStream.write("\n" + line)
                fileStream.write("\n" + "***** {} lignes trouvées *****".format(len(matchedLines)))
        print("<Info> Report generated : {}".format(reportFileName))
    except Exception as err:
        print("<Error> {}".format(err))
        sys.exit()

if __name__ == '__main__':
    # All libs are part of standard distribution for python 3
    import sys
    import re
    import collections
    from tkinter import Tk, filedialog
    from datetime import datetime
    # Execute main function
    sys.exit(main(sys.argv))
