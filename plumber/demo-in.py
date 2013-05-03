#!/usr/bin/python

from sys import *
from thread import *
from os import *
from time import *

global active_threads

def reader_thread(prog):
	global active_threads
	system(prog)
	active_threads -= 1

def write_thread(x):
	while write(outfile, read(mypipe[0],1)):
		sleep(0)		
					 
active_threads = 0
mypipe = pipe()
dup2(0, 10)
dup2(1, 11)
dup2(mypipe[1], 1)

outfile = open("/tmp/plumber-test-001", O_WRONLY | O_CREAT)

for i in range(1, len(argv)):
	active_threads += 1
	start_new_thread(reader_thread, (argv[i], ))

start_new_thread(write_thread, (argv[i], ))

while active_threads:
	sleep(1)
write(outfile, "\nall_done")
