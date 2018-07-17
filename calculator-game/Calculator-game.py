import sys

operations = {}
operations['negate'] = lambda value: -value
# this might be getting too long
operations['delete'] = lambda value: (lambda word: float(word[:-1]) if sum(map(lambda ch: 1 if ch.isdigit() else 0, word))>1 else 0)('{0:.0f}'.format(value))
operations['reverse'] = lambda value: float(''.join(reversed('{0:.0f}'.format(value))))

def dispatch_operation(name):
    operation = None
    if name in operations:
        operation = operations[name]
    elif name.startswith('add'):
        term = int(name[3:])
        operation = lambda value: value + term
    elif name.startswith('div'):
        denominator = float(name[3:])
        operation = lambda value: value/denominator
    elif name.startswith('edit'):
        search, replace = name[4:].split('-')
        operation = lambda value: float(str(value).replace(search, replace))
    elif name.startswith('mul'):
        factor = int(name[3:])
        operation = lambda value: value*factor
    elif name.startswith('sub'):
        term = int(name[3:])
        operation = lambda value: value - term
    elif name.startswith('type'):
        insert = name[4:]
        operation = lambda value: float("{0:g}".format(value)+insert)
    
    if operation == None:
        print('WARNING - operation {0} not defined'.format(name))
    
    return lambda value: operation(value)

class CalculatorPuzzle:
    def __init__(self, moves, goal, initial, buttons):
        self.moves = moves
        self.goal = goal
        self.initial = initial
        self.buttons = buttons
    
    def search(self):
        solutions = []
        self.search_rec(self.moves, self.initial, [], solutions)
        return solutions
    def search_rec(self, moves, value, stack, solutions):
        #print('stack: {0}'.format(stack))
        if moves < 1:
            return
        for button in self.buttons:
            nextstack = stack+[button]
            #if button == 'delete':
            #    sys.stdout.write('{0} {1} -> '.format(value, button))
            result = dispatch_operation(button)(value)
            #if button == 'delete':
            #    print(result)
            #print('{0} {1} {2}'.format(result, '==' if result == self.goal else '!=', self.goal))
            if result == self.goal:
                #print('{0} solves!'.format(nextstack))
                solutions.append(nextstack)
            self.search_rec(moves-1, result, nextstack, solutions)
    
    def __str__(self):
        return '{0} -> {1} in {2} using [{3}]'.format(self.initial, self.goal, self.moves, ', '.join(self.buttons))

puzzles = {}

datafile = open('app-puzzles.dat', 'r')
for line in datafile.readlines():
    if len(line.strip()) == 0 or line.startswith('#'):
        continue
    line = line.split(',')
    
    id = line[0].strip()
    if id in puzzles:
        print('WARNING - replacing puzzle "{0}": {1}'.format(id, puzzles[id]))
    
    moves = int(line[1].strip())
    goal = int(line[2].strip())
    initial = int(line[3].strip())
    buttons = map(lambda token: token.strip(), line[4:])
    
    puzzles[id] = CalculatorPuzzle(moves, goal, initial, buttons)

puzzles['44'] = CalculatorPuzzle(5, 52, 44, ['add9', 'div2', 'mul4', 'negate'])

tags = list(puzzles.keys())
tags.sort()
for tag in tags:
    puzzle = puzzles[tag]
    print('level {0}: {1}'.format(tag, puzzle))
    solutions = puzzle.search()
    if len(solutions) == 0:
        print('WARNING - no solutions for puzzle {0}'.format(tag))
    for solution in solutions:
        print(' {1} {0}'.format(', '.join(solution), '!' if len(solution) < puzzle.moves else '*'))

#
