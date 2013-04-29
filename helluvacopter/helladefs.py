
import math

def distance(pointA, pointB=(0, 0)):
	return math.sqrt((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2)

class Point:
	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __getitem__(self, index):
		if index == 0:
			return self.x
		elif index == 1:
			return self.y
		else:
			raise IndexError('tuple index out of range')

	def __str__(self):
		return '(%f, %f)' % (self.x, self.y)

	def __repr__(self):
		return '<Point object, x: %f, y: %f>' % (self.x, self.y)

	def get_tuple(self):
		return (self.x, self.y)

	def set_tuple(self, point):
		self.x = point[0]
		self.y = point[1]

	def from_tuple(tuple):
		return Point(tuple[0], tuple[1])

	def rotate(self, angle):
		return Point(
			self.x * math.cos(angle) + self.y * math.sin(angle),
			-self.x * math.sin(angle) + self.y * math.cos(angle))


