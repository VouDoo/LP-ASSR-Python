# -*- coding: UTF-8 -*-

#! /usr/bin/env python3.5

# ---------------------------------------------------------------------
# Title: Fichiers _ Exercice 2
# A program to manage files
#
# Author: Grymonprez Maxence
# Email: maxgrymonprez@live.fr
# ---------------------------------------------------------------------
# All libs are part of standard distribution for python 3.5

import sys, os
import tkinter as tk
from tkinter import filedialog

def returnlinefromfile():
    root = tk.Tk().withdraw()
    inputFileName = filedialog.askopenfilename()
    if not inputFileName:
        return str("<Error> File is not selected")
    elif not os.path.isfile(inputFileName):
        return str("<Error> {0} is not a file or does not exist".format(inputFileName))
    else:
        fileAbsPath = os.path.abspath(inputFileName)
        lineIndex = int(input("Please, enter line index : "))
        while lineIndex <= 0:
            print("<Error> Index cannot be null or negative")
            lineIndex = int(input("Please, re-enter line index : "))
        try:
            with open(fileAbsPath, "r") as fileStream:
                fileContent = fileStream.read().splitlines()
                if lineIndex <= len(fileContent):
                    return str("<Return> {0}".format(fileContent[lineIndex - 1].strip()))
                else:
                    return str("<Error> Index exceeds the number of lines in file")
        except Exception as err:
            return str("<Error> {0}".format(err))

def exitApp():
    sys.exit()

def main():
    menu = {
        '1': {
            'action': 'Execute application',
            'exec': returnlinefromfile
        },
        '2': {
            'action': 'Exit application',
            'exec': exitApp
        }
    }
    while True:
        for key, value in menu.items():
            print(key, value['action'])
        select = str(input(">> "))
        try:
            print(menu[select]['exec']())
        except KeyError:
            print("<Error> Invalid selection, please try again")
        input("Press Enter to back to menu ...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
if __name__ == "__main__":
    main()
