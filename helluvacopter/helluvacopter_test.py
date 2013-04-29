
import math
import pygame
import time

import flyingbox
import helladefs

# setup

pygame.init()
bgimage = pygame.image.load('background_1.jpg')
window = bgimage.get_rect()
screen = pygame.display.set_mode((window.width, window.height))
bgimage.convert()

background = (128, 128, 128)
white = (255, 255, 255)

mouse = (0, 0)

frametime = 0.0 # start out 0, will be dynamically adjusted
delay = 0.000
start = time.time()
paused = True

# setup game objects
minicontrol = pygame.Rect(0, 0, 100, 100)
minicontrol.top = window.top + 1
minicontrol.right = window.right - 1


gravity = 25.0

boxlift = 50.0 # max thrust

chopper = FlyingBox(boxlift, boxtiltstrength, screen.get_rect().center, 'copter_2.png')
chopper.reset()

boxtiltstrength = 5

boxpos = [float(screen.get_rect().centerx), float(screen.get_rect().centery)]
boxspeed = [0.0, 0.0]
boxangle = 0.0
boxtiltspeed = 0.0
boxthrust = [0.0, 0.0]

boxpic = pygame.image.load('copter_2.png')
boxpic.convert_alpha()

# functions

def boxreset():
	global boxpos, boxspeed, boxangle, boxtiltspeed, boxthrust
	boxpos = [float(screen.get_rect().centerx), float(screen.get_rect().centery)]
	boxspeed = [0.0, 0.0]
	boxangle = 0.0
	boxtiltspeed = 0.0
	boxthrust = [0.0, 0.0]

def drawbox():
	rotocopter = pygame.transform.rotate(boxpic, -math.degrees(boxangle))
	screen.blit(
		rotocopter, 
		(
			boxpos[0] - rotocopter.get_width() / 2,
			boxpos[1] - rotocopter.get_height() / 2
		))
	pygame.draw.line(
		screen, 
		(0, 127, 0), 
		boxrect.center, 
		(
			boxpos[0] + gravity * boxspeed[0], 
			boxpos[1] - gravity * boxspeed[1]
		))
# 	pygame.draw.line(
# 		screen, 
# 		(192, 0, 0), 
# 		boxrect.center, 
# 		(
# 			boxpos[0] + 50 / gravity * boxthrust[0], 
# 			boxpos[1] - 50 / gravity * boxthrust[1]
# 		))

while True:
	# check events
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				paused = not paused
			if event.button == 2:
				boxreset()
			if event.button == 3:
				pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
			if event.button == 4:
				if delay < 0.010:
					delay -= 0.010
			if event.button == 5:
				delay += 0.010
		if event.type == pygame.MOUSEMOTION:
			mouse = event.pos
		if event.type == pygame.QUIT:
			pygame.event.clear()
			pygame.quit()
			quit()

	# update physics

	# 'unpausable' objects
	#none

	# 'pausable' objects
	if not paused:
		boxtiltspeed = boxtiltstrength * float(mouse[0] - window.centerx) / window.centerx
		boxangle += boxtiltspeed * frametime
		if boxangle < -math.pi:
			boxangle += 2*math.pi
		if boxangle > math.pi:
			boxangle -= 2*math.pi
		boxangle *= 0.95 # return to center

		boxthrust = [
			math.sin(boxangle) * boxlift * float(window.height - mouse[1]) / window.height,
			math.cos(boxangle) * boxlift * float(window.height - mouse[1]) / window.height ]

		boxspeed[0] += boxthrust[0] * frametime
		boxspeed[1] += (boxthrust[1] - gravity) * frametime

		boxpos[0] += boxspeed[0]
		boxpos[1] -= boxspeed[1]

	# draw stuff
	#screen.lock()

	screen.fill(background) # is this right?
	screen.blit(bgimage, (0, 0))

	drawbox()
	
	pygame.draw.line(
		screen, 
		white,
		(minicontrol.left + minicontrol.width * mouse[0] // window.width, minicontrol.top),
		(minicontrol.left + minicontrol.width * mouse[0] // window.width, minicontrol.bottom))
	pygame.draw.line(
		screen,
		white,
		(minicontrol.left, minicontrol.top + minicontrol.height * mouse[1] // window.height),
		(minicontrol.right, minicontrol.top + minicontrol.height * mouse[1] // window.height))
	pygame.draw.rect(screen, white, minicontrol, 1)

	pygame.display.flip()

	# timing
	time.sleep(delay)
	elapsed = time.time() - start
	if elapsed < frametime:
		if frametime - elapsed > elapsed / 4:
			frametime -= 0.001
		time.sleep(frametime - elapsed)
	else:
		#print "Frame time exceeded: %f" % elapsed
		frametime += 0.010
	start = time.time()

# if we ever break out of the loop for some unexpected reason:
pygame.event.clear()
pygame.quit()
quit()

