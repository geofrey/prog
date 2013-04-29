import pygame
import math

from helladefs import *

class FlyingBox:
	def __init__(self, max_power, gravity, max_tilt_power, pos, imagefilename, imagecenter=None):
		self.max_power = max_power
		self.max_tilt_power = max_tilt_power
		self.gravity = gravity
		self.pos_init = pos
		self.image = pygame.image.load(imagefilename)
		self.image.convert_alpha()
		if imagecenter == None:
			self.imageoffset = Point(
				self.image.get_width() / 2,
				self.image.get_height() / 2)
		else:
			# center measured from top left corner
			# converted to on-screen offset from center
			self.imageoffset = Point(
				imagecenter.x - self.image.get_width()/2,
				imagecenter.y - self.image.get_height()/2)
		self.reset()

	def reset(self):
		self.pos = Point.from_tuple(self.pos_init)
		self.speed = Point(0.0, 0.0)
		self.angle = 0.0
		self.tiltspeed = 0.0

	def draw(self, surface):
		rotobox = pygame.transform.rotate(self.image, -math.degrees(self.angle))
		rotooffset = self.imageoffset.rotate(-self.angle)
		surface.blit(
				rotobox, 
				(
					self.pos.x - rotobox.get_width()/2 - rotooffset.x, 
					self.pos.y - rotobox.get_height()/2 - rotooffset.y))
		pygame.draw.line(
			surface,
			(0, 127, 0), # dark green
			self.pos.get_tuple(),
			(self.pos.x + 20 / self.max_power * self.speed.x, self.pos.y - 20 / self.max_power * self.speed.y))

	def update(self, control_in, time):
		control = Point(control_in.x - 0.5, 1.0 - control_in.y)

		tilt_power = control.x * self.max_tilt_power - self.gravity / self.max_tilt_power * math.sin(self.angle)
		self.tiltspeed += tilt_power * time
		self.tiltspeed *= 0.95 # attenuation
		self.angle += self.tiltspeed * time
		if self.angle < -math.pi:
			self.angle += 2*math.pi 
		if self.angle > math.pi:
			self.angle -= 2*math.pi

		power = Point(
				math.sin(self.angle) * self.max_power * control.y,
				math.cos(self.angle) * self.max_power * control.y)

		self.speed.x += power.x * time
		self.speed.y += (power.y - self.gravity) * time

		self.pos.x += self.speed.x * time
		self.pos.y -= self.speed.y * time
