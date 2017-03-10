#!/usr/bin/env python3
# -*- coding: utf8 -*-


#####################################################
#
#   Name    : exeRemoteCmd.py
#   Author  : Grymonprez Maxence
#   Version : 1.2
#   Date    : 24/09/2016
#
#####################################################


"""

    Information
    ~~~~~~~~~~~

    A pure python script !
    This script allows to execute quickly and remotely some commands from a file via ssh protocol.


    Importante Notice
    ~~~~~~~~~~~~~~~~~

    before, make sure you have the module named "paramiko".
    This module is used to establish a client SSH connection.
    Get it with "pip". Use this following command:
        'pip install paramiko'

    ... AND, PLEASE, USE PYTHON 3 !


    How to use
    ~~~~~~~~~~

    Refer commands in file labeled "commands.cfg" located in script's directory in "/config".

    Exemple of content for "commands.cfg":

        lscpu | grep Arch*
        lspci
        lsusb


    Usual use for the script:

        'python /path/to/exeRemoteCmd.py [-h] [-i PORT] [-u USER] [-p PASSWORD] ip'.

        Arguments list :
            ip          : Target's IP address
            port        : Target's port number
            user        : SSH user
            password    : SSH password


    For more help, type this :

        'python /path/to/exeRemoteCmd.py -h'
        or
        'python /path/to/exeRemoteCmd.py --help'


    Released
    ~~~~~~~~

    September 24, 2016
    ------------------
    Version 1.1.0 :
        * Add function "requiremodules"
            -> Check if exist "paramiko" module
        * Fix path to "commands.cfg" (any OS)

    September 22, 2016
    ------------------
    Version 1.0.1 :
        * Minor modifications
        * Add optionnal arguments (argparse module)
            -> "-user" and "-password" for SSH connection

    September 21, 2016
    ------------------
    Version 1.0. :
        * First release

"""


# Module imports

import pip
import sys

# Check require modules to execute correctly the script
# Function "requiremodules"


def requiremodules(*packages):
    """
    description :
        Check if packages are installed.
        If not, install them.
    inputs :
        - packages : packages to import
    """
    for package in packages:
        try:
            if not isinstance(package, str):
                import_name, install_name = package
            else:
                import_name = install_name = package
            __import__(import_name)
        except ImportError:

            cmd = ['install', install_name]
            if not hasattr(sys, 'real_prefix'):
                cmd.append('--user')
            pip.main(cmd)


# Python Standard libraries
import os
import argparse
import ipaddress
import socket
from getpass import getpass  # Secret password getter
# Other libraries
# Paramiko module
try:
    requiremodules('paramiko')
except Exception:
    print('Error to install "paramiko"')
    sys.exit(1)  # Exit program with error
from paramiko import *

#[End] Module imports


# Functions Definition

# Function "getcontentfromfile"
def getcontentfromfile(file):
    """
    description :
        Import file content to a list.
    inputs :
        - file : file's path
    outputs :
        - lines : list with file content for each line
    """
    # Open file
    try:
        f = open(file, "r")
        commands = f.read().splitlines()
        f.close()
    except FileNotFoundError as e:
        raise FileNotFoundError(
            file + " not found... Please, verify its location or create it")
    except Exception:
        raise
    # Append list for return
    lines = list()
    for line in commands:
        lines.append(line)
    return lines

#[End] Functions Definition


# Main program

# Title
print("""\
    \n\n
    #************************************#
    #****** Script exeRemoteCmd.py ******#
    #************************************#
    """)

# Arguments parser
# Create object
parser = argparse.ArgumentParser()
# Positional arguments
parser.add_argument("ip", type=str, help="Target's IP Address")
# Optional arguments
parser.add_argument("-i", "--port", type=int, default="22",
                    help="Target's port number (default : port 22)")
parser.add_argument("-u", "--user", type=str, help="SSH user")
parser.add_argument("-p", "--password", type=str, help="SSH password")
# Collect values
args = parser.parse_args()


# List of commands to execute remotely (import from file "commands.cfg")
# Move to script's directory

# Try to open file "commands.cfg"
cmdsFile = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)),
    'config',
    'commands.cfg')
print(cmdsFile)
try:
    cmdsToExe = getcontentfromfile(cmdsFile)
except Exception as e:
    print(e)
    sys.exit(1)  # Exit program with error

# Initialization variable from arguments
ipTarget = args.ip
portTarget = int(args.port)
sshUser = args.user
sshPwd = args.password

# Check IP address format
try:
    ipaddress.ip_address(ipTarget)
except ValueError as e:
    print("Invalid IP format:", e)
    sys.exit(1)  # Exit program with error

# Check connectivity statut by the port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print("> Test connection :")
    sock.connect((ipTarget, portTarget))
    print(ipTarget, "is reachable via the port", portTarget)
except socket.error as e:
    print("Error during connection to", ipTarget, "via the port", portTarget)
    sys.exit(1)  # Exit program with error
finally:
    sock.close()

# Open SSH connection
print("\n> SSH authentication")

# Check user and password arguments
print("\tUsername: ", end='')
if not sshUser:
    sshUser = str(input())
else:
    print(sshUser)
if not sshPwd:
    sshPwd = getpass("\tPassword: ")
else:
    print("\t(Password already entered)")

# Establish SSH client
client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.load_system_host_keys()
try:
    client.connect(
        ipTarget,
        port=portTarget,
        username=sshUser,
        password=sshPwd)
except AuthenticationException as e:
    print("\nConnection error : Authentication failed...")
    sys.exit(1)  # Exit program with error

# File "commands.cfg" is empty
if not cmdsToExe:
    print("\nNo commands find... please refer 'commands.cfg'")
# Commands execution
else:
    print("\n****** SSH connection established ! ******")
    i = 0
    for cmd in cmdsToExe:
        i += 1
        try:
            # Remotely execution
            stdin, stdout, stderr = client.exec_command(cmd)
            # Command line (stdin)
            print("\nCommand[", i, "]> ", cmd, sep='')
            # Output (stdout)
            print("\n*** Output ***")
            stdoutResult = stdout.readlines()
            if not stdoutResult:
                print("No output")
            else:
                for line in stdoutResult:
                    line = line.encode(sys.stdout.encoding, errors='replace')
                    print(line.decode('cp850'))
            # Errors (stderr)
            print("\n*** Errors ***")
            stderrResult = stderr.readlines()
            if not stderrResult:
                print("No error")
            else:
                for line in stderrResult:
                    line = line.encode(sys.stdout.encoding, errors='replace')
                    print(line.decode('cp850'))
        except Exception as e:
            print(e)

# Close SSH connection
client.close()

sys.exit(0)  # Exit program without error

#[End] Main program
