#!/usr/bin/python3

import sys

# read grid
#  lines must all be the same length, naturally
#  blank line to end
grid = []
shadow = []
line = input()
while len(line)>0:
    grid.append(list(line))
    shadow.append([False for letter in line])
    line = input()

class Location:
    def __init__(self, coords, direction):
        self.coords = coords
        self.direction = direction

# read words
#  one word per line
#  case sensitive wrt/ grid
#  blank line to end
words = {}
wordlist = []
line = input()
try:
    while len(line) > 0:
        words[line] = None
        wordlist.append(line)
        line = input()
except EOFError:
    pass

# build prefix tree
class LetterNode:
    def __init__(self, letter):
        self.letter = letter
        self.end = None # what word ends here. Terminal does not imply leaf
        self.next = {}

letters = LetterNode(None)
for word in words:
    leaf = letters
    for letter in range(len(word)):
        if word[letter] not in leaf.next:
            leaf.next[word[letter]] = LetterNode(word[letter])
        leaf = leaf.next[word[letter]]
        if letter == len(word)-1:
            leaf.end = word

# search grid
directions = {
    'e': (0,1),
    'se': (1,1),
    's': (1,0),
    'sw': (1,-1),
    'w': (0,-1),
    'nw': (-1,-1),
    'n': (-1,0),
    'ne': (-1,1)
}

def trace(i, j, direction):
    ii = i
    di = directions[direction][0]
    jj = j
    dj = directions[direction][1]
    while 0 <= ii and ii < len(grid) and 0 <= jj and jj < len(grid[i]):
        yield grid[ii][jj]
        ii += di
        jj += dj

for i in range(len(grid)):
    for j in range(len(grid[i])):
        for direction in directions:
            cursor = letters
            for letter in trace(i, j, direction):
                if letter not in cursor.next:
                    break
                cursor = cursor.next[letter]
                if cursor.end:
                    words[cursor.end] = Location((i,j), direction)

# output $WORD $ROW,$COL $DIRECTION
#  1,1 is top left corner
#  'east' means right-to-left
for word in wordlist:
    answer = words[word]
    print(word,' not found!' if answer == None else (str(answer.coords[0]+1)+','+str(answer.coords[1]+1)+' '+answer.direction))

for word in words:
    if words[word] == None:
        continue
    i,j = words[word].coords
    step = directions[words[word].direction]
    for n in range(len(word)):
        shadow[i][j] = True
        i += step[0]
        j += step[1]

print()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j] if shadow[i][j] else ' ', end='')
    print()

# TODO
#  case-insensitive search
#  ???
#  profit!
