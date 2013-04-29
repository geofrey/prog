
import math
import pygame
import time

import flyingbox
import minicontrol
from helladefs import *

# setup

pygame.init()

#bgimage = pygame.image.load('background_1.jpg')
bgimage = pygame.image.load('background_2.png')
window = bgimage.get_rect()
screen = pygame.display.set_mode((window.width, window.height))
bgimage.convert()

background = (128, 128, 128)

mouse = Point(0, 0)

frametime = 0.0 # start out 0, will be dynamically adjusted
paused = True

# setup game objects

gravity = 500.0
lift = 1000.0 # max thrust
tiltstrength = 30.0

chopper = flyingbox.FlyingBox(lift, gravity, tiltstrength, Point(window.centerx, window.centery), 'copter_2.png', Point(52, 29))
minicontrol = minicontrol.MiniControl(Point(window.right - 100, 0), Point(100, 100), centerdot=Point(0.5, gravity / lift))

chopper.update(Point(0.5, 0.5), 0)
# functions

while True:
	start = time.clock()

	# check events
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				paused = not paused
			if event.button == 2:
				chopper.reset()
			if event.button == 3:
				pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
		if event.type == pygame.MOUSEMOTION:
			mouse.x = float(event.pos[0])/window.width
			mouse.y = float(event.pos[1])/window.height
		if event.type == pygame.QUIT:
			pygame.event.clear()
			pygame.quit()
			quit()

	# update physics

	# 'unpausable' objects
	minicontrol.update(mouse)

	# 'pausable' objects
	if not paused:
		chopper.update(mouse, frametime)

	# draw stuff

	screen.blit(bgimage, (0, 0))
	minicontrol.draw(screen)
	chopper.draw(screen)
	pygame.display.flip()

	#timing

	elapsed = time.clock() - start
	if elapsed < frametime:
		if frametime - elapsed > elapsed / 4:
			frametime -= 0.001
		time.sleep(frametime - elapsed)
	else:
		#print "Frame time exceeded: %f" % elapsed
		frametime += 0.010

# if we ever break out of the loop for some unexpected reason:
pygame.event.clear()
pygame.quit()
quit()

