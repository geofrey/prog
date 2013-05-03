#!/usr/bin/python

from sys import *
from thread import *
from os import *
from time import *

global active_threads

def eater_thread(prog):
	global active_threads
	system(prog)
	active_threads -= 1

def read_thread(x):
	next_chunk = read(infile, 100)
	while next_chunk != "all_done" and next_chunk != "":
 		write(mypipe[1], next_chunk)
		next_chunk = read(infile, 100)
	close(mypipe[1])

active_threads = 0
mypipe = pipe()
dup2(0, 10)
dup2(1, 11)
dup2(mypipe[0], 0)
infile = open("/tmp/plumber-test-001", O_RDONLY)

start_new_thread(read_thread, (mypipe, ))

for i in range(1, len(argv)):
	active_threads += 1
	start_new_thread(eater_thread, (argv[i], ))

while(active_threads):
	sleep(1)
