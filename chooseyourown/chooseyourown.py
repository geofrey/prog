import sys

from chooseyourownclasses import Scene, Game
from chooseyourownutil import *
from chooseyourownbuiltins import builtins

if len(sys.argv) == 2:
	storyname = sys.argv[1]
else:
	print 'What story would you like to play? Type a file name:'
	storyname = sys.stdin.readline().strip()

story = applysequence(storyname, [
	lambda name: open(name).readlines(),
	sanitizefile,
	Linerator,
	treead
])

game = Game.load(story)
#print(game)

# set up the command loop
current = game.initial
command = 'foo'

while len(command) > 0:
	print
	print game.scenelist[current].description
	print '> ',
	command = sys.stdin.readline().strip().lower()
	if command in builtins.keys():
		builtins[command]()
	elif command in game.scenelist[current].paths:
		current = game.scenelist[current].paths[command].dst
	else:
		print "I didn't understand that..?"
