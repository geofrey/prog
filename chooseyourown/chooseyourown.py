import sys

class Scene:
	id = None
	description = ''
	options = []
	parent = None
	childs = []
	
	@staticmethod
	def load(file, game=None):
		names = file.readline().strip().split()
		if len(names) == 0:
			return None # EOF
		id = names[0]
		parent = None # make this 'world'?
		if len(names) == 2:
			parent = names[1]
		elif game:
			parent = game.world
		description = file.readline().strip()

		paths = {}
		line = file.readline().strip().split()
		while line != []:
			paths[line[0]] = line[1]
			line = file.readline().strip().split()
		return Scene(id, parent, description, paths)
	
	def serialize(self):
		data = []
		data.append('{0}\t{1}'.format(self.id, self.parent))
		data.append(self.description)
		for path in self.options:
			data.append('{0}\t{1}'.format(path, self.options[path]))
		
	def __init__(self, id, parent, description, paths):
		# scene definition consists of:
		# first line: scene ID
		# second line: description
		# additional lines: command + scene ID pairs defining where you can go from here
		self.id = id
		self.description = description
		self.options = paths
	
	def include(self, child):
		self.childs.append(child)
		child.parent = self

class Game:
	scenelist = {}
	name = ''
	author = ''
	initial = ''
	world = ''
	
	def __init__(self, name, author, start, world, scenes):
		self.name = name
		self.author = author
		self.inital = start
		self.world = world
		self.scenelist = scenes
	
	@staticmethod
	def load(filename):
		file = open(filename)
		name = file.readline().strip()
		author = file.readline().strip()
		start, world = file.readline().strip().split()
		file.readline()
		scenelist = {}
		while True:
			scene = Scene.load(file)
			if scene == None:
				break
			scenelist[scene.id] = scene
		return Game(name, author, start, world, scenelist)

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
