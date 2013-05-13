import sys

from chooseyourownclasses import Scene, Game

if len(sys.argv) == 2:
	storyname = sys.argv[1]
else:
	print 'What story would you like to play? Type a file name:'
	storyname = sys.stdin.readline().strip()
game = Game.load(storyname)

# set up the command loop
current = 'intro' # magical, always start at 'intro'
command = ''

while True:
	print
	print game.scenelist[current].description
	command = sys.stdin.readline().strip().lower()
	if command == 'exit':
		exit()
	elif command in game.scenelist[current].options:
		current = game.scenelist[current].options[command]
	else:
		print "I didn't understand that..?"
