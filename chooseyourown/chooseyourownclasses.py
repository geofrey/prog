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

class Path(Reprobate):
	def __init__(self, name, destination):
		self.name = name
		self.dst = destination
	
	def move(self):
		if self.check():
			raise NotImplemented()
	
	def serialize(self, indent=''):
		return(indent+'path\t{name}\t{dst}'.format(name=self.name, dst=self.dst))

class Action(Reprobate):
	def __init__(self, name, effects, consequences):
		self.name = ''
		self.effects = []
		self.consequences = []
	
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

class Effect:
	# any data?
	def apply(self):
		raise NotImplemented()

class CreateItem(Effect): # see where this is going?
	def __init__(self, item, target):
		raise NotImplemented()

class Item:
	def __init__(self):
		for base in self.__class__.__bases__:
			base.__init__(self) # ugly...
		self.name = ''
		self.description = ''
	
	def serialize(self, indent=''):
		return indent+'\t'.join(['item', self.name, self.description])
	
	@staticmethod
	def load(object):
		item = Item()
		item.name, item.description = object[0]
		return item

class Inventoried(Reprobate):
	def __init__(self):
		self.inventory = []
	
	def serialize(self, indent=''):
		if self.inventory:
			return '\n'.join([indent+'inventory'] + [indent+indentstep+item.serialize() for item in self.inventory])

	# I don't like that this is inconsistent with the other static load methods
	def load(self, data):
		# nothing to load from data[0]
		for entity in data[1]:
			self.inventory.append(Item.load(entity))
					
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
	def __init__(self):
		self.state = {}
	
	def serialize(self, indent=''):
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
		
		Inventoried.__init__(self)
		Stateful.__init__(self)

	def serialize(self, indent=''):
		data = []
		data.append(indent+'\t'.join(['scene', self.id, self.parent, self.description]))
		data += [path.serialize(indent+indentstep) for path in self.paths.values()]
		if self.inventory:
			data.append(Inventoried.serialize(self, indent+indentstep))
		if self.state:
			data.append(Stateful.serialize(self, indent+indentstep))
		return '\n'.join(data)
	
	@staticmethod
	def load(object):
		scene = Scene()
		scene.id, scene.parent, scene.description = object[0][1:]
		
		for details in object[1]:
			name = details[0][0]
			item = details[0][1:]
			if name == 'inventory':
				Inventoried.load(scene, details)
			elif name == 'state':
				raise NotImplemented('Enemy Of The State parsing routine')
			elif name == 'path':
				name, dst = item
				scene.paths[name] = Path(name, dst)
			elif name == 'action':
				raise NotImplemented('No actions. Try again later.')
		return scene

class Player(Inventoried, Stateful):
	def __init__(self):
		self.name = ''
		Inventoried.__init__(self)
		Stateful.__init__(self)
	
	def serialize(self, indent=''):
		data = indent + 'player\t{0}'.format(self.name)
		if self.inventory:
			data += Inventoried.serialize(self, indent+indentstep)
		if self.state:
			data += Stateful.serialize(self, indent+indentstep)
		return data
	
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
	
