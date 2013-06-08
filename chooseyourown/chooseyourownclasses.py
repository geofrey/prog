from chooseyourownutil import *

global indentstep
indentstep = '\t'

class NotImplemented(Exception):
	pass

class Reprobate: # because "__repr__", get it?
	def serialize(self, indent=''):
		pass
	
	def __repr__(self, theType=None, seen=[], indent=''):
		if not theType:
			theType = self.__class__ # hmmm.
		
		data = []
		
		datum = theType.serialize(self, indent)
		if datum: # handle None and '' and [] etc.
			data.append(datum)
		
		for subtype in theType.__bases__:
			if subtype not in seen:
				data.append(subtype.__repr__(self, subtype, seen+[subtype], indent+indentstep))
		return '\n'.join(data)

class EventListener(Reprobate):
	events = {} # name : [action]
	
	def serialize(self, indent):
		if len(events) == 0:
			return indent
		# else:
		title = indent + 'events'
		content = '\n'.join([indent+indentstep+'{name}\t{value}'.format(name=item, value=self.events[item]) for item in self.events.keys()])
		return title + '\n' + content
	
	def dispatch(self, event):
		if event in self.events:
			for action in self.events[event]:
				action.execute()
	
	def hook(self, event, action):
		if event not in self.events:
			self.events[event] = []
		self.events[event].append(action)

class Predicated(Reprobate):
	conditions = []
	
	def serialize(self, indent=''):
		return '\n'.join([indent+'conditions'] + [indent + indentstep + '{name}\t{value}'.format(name=item, value=self.conditions[item]) for item in self.conditions])
		
	def check(self):
		# evaluate conditions
		# may need more parameters
		raise NotImplemented()

class Path(Predicated):
	name=''
	dst=''
	
	def __init__(self, name, destination):
		self.name = name
		self.dst = destination
	
	def move(self):
		if self.check():
			raise NotImplemented()
	
	def serialize(self, indent=''):
		return(indent+'path\t{name}\t{dst}'.format(name=self.name, dst=self.dst))

class Action(Predicated):
	name = ''
	effects = []
	consequences = []
	
	def serialize(self, indent=''):
		data = []
		data.append(indent+'action'+'\t'+self.name)
		if self.effects:
			data.append(indent+indentstep+'effects')
			data += [effect.serialize(indent+indentstep*2) for effect in self.effects]
		if self.consequences:
			data.append(indent+indentstep+'consequences')
			data += [orelse.serialize(indent+indentstep*2) for orelse in self.consequences]
		return 
	
	def execute(self):
		if self.check():
			for effect in effects:
				effect.apply()
		else:
			for effect in consequences:
				effect.apply()

class Effect(Reprobate):
	# any data?
	def apply(self):
		raise NotImplemented()

class CreateItem(Effect): # see where this is going?
	def __init__(self, item, target):
		raise NotImplemented()

class Item(EventListener):
	name = ''
	description = ''
	
	def __init__(self, name, description):
		self.name = name
		self.description = description

class Inventoried(Reprobate):
	inventory = []
	
	def serialize(self, indent=''):
		if self.inventory:
			return [indent+'inventory'] + '\n'.join([indent+indentstep+item for item in self.inventory])
	
	def add(self, item):
		self.inventory.append(item)
	
	def remove(self, item):
		for myItem in self.inventory:
			if myItem.name == item.name:
				self.inventory.remove(myItem)
				return # yes return from the middle of the loop
	
	def has(self, item):
		for myItem in self.inventory:
			if myItem.name == item.name:
				return True
		return False

class Stateful(Reprobate):
	state = {}
	
	def serialize(self, indent):
		if self.state:
			return '\n'.join([indent+'state'] + [indent+indentstep+'{name}\t{value}'.format(name=item, value=self.state[item]) for item in self.state])
	
	def set(self, name, value):
		self.state[name] = value
	
	def unset(self, name):
		self.state.remove(name)
	
	def get(self, name, recurse=True):
		if name in self.state:
			return self.state[name]
		elif recurse:
			#somehow get parent and ask them
			raise NotImplemented()
		else:
			return None

class Scene(Inventoried, Stateful):
	def __init__(self):
		id = None
		self.description = ''
		self.paths = {}
		self.parent = None

	def serialize(self, indent=''):
		data = []
		data.append(indent+'\t'.join(['scene', self.id, self.parent, self.description]))
		# description and parent don't get their own lines yet
		#data.append(indent+indentstep+'desc\t{0}'.format(self.description))
		#if self.parent:
		#	data.append(indent+indentstep+'parent\t{0}'.format(self.parent))
		data += [path.serialize(indent+indentstep) for path in self.paths.values()]
		return '\n'.join(data)
	
	@staticmethod
	def load(object):
		scene = Scene()
		scene.id, scene.parent, scene.description = object[0][1:]
		
		for details in object[1]:
			name = details[0][0]
			item = details[0][1:]
			if name == 'inventory':
				raise NotImplemented('Inventory is backordered.')
			elif name == 'state':
				raise NotImplemented('Enemy Of The State parsing routine')
			elif name == 'path':
				name, dst = item
				scene.paths[name] = Path(name, dst)
			elif name == 'action':
				raise NotImplemented('No actions. Try again later.')
		return scene

class Player(Inventoried, Stateful):
	def serialize(self, indent=''):
		if self.inventory or self.state:
			return indent + 'player\t{0}'.format(self.name)
	
	@staticmethod
	def load(file): # file:Linerator
		raise NotImplemented()

class Game(Reprobate):
	def __init__(self):
		self.scenelist = {}
		self.name = ''
		self.author = ''
		self.initial = ''
		self.world = ''
		self.player = Player()
	
	def serialize(self, indent=''):
		data = [indent+'\t'.join(['story', self.name, self.author, self.initial, self.world])]
		playerdata = self.player.serialize(indent+indentstep)
		if playerdata:
			data.append(playerdata)
		data += [scene.serialize(indent) for scene in self.scenelist.values()]
		return '\n'.join(data)
	
	@staticmethod
	def load(tree):
		game = Game()
		for entity in tree:
			name = entity[0][0]
			data = entity[0][1:]
			if name == 'story':
				game.name, game.author, game.initial, game.world = data
			elif name == 'player':
				raise NotImplemented('Hate the game, don\'t hate the Player parser.')
			elif name == 'scene':
				game.scenelist[data[0]] = Scene.load(entity)
			else:
				raise ValueError('I have no idea what you mean by \'{0}\'. Fix your game file or something.'.format(entity[0][0]))
		return game
