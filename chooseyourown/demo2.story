story	Demo Story	gws	intro	world

scene	intro	world	Congratulations! This is the first scene of this interactive fiction. From here you must proceed to the MENU.
	path	menu	menu

scene	menu	world	Where do you want to go now? You can QUIT early, go DENNIS, or explore a passageway that leads to the SOUTH. Or just STAY here.
	path	quit	quit
	path	dennis	dennis # yeah baby, comments!
	path	south	passage1
	path	stay	menu

scene	dennis	world	Dennis doesn't have much to say about this game, but he does seem eager to tell you about parapets. WTF?
	path	back	menu

# also, comments on an otherwise-empty line can be useful

scene	passage1	world	There's a lot of dust and construction debris around here, but the rest of the game is inaccessible. The only way to go is out a DOOR leading back to the shell.
	path	door	quit
	path	back	menu
	
	inventory
		broom	A broom. You know, like for sweeping.
	
	action sweep
		conditions
			inventory broom
		effects
			description	Sweeping up some of the dust from the floor reveals a secret TRAPDOOR - this looks interesting...
			path	add	trapdoor	secret

scene	quit	world	Bye, now! Type '!exit' to get out of here.
	path	back	quit

scene	secret	passage1	Congratulations on reaching the secret scene!
