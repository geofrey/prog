#!/cygdrive/c/PROGRA~1/Python25/python.exe

import cmath
import pygame
import time
import threading
import sys

def dprint(message, importance=-1):
	global debuglevel
	if importance >= debuglevel:
		print message
		sys.stdout.flush()

debuglevel=-3
dprint('debug ON', -1)

def mandelpaint():
	global screen
	global view
	global iterations
	palette = [
		(255,
		int(255.0 * n / iterations),
		int(255.0 * n / iterations)) for n in range(0, iterations + 1)]
	
	#dprint('create pixelarray')
	#canvas = pygame.PixelArray(screen)
	width = screen.get_width()
	height = screen.get_height()
	dprint('drawing on %i by %i' % (width, height), -2)
	
	t = view.top
	b = view.bottom
	l = view.left
	r = view.right
	w = r - l
	h = t - b
	dprint('view size %f by %f' % (w, h), -2)
	
	for imag in range(0, height):
		dprint('start drawing row', -4)
		for real in range(0, width):
			r = (w * real)/width + l
			i = (h * imag)/height + b
			C = complex(r, i)
			Z = complex(0.0, 0.0)
			
			n = 0
			while(n < iterations and abs(Z) < 2.0):
				Z = Z*Z + C
				n = n + 1
			if n < iterations:
				dprint('%f, %f OUTSIDE after %i iterations' % (r, i, n), -5)
				#canvas[real][imag] = palette[n]
				screen.set_at((real, imag), palette[n])
			else:
				dprint('%f, %f INSIDE' % (r, i), -5)
				screen.set_at((real, imag), (0, 0, 0))
				
	# done
	dprint('image completed')
	quit()

def exit():
	dprint('bye', 0)
	pygame.event.clear()
	pygame.quit()
	quit()

class View:
	def __init__(self):
		self.top = 1.1
		self.bottom = -1.1
		self.left = -2.1
		self.right = 0.7

	def reset(self):
		dprint('reset to default view')
		self.__init__()

	def zoom(self, r, i):
		dprint('zoom in on %f, %f' % (r, i))
		factor = 2.0
		self.top = i + (self.top - i)/factor
		self.bottom = i - (i - self.bottom)/factor
		self.left = r - (r - self.left)/factor
		self.right = r + (self.right - r)/factor
		
		dprint('new window (%f, %f) x (%f, %f)' % (self.left, self.top, self.right, self.bottom), -1)

view = View()

width = 300
height = 200
frametime = 1.0/15 # make  > 0 to enable throttling

dprint('create canvas')
pygame.init()
screen = pygame.display.set_mode((width, height))
image = pygame.Surface((width, height))

# asynchronous compute and draw
def startdrawing():
	# TODO: check if painter exists, kill it if it does
	painter = threading.Thread(None, mandelpaint, 'painter', [])
	painter.start()

iterations = 80
view.reset()
startdrawing() # initial render

dprint('start event loop')
while True:
	start = time.time()
	
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			dprint('mouse button %i' % event.button, -2)
			if event.button == 1:
				dprint('mouse button')
				dprint('coords: %i, %i' % (event.pos[0], event.pos[1]), -2)
				view.zoom(
					view.left + event.pos[0] * ((view.right - view.left)/width),
					view.bottom + (event.pos[1]) * ((view.top - view.bottom)/height))
			elif event.button == 2:
				view.reset()
			elif event.button == 3:
				exit()
			elif event.button == 4:
				# scrool up
				iterations = int(iterations * 1.5)
				dprint('%i iterations' % (iterations))
			elif event.button == 5:
				# scrool down
				iterations = max(int(iterations * 2.0/3), 2)
				dprint('%i iterations' % (iterations))
			startdrawing() # every button event wants a redraw
		elif event.type == pygame.MOUSEMOTION:
			dprint('mouse at %i, %i' % (event.pos[0], event.pos[1]), -3)
		elif event.type == pygame.QUIT:
			dprint('window closed')
			exit()
		# ignore unspecified event types
	
	#dprint('copy image', -3)
	#screen.blit(image, screen.get_rect())
	pygame.display.flip()
	
	if frametime > 0:
		elapsed = time.time() - start
		while elapsed > frametime:
			elapsed = elapsed - frametime
		delay = frametime - elapsed
		dprint('sleep %f' % frametime, -4)
		time.sleep(delay)

dprint('wtf how did I get here?', 1)
exit()

