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
        if moves < 1:
            return
        solutions = []
        for button in self.buttons:
            result = dispatch_operation(button)(value)
            print('{0} {1} -> {2}'.format(value, button, result))
            print('{0} {1} {2}'.format(result, '==' if result == self.goal else '!=', self.goal))
            if result == self.goal:
                print('{0} solves!'.format(stack))
                solutions.append(stack)
            self.search_rec(moves-1, result, stack+[button], solutions)
    
    def __str__(self):
        return '{0} -> {1} in {2} using [{3}]'.format(self.initial, self.goal, self.moves, ', '.join(self.buttons))
    

puzzles = []

puzzles.append(CalculatorPuzzle(2, 2, 0, ['add1']))

operations['add1'] = lambda value: value+1

print(dispatch_operation('add1')(3))

for i in range(0, len(puzzles)):
    print('level {0}: {1}'.format(i, puzzles[i]))
    solutions = puzzles[i].search()
    for solution in solutions:
        print(', '.join(solution))

#
