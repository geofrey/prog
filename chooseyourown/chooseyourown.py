import sys

from chooseyourownclasses import Scene, Game
from chooseyourownutil import *

if len(sys.argv) == 2:
	storyname = sys.argv[1]
else:
	print 'What story would you like to play? Type a file name:'
	storyname = sys.stdin.readline().strip()

storyfile = open(storyname).readlines()
storyfile = filter(lambda line: len(line) > 0, map(lambda line: line.rstrip(), storyfile))
story = treead(Linerator(storyfile))
game = Game.load(story)

# set up the command loop
current = game.initial
command = 'foo'

while len(command) > 0:
	print
	print game.scenelist[current].description
	print '> ',
	command = sys.stdin.readline().strip().lower()
	if command == 'exit':
		exit()
	elif command in game.scenelist[current].paths:
		current = game.scenelist[current].paths[command].dst
	else:
		print "I didn't understand that..?"
