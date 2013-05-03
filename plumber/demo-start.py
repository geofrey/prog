#!/usr/bin/python

from sys import *
from thread import *
from os import *
from time import *
from commands import getoutput

global active_threads

def run_command_thread(prog):
	global active_threads
	system(prog)
	active_threads -= 1

active_threads = 0

write_command = getoutput("echo " + argv[0] + " | sed s/start/in/g")
					 
for i in range(1, len(argv)):
	if argv[i] != ":":
		write_command += " \"" + argv[i] + "\""
	else:
		break

active_threads += 1
start_new_thread(run_command_thread, (write_command, ))

state = 0

sleep(1) # Really cheap hack to make it look like stuff works

for i in range(1, len(argv)):
	if argv[i] == ":":
		state = 1
		continue
	if state == 0:
		continue
	active_threads += 1
	line = getoutput("echo " + argv[0] + " | sed s/start/out/g") + " \"" + argv[i] + "\""
	start_new_thread(run_command_thread, (line, ))

while active_threads:
	sleep(1)
system("rm /tmp/plumber-test-001")
