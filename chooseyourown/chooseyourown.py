import sys

global scenelist
scenelist = {}

class Scene:
	id = None
	description = ''
	options = []
	parent = None
	childs = []
	
	@staticmethod
	def parse(data):
		id = data[0]
		description = data[1]
		paths = dict([(o[0], o[1]) for o in [word.split('\t') for word in data[2:]]])
		return Scene(id, description, paths)
	
	def __init__(self, id, description, paths):
		# scene definition consists of:
		# first line: scene ID
		# second line: description
		# additional lines: command + scene ID pairs defining where you can go from here
		self.id = id
		self.description = description
		self.options = paths
		
		scenelist[id] = self
	
	def include(self, child):
		self.childs.append(child)
		child.parent = self


# load our story:
def get_scene(file):
	textchunk = []
	line = file.readline().strip()
	while len(line) > 0:
		textchunk.append(line)
		line = file.readline().strip()
	if len(textchunk) == 0:
		return None
	else:
		return Scene.parse(textchunk)

if len(sys.argv) == 2:
	storyname = sys.argv[1]
else:
	print 'What story would you like to play? Type a file name:'
	storyname = sys.stdin.readline().strip()
story = open(storyname)

scene = get_scene(story)
while scene is not None:
	scene = get_scene(story)



# set up the command loop
current = 'intro' # magical, always start at 'intro'
command = ''

while True:
	print
	print scenelist[current].description
	command = sys.stdin.readline().strip().lower()
	if command == 'exit':
		exit()
	elif command in scenelist[current].options:
		current = scenelist[current].options[command]
	else:
		print "I didn't understand that..?"
