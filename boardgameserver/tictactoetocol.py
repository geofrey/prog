# TicTacToe client-server defs

COMMAND_CREATE = 'create' # player1 player2
COMMAND_MOVE = 'move' # gameID, player, i, j
COMMAND_RESIGN = 'resign' # gameID, player
COMMAND_SHOW = 'getState' # [gameID]
COMMAND_HELLO = 'helloworld' #

COMMAND_SHUTDOWN = 'shutdown' #


RESPONSE_CREATE = 'created' # gameID
RESPONSE_MOVE = 'moved' #
RESPONSE_GAMEOVER_VICTORY = 'victory'
RESPONSE_GAMEOVER_DEFAULT = 'default'
RESPONSE_GAMEOVER = 'gameover' # winner victory|default
RESPONSE_SHOW = 'status' # array player
RESPONSE_SHOW_ALL = 'games' # (\n gameID player1 player2)
RESPONSE_HELLO = 'server_says' # message

ERROR_GAME = 'game_error' # message
ERROR_COMMAND = 'command_error' # message
ERROR_SERVER = 'internal_error' # message

# some classes to encapsulate different command data?

ENCODING = 'utf-8'
