class QuadTree:
	class Node:
		def __init__(self, location, value):
			self.location = location
			self.neighbor = {}
			self.value = value
		def compare(self, location):
			easter = location[0] > self.location[0]
			norther = location[1] > self.location[1]
			if easter:
				if norther:
					return 'ne'
				else:
					return 'se'
			else:
				if norther:
					return 'nw'
				else:
					return 'sw'
		def insert(self, incoming):
			direction = self.compare(incoming.location)
			if direction in self.neighbor:
				self.neighbor[direction].insert(incoming)
			else:
				self.neighbor[direction] = incoming
		# </Node>
	def __init__(self):
		self.root = None
	def insert(self, location, value):
		incoming = QuadTree.Node(location, value)
		if self.root == None:
			self.root = incoming
		else:
			self.root.insert(incoming)
	def closest(self, location):
		parent = self.root
		current = self.root
		closest = {}
		# drill down to strict-closest
		direction = current.compare(location)
		while direction in current.neighbor:
			parent = current
			closest[direction] = current
			current = current.neighbor[direction]
			direction = current.compare(location)
		distance = float('+inf')
		winner = None
		for candidate in closest.values():
			newdistance = cartesiandistance(candidate.location, location)
			if newdistance < distance:
				winner = candidate
				distance = newdistance
		return winner
# </QuadTree>

import math
def cartesiandistance(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)