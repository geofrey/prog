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
operations['add9'] = lambda value: value+9
operations['negate'] = lambda value: -value
operations['div2'] = lambda value: value/2.0
operations['mul4'] = lambda value: value*4.0

puzzles = {}
puzzles['1'] = CalculatorPuzzle(2, 2, 0, ['add1'])
puzzles['44'] = CalculatorPuzzle(5, 52, 44, ['add9', 'div2', 'mul4', 'negate'])

print(dispatch_operation('add1')(3))

tags = list(puzzles.keys())
tags.sort()
for tag in tags:
    puzzle = puzzles[tag]
    print('level {0}: {1}'.format(tag, puzzle))
    solutions = puzzle.search()
    for solution in solutions:
        print(' {1} {0}'.format(', '.join(solution), '!' if len(solution) < puzzle.moves else '*'))

#
