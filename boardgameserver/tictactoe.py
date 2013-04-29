from functools import reduce
import operator

class Game():
    def __init__(self):
        self.Turn = 1
    def nextTurn(self):
        self.Turn = self.Turn + 1
        # TODO: this looks like a good place to put an AI's-turn callback...

class GameException(Exception):
    pass

class GameSetupException(GameException):
    pass

class GameMoveException(GameException):
    pass

class MultiPlayerGame(Game):
    def __init__(self, names):
        super().__init__()
        self.Players = names

    def currentPlayer(self):
        return self.Players[(self.Turn - 1) % len(self.Players)] # - 1 because turn number is 1-based, not 0

    def nextPlayer(self):
        return self.Players[self.Turn % len(self.Players)]

class TicTacToe(MultiPlayerGame):
    def __init__(self, names):
        if len(names) != 2:
            raise GameSetupException('TicTacToe is a two-player game.')
        super().__init__(names)
        self.Board = [['' for i in range(3)] for i in range(3)]
        self.Symbols = { self.Players[0] : 'X', self.Players[1]: 'O' }

    def checkWin(self):
        wins =\
            [[(i,j) for j in range(3)] for i in range(3)] +\
            [[(j,i) for j in range(3)] for i in range(3)] +\
            [[(i,i) for i in range(3)]] +\
            [[(i,2-i) for i in range(3)]]
        return reduce(operator.__or__, map(lambda row: reduce(operator.__and__, map(lambda coord: self.Board[coord[0]][coord[1]] == self.Symbols[self.currentPlayer()], row)), wins))
    
    def move(self, player, coord): # returns True if this is a winning move
        if player != self.currentPlayer():
            if player in self.Players:
                message = "It's not {0}'s turn in this game."
            else:
                message = "{0} isn't even playing in this game!"
            raise GameMoveException(message.format(player))

        if coord[0] not in range(3) or coord[1] not in range(3):
            raise GameMoveException('Nonsensical board position requested.')
        
        if self.Board[coord[0]][coord[1]] != '':
            raise GameMoveException('Board position already occupied.')

        self.Board[coord[0]][coord[1]] = self.Symbols[self.currentPlayer()]
        status = self.currentPlayer() if self.checkWin() else None
        self.nextTurn()
        return status

