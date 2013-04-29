import sys

class Peg:
	def __init__(self, ID, x, y, full=True):
		self.ID = ID
		self.x = x
		self.y = y
		self.status = full
		self.neighbors = {}
	def isFull(self):
		return self.status
	def isEmpty(self):
		return not self.status
	def set(self):
		self.status = True
	def clear(self):
		self.status = False

def load_board(filename):
	global board
	file = open(filename, 'r')
	board = {}
	minx = float('+inf')
	miny = float('+inf')
	maxx = float('-inf')
	maxy = float('-inf')
	for line in file.readlines():
		# ID	x	y	{direction+neighborID}
		# string	float	float	1char+string
		# ID* means leave empty
		if line[0] == '#':
			continue
		line = line.strip().split('\t')
		current = line[0]
		if current not in board:
			x = float(line[1])
			y = float(line[2])
			full = True
			if current[-1] == '*':
				current = current[:-1]
				full = False
			board[current] = Peg(current, x, y, full) # peg state comes from datafile
			if x < minx:
				minx = x
			if x > maxx:
				maxx = x
			if y < miny:
				miny = y
			if y > maxy:
				maxy = y
		for link in line[3:]:
			direction = link[0]
			destination = link[1:]
			#if destination not in board:
			#	board[destination] = Peg()
			board[current].neighbors[direction] = destination
	global boardwidth
	boardwidth = maxx - minx
	global boardheight
	boardheight = maxy - miny
	return board

#boardfile = 'triangle-5.dat'
#boardfile = 'cross-short.dat'
boardfile = 'wagonwheel3.dat'

if len(sys.argv) > 1:
        boardfile = sys.argv[1]

board = load_board(boardfile)

def move(source, destination):
	if source not in board:
		return False
	if destination not in board:
		return False
	for d in board[source].neighbors:
		midpoint = board[source].neighbors[d]
		if d in board[midpoint].neighbors:
			if board[midpoint].neighbors[d] == destination:
				# valid direction to move
				if board[source].isFull() and board[midpoint].isFull() and board[destination].isEmpty():
					board[source].clear()
					board[midpoint].clear()
					board[destination].set()
					return True
	return False # no valid move was found

def do_move(command):
	command = command.split()
	if len(command) != 2:
		return	
	src, dst = command[0], command[1]
	if len(src) > 0 and len(dst) > 0:
		move(src, dst)

# GUI stuff from here on

import math
import pygame
import random
import time

def euclideandistance(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# constants
# boardwidth and boardheight set previously
gridsize = 50
margin = gridsize # could be bigger or smaller, too
holesize = 30
pegsize = 25

# init
pygame.init()
screen = pygame.display.set_mode((int(gridsize * boardwidth + 2*margin), int(gridsize * boardheight + 2*margin)))
window = screen.get_rect()

# game variables
trytomove = False
mouse = (0, 0)
background = (127, 127, 127)
holecolor = (63, 63, 63)
pegcolor = pygame.Color('white')
highlightcolor = pygame.Color('red')
frametime = 1.0/10
pointedat = None
origin = None
destination = None

state = 'select origin'
	
while True:
	framestart = time.clock()
	
	# handle events
	for event in pygame.event.get():
		if event.type == pygame.MOUSEMOTION:
			mouse = event.pos[0], window.height - event.pos[1]
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: # right-click
				if state == 'select origin':
					state = 'set origin'
				elif state == 'select destination':
					state = 'set destination'
			if event.button == 2: # middle-click
				state = 'quit'
			if event.button == 3: # left-click
				# reset
				board = load_board(boardfile)
		elif event.type == pygame.QUIT:
			state = 'quit'
		else:
			pass # ignore other events
	
	# update logic
	
	distance = float('+inf')
	for peg in board:
		newdistance = euclideandistance(mouse, (board[peg].x * gridsize, board[peg].y * gridsize))
		if newdistance < distance:
			distance = newdistance
			pointedat = board[peg].ID
	
	if state == 'select origin' or state == 'select destination':
		pass
	elif state == 'set origin':
		if board[pointedat].isFull():
			origin = pointedat
			state = 'select destination'
		else:
			state = 'select origin'
	elif state == 'set destination':
		destination = pointedat
		try:
			move(origin, destination)
		except KeyError:
			pass
		state = 'select origin'
		origin = None
	elif state == 'quit':
		pygame.event.clear()
		pygame.quit()
		quit()
	
	# draw window
	screen.fill(background)
	holerect = pygame.Rect(0, 0, holesize, holesize) # reuse
	pegrect = pygame.Rect(0, 0, pegsize, pegsize) # also reuse

	for peg in board:
		holerect.center = (int(board[peg].x * gridsize), int(window.height - board[peg].y * gridsize))
		pygame.draw.ellipse(screen, holecolor, holerect, 4)
		if board[peg].isFull():
			pegrect.center = (int(board[peg].x * gridsize), int(window.height - board[peg].y * gridsize))
			pygame.draw.ellipse(screen, highlightcolor if peg == origin else pegcolor, pegrect, 0)
	holerect.center = (int(board[pointedat].x * gridsize), int(window.height - board[pointedat].y * gridsize))
	pygame.draw.ellipse(screen, highlightcolor, holerect, 4)
	pygame.display.flip()
	
	frameelapsed = time.clock() - framestart
	if frameelapsed < frametime:
		time.sleep(frametime - frameelapsed)
# </loop>

exit()
