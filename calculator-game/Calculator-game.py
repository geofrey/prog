operations = {}
def dispatch_operation(name):
    operation = operations[name]
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
            result = dispatch_operation(button)(value)
            #print('{0} {1} -> {2}'.format(value, button, result))
            #print('{0} {1} {2}'.format(result, '==' if result == self.goal else '!=', self.goal))
            if result == self.goal:
                #print('{0} solves!'.format(nextstack))
                solutions.append(nextstack)
            self.search_rec(moves-1, result, nextstack, solutions)
    
    def __str__(self):
        return '{0} -> {1} in {2} using [{3}]'.format(self.initial, self.goal, self.moves, ', '.join(self.buttons))
    
operations['add1'] = lambda value: value+1
operations['add2'] = lambda value: value+2
operations['add3'] = lambda value: value+3
operations['add4'] = lambda value: value+4
operations['add5'] = lambda value: value+5
operations['add6'] = lambda value: value+6
operations['add8'] = lambda value: value+8
operations['add9'] = lambda value: value+9

operations['delete'] = lambda value: int(value/10) # this might not always work

operations['div2'] = lambda value: value/2.0
operations['div3'] = lambda value: value/3.0
operations['div4'] = lambda value: value/4.0
operations['div5'] = lambda value: value/5.0
operations['div7'] = lambda value: value/7.0

operations['edit1-2'] = lambda value: float(str(value).replace('1', '2'))
operations['edit2-3'] = lambda value: float(str(value).replace('2', '3'))
operations['edit6-9'] = lambda value: float(str(value).replace('6', '9'))
operations['edit8-4'] = lambda value: float(str(value).replace('8', '4'))

operations['mul2'] = lambda value: value*2
operations['mul3'] = lambda value: value*3
operations['mul4'] = lambda value: value*4
operations['mul5'] = lambda value: value*5
operations['mul7'] = lambda value: value*7
operations['mul9'] = lambda value: value*9
operations['mul10'] = lambda value: value*10
operations['mul11'] = lambda value: value*11

operations['negate'] = lambda value: -value

operations['sub2'] = lambda value: value-2
operations['sub5'] = lambda value: value-5
operations['sub8'] = lambda value: value-8
operations['sub9'] = lambda value: value-9

operations['type0'] = lambda value: value*10+0
operations['type1'] = lambda value: value*10+1
operations['type2'] = lambda value: value*10+2
operations['type5'] = lambda value: value*10+5
operations['type10'] = lambda value: value*100+10
operations['type12'] = lambda value: value*100+12


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
    for button in buttons:
        if button not in operations:
            print('WARNING - puzzle {0} operation {1} is not defined'.format(id, button))
    
    puzzles[id] = CalculatorPuzzle(moves, goal, initial, buttons)

puzzles['44'] = CalculatorPuzzle(5, 52, 44, ['add9', 'div2', 'mul4', 'negate'])

tags = list(puzzles.keys())
tags.sort()
for tag in tags:
    puzzle = puzzles[tag]
    print('level {0}: {1}'.format(tag, puzzle))
    solutions = puzzle.search()
    for solution in solutions:
        print(' {1} {0}'.format(', '.join(solution), '!' if len(solution) < puzzle.moves else '*'))

#
