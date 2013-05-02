import sys

global scenelist
scenelist = {}

class Scene:
   def __init__(self, data):
      # scene definition consists of:
      # first line: scene ID
      # second line: description
      # additional lines: command + scene ID pairs defining where you can go from here
      self.id = data[0]
      self.description = data[1]
      self.options = dict([(o[0], o[1]) for o in [word.split('\t') for word in data[2:]]])


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
      return Scene(textchunk)

if len(sys.argv) == 2:
   story = sys.argv[1]
else:
   print 'What story would you like to play? Type a file name:'
   story = sys.stdin.readline().strip()

scene = get_scene(open(story))
while scene is not None:
   scenelist[scene.id] = scene
   scene = get_scene(story)
del(scene, story)


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
