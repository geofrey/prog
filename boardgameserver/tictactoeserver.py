import socketserver
from tictactoe import *
import tictactoetocol as ttt

class TicTacToeHandler(socketserver.StreamRequestHandler):

    def create(self, player1, player2):
        gameid = str(self.server.nextGameID)
        self.server.nextGameID += 1
        game = TicTacToe([player1, player2])
        game.gameID = gameid
        self.server.games[gameid] = game
        return gameid
    
    def move(self, game, player, i, j):
        victor = self.server.games[game].move(player, (int(i), int(j)))
        if victor:
            del(self.server.games[game])
        return victor

    def resign(self, game, quitter):
        winner = self.server.games[game].nextPlayer()
        del(self.server.games[game]) # game over, man...game over
        return winner
    
    def handle(self):
        print('connection from {0}'.format(self.client_address))
        request = str(self.rfile.readline(), ttt.ENCODING).strip().split()
        print(request)
      
        command, options = (request[0], request[1:]) if len(request) > 0 else ('', [])

        try:
            response = [ttt.ERROR_COMMAND, '"{0}"'.format(command)] # default
            
            if command == ttt.COMMAND_CREATE:
                newgame = self.create(options[0], options[1])
                response = [ttt.RESPONSE_CREATE, newgame]
            
            elif command == ttt.COMMAND_MOVE:
                try:
                    winner = self.move(*options)
                    if winner: # player name on win
                        response = [ttt.RESPONSE_GAMEOVER, winner, ttt.RESPONSE_GAMEOVER_VICTORY]
                    else: # None on not-win
                        response = [ttt.RESPONSE_MOVE]
                except GameException as problem:
                    response = [ttt.ERROR_GAME]
                    response[1:1] = problem.args
            
            elif command == ttt.COMMAND_RESIGN:
                winner = self.resign(options[0], options[1])
                response = [ttt.RESPONSE_GAMEOVER, winner, ttt.RESPONSE_GAMEOVER_DEFAULT]
            
            elif command == ttt.COMMAND_SHOW:
                if len(options) == 0:
                    response = [ttt.RESPONSE_SHOW_ALL]
                    for game in self.server.games.values():
                        response += ['\n', game.gameID, game.currentPlayer(), game.nextPlayer()]
                else:
                    game = self.server.games[options[0]]
                    response = [ttt.RESPONSE_SHOW, str(game.Board), game.currentPlayer(), game.Symbols[game.currentPlayer()]]
            
            elif command == ttt.COMMAND_HELLO:
                message = 'Hello, {name}! I am currently serving {count} games.'.format(name=options[0], count=len(self.server.games))
                response = [ttt.RESPONSE_HELLO, message]
            
            elif command == ttt.COMMAND_SHUTDOWN:
                response = ['bye.']
                self.server.keep_calm_and_carry_on = False
        except anything:
            response = [ttt.ERROR_SERVER, str(anything)]
        finally:
            response.append('\n')
            print(response)
            self.request.send(bytes(' '.join(response), ttt.ENCODING))

class ReusePortTCPServer(socketserver.TCPServer):
    def __init__(self, addr, handler):
        self.allow_reuse_address = True # to avoid headaches during testing. Should probably take this out later, assuming there's a good reason ports aren't normally shared.
        super().__init__(addr, handler)
        self.keep_calm_and_carry_on = True
        
        self.games = {}
        self.nextGameID = 1

print('server starting...')
server = ReusePortTCPServer(('localhost', 1234), TicTacToeHandler)

try:
    while server.keep_calm_and_carry_on:
        server.handle_request()
    print('server has exited normally')
except Exception as problem:
    print('emergency shutdown: {wahwah}'.format(wahwah=problem))
finally:
    server.server_close()
print('bye')
