from yeanpypa import *

name = Literal('\'') + Word(alpha) + Literal('\'')
value = name # synonym
destination = name
description = name
scenename = name

path = Literal('path') + name + destination
item = Literal('item') + name + description

effinv = Literal('inventory') + Literal('{') + ( Literal('create') + name + name ) | ( Literal('destroy') + name )
effcreate = Literal('create') + scenename + item
effstate = Literal('state') + name + value
effgo = Literal('go') + name
effpath = Literal('path') + Literal('add') | Literal('remove') + scenename + path

effect = Literal('effect') + effinv | effstate | effgo | effpath | effcreate

#reqinv = Literal('inventory') + name
#reqstate = Literal('state') + name + value
requirement = Literal('require') + ( Literal('inventory') + name ) | ( Literal('state') + name + value )

action = Literal('action') + name + Literal('{') + Word( requirement | effect ) + Literal('}')

scene = Literal('scene') + name + description + Literal('{') + Word( action | path | item ) + Literal('}')

# Each region names its children.
region = Literal('region') + name + Literal('subscenes') + Literal('{') + Word(name) + Literal('}') + Literal('contents') + Literal('{') + Word( scene | action | effect ) + Literal('}')