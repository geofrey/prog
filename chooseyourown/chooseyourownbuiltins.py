# builtin commands

global game

builtins = {
	'!exit': lambda: bi_exit(),
	'inv': lambda: inv(),
	'look': lambda: look(),
	'aoeusnth': None
}

def bi_exit():
	__builtins__.exit() # completely exit Python. Rather extreme, noL?

def inv():
	print(game.player.inventory)

def look():
	print(game.scenelist[current].inventory)

