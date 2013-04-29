
import pygame

from helladefs import *

class MiniControl:
	def __init__(self, pos, size, color=(255, 255, 255), centerdot=None):
		self.pos = pos
		self.size = size
		self.update(Point(0.5, 0.5))
		# self.x inited
		# self.y inited
		self.color = color
		if centerdot != None:
			self.dot = Point.from_tuple(centerdot)
		else:
			self.dot = None

	def update(self, mouserel):
		self.x = mouserel.x
		self.y = mouserel.y

	def draw(self, screen):
		if self.dot != None:
			pygame.draw.circle(
					screen,
					self.color,
					(
						self.pos.x + self.dot.x * self.size.x,
						self.pos.y + self.dot.y * self.size.y),
					4)
		pygame.draw.line(
			screen, 
			self.color,
			(self.pos.x + self.size.x * self.x, self.pos.y),
			(self.pos.x + self.size.y * self.x, self.pos.y + self.size.y))
		pygame.draw.line(
			screen,
			self.color,
			(self.pos.x, self.pos.y + self.size.y * self.y),
			(self.pos.x + self.size.x, self.pos.y + self.size.y * self.y))
		pygame.draw.rect(
				screen, 
				self.color, 
				pygame.Rect(
					self.pos.get_tuple(), 
					self.size.get_tuple()), 
				1)

