#!/usr/bin/python2.7

import subprocess

print("*** Test 1 subprocess ***")

adr = '127.0.0.1'
test1_proc = subprocess.Popen(['ping', '-c', '3', adr], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
test1_out, test1_err = test1_proc.communicate()
print("--- Output ---")
print(test1_out)
print("--- Error ---")
print(test1_err)

print("*** Test 2 subprocess ***")

test2_proc1 = subprocess.Popen(['ls', '-l', '/'], stdout=subprocess.PIPE)
test2_proc2 = subprocess.Popen('wc', stdin=test2_proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
test2_out, test2_err = test2_proc2.communicate()
print("--- Output ---")
print(test2_out)
print("--- Error ---")
print(test2_err)
