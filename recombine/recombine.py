
import pygame
from pygame import rect, draw, event
import time

from recombinations import *

# game variables

mode = 'normal' # set to 'rapidfire' for nonstop single-green drops
# (anything else is === 'normal')
autofire = True # only used with 'rapidfire'

boardheight = 7
boardwidth = 7
currentcolor = 3
frame = 1.0/30
idletime = 1 * frame
droptime = 2 * frame
breaktime = 15 * frame
frametime = idletime # initial
gridsize = 40
boardoffset = int(gridsize/2)
maxcolor = 10
mouse = (0, 0)
turn = 0
score = 0

state = 'idle'

# init

pygame.init()
scorefont = pygame.font.Font(pygame.font.get_default_font(), 14)
window = pygame.Rect(0, 0, gridsize*boardwidth + 2*boardoffset, gridsize*boardheight + 3*boardoffset)
screen = pygame.display.set_mode((gridsize*boardwidth + 2*boardoffset, gridsize*(boardheight+2) + 3*boardoffset)) # ??
#screen = pygame.display.set_mode(window...
window = screen.get_rect()

background = pygame.Color('gray')
board = Board((boardheight, boardwidth), maxcolor)
boardpos = pygame.Rect((boardoffset, 2*boardoffset), (boardwidth*gridsize, (boardheight+2)*gridsize))
scoreoffset = (boardoffset, boardoffset)
combinecolors = ['green', 'yellow', 'orange', 'red', 'magenta', 'purple', 'blue', 'cyan', 'black', 'white']
combinecolors = [None] + list(map(pygame.Color, combinecolors)) # generate Color objects and put a placeholder in position 0
combinescores = [None, 5, 10, 15, 35, 295, 305, 315, 325, 335, 670]
drop = new_drop(currentcolor, mode)
dropindex = 0
gridcolor = pygame.Color('white')
outlinecolor = pygame.Color('black')

validgroup = lambda l: len(l)>=3

def shutdown():
    pygame.event.clear()
    pygame.quit()
    print(turn)
    print(score)
    quit()
	
# event loop

while True:
    start = time.clock()

    # check events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left
                if state != 'moving' and state != 'pause':
                    state = 'drop'
            if event.button == 3: # right
                if state == 'pause':
                    state = pause # restore
                else:
                    pause = state
                    state = 'pause'
            if event.button == 4: # wheel
                drop = spin(drop, 'right')
            if event.button == 5: # wheel
                drop = spin(drop, 'left')
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                drop = spin(drop, 'right')
            if event.key == pygame.K_DOWN:
                if state != 'moving':
                    state = 'drop'
            if event.key == pygame.K_LEFT:
                dropindex = max(0, dropindex - 1)
            if event.key == pygame.K_RIGHT:
                dropindex = min(dropindex + 1, boardwidth)
        if event.type == pygame.MOUSEMOTION:
            mouse = event.pos
            # game state is updated inside event handling to allow mouse+keyboard input
            ## Adjust mouse position by the border width, clip that at 0.
            ## Scale down by the size of each square and clip that at piece-width away from the right edge.
            dropindex = min(max(mouse[0]-boardoffset, 0) / gridsize, boardwidth - len(drop[0]))
        
        if event.type == pygame.QUIT:
            shutdown()

    # update stuff
    if state == 'drop':
        if mode == 'rapidfire' and autofire:
            dropindex = boardwidth - 1
            while dropindex >= 0 and board[boardheight-1][dropindex] != 0:
                dropindex -= 1
        board.insert(drop, dropindex)
        turn += 1
        state = 'moving'
    elif state == 'moving':
        state = 'moving' if board.gravity() else 'breaking'
        frametime = droptime
    elif state == 'breaking':
        state = 'idle'
        groups = list(filter(validgroup, board.find_groups()))        
        if len(groups) > 0:
            for group in groups:
                groupcolor = board[group[0][0]][group[0][1]]
                currentcolor = max(board.replace_group(group), currentcolor)
                score += combinescores[groupcolor]*len(group)
            frametime = breaktime
            state = 'moving'
        else:
            if board.overheight():
                state = 'gameover'
            else:
                drop = new_drop(currentcolor, mode)
                frametime = idletime
                state = 'idle'
                if mode == 'rapidfire':
                    state = 'drop'
    elif state == 'gameover':
        break

    # draw board
    
    screen.fill(background)
    
    draw.line(screen, gridcolor, (boardpos.left, boardpos.top + 2*gridsize), (boardpos.right, boardpos.top + 2*gridsize), 3)
    draw.rect(screen, outlinecolor, boardpos, 4) # board outline
    
    #colored blockies
    
    for level in range(1, currentcolor):
        r = pygame.Rect(0,0,0,0)
        r.top = 10
        r.height = gridsize/2
        r.left = boardwidth * gridsize - gridsize/2 * len(combinecolors) + gridsize/2 * level
        r.width = gridsize/2
        draw.ellipse(screen, combinecolors[level], pygame.Rect(r.left, r.top, r.width, r.height), 0)
        
    piece = pygame.Rect(boardpos) # to be reused
    piece.width = piece.height = gridsize
    
    if state == 'idle':
        # draw drop
        for i in range(0, len(drop)):
            for j in range(0, len(drop[0])):
                piece.top = boardpos.top + (1 - i)*gridsize
                offset = min(dropindex, boardwidth - len(drop[0]))
                piece.left = boardpos.left + (j + offset)*gridsize
                draw.ellipse(screen, combinecolors[drop[i][j]], piece, 0)
    
    # draw pieces
    
    for i in range(0, len(board.grid)):
        piece.bottom = boardpos.bottom - i*gridsize
        for j in range(0, len(board.grid[0])):
            piece.left = boardpos.left + j*gridsize
            if board[i][j] > 0:
                #draw.rect(screen, combinecolors[board[i][j]], piece, 0)
                draw.ellipse(screen, combinecolors[board[i][j]], piece, 0)
    
    screen.blit(scorefont.render(str(score), True, gridcolor), scoreoffset)

    if state == 'pause':
        pausenote = scorefont.render('paused', True, gridcolor)
        screen.blit(pausenote, window.center) # not properly centered...
    
    pygame.display.flip()

    #timing

    elapsed = time.clock() - start
    if elapsed < frametime:
        time.sleep(frametime - elapsed)

# finally
shutdown()

