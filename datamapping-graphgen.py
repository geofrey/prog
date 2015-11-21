import sys
import csv
from bedugging import *

if len(sys.argv) != 3:
	dprint(lambda: 'Call {0} with 2 arguments - (1) a source file, CSV data, and (2) a destination file to write GML.'.format(sys.argv[0]), -2)
	exit(-1)

class Node:
	def __init__(self, id, label):
		self.id = id
		self.label = label
	
	def __str__(self):
		dprint(lambda: 'serialize node {0}'.format(self.id), 2)
		return\
'''node [
	id	{id}
	label	"{label}"
]
'''.format(id=self.id, label=self.label)

class Nodelist:
	def __init__(self):
		self.nodes = {}
		self.sedon = {} # 'nodes'.reverse(), get it?
	
	def add(self, label):
		newnode = Node(len(self.nodes)+1, label)
		self.nodes[newnode.id] = newnode
		if newnode.label not in self.sedon:
			self.sedon[newnode.label] = []
		self.sedon[newnode.label].append(newnode) # labels are not required to be unique
		dprint(lambda: 'add node {0} with label {1}'.format(newnode.id, newnode.label), 1)
		return newnode.id
	
	def __getitem__(self, key):
		result = None
		if type(key)==int:
			result = self.nodes[key]
			dprint(lambda: 'look up node {id} by id'.format(id=result.id), 2)
		else:
			result = self.sedon[key]
			dprint(lambda: 'look up node {ids} by name {name}'.format(ids=list(map(lambda node:node.id, result)), name=key), 2)
		return result
	
	def __contains__(self, key):
		return key in self.nodes or key in self.sedon
	
	def __str__(self):
		return ''.join(map(str, self.nodes.values()))

class Edge:
	def __init__(self, id, src, dst, label):
		self.id = id
		self.src = src
		self.dst = dst
		self.label = label
	
	def __str__(self):
		dprint(lambda: 'serialize edge {0}'.format(self.id), 2)
		return\
'''edge [
	id	{id}
	source	{source}
	target	{destination}
	label	"{label}"
	graphics [
		targetArrow	"standard"
	]
]
'''.format(id=self.id, source=self.src, destination=self.dst, label=self.label)

class Edgelist:
	def __init__(self):
		self.edges = {}
		self.segde = {}
	
	def add(self, srcid, dstid, label):
		newedge = Edge(len(self.edges)+1, srcid, dstid, label)
		self.edges[newedge.id] = newedge
		if newedge.id not in self.segde:
			self.segde[newedge.id] = []
		self.segde[newedge.id].append(newedge)
		dprint(lambda: 'add edge {id}: {src}--"{label}"-->{dst}'.format(id=newedge.id, src=newedge.src, dst=newedge.dst, label=newedge.label), 1)
		return newedge.id
	
	def __getitem__(self, key):
		result = None
		if type(key)==int:
			result = self.edges[key]
			dprint(lambda: 'look up edge {id} by id: {src}->{dst}'.format(id=key, src=result.src, dst=result.src), 1)
		else:
			result = self.segde[key]
			dprint(lambda: 'look up edge {id} by name {name}: {src}->{dst}'.format(id=result.id, name=key, src=result.src, dst=result.src), 1)
		return result
	
	def __contains__(self, key):
		return key in self.edges or key in self.segde
	
	def __str__(self):
		return "".join(map(str, self.edges.values()))

class Graph:
	def __init__(self):
		self.nodes = Nodelist()
		self.edges = Edgelist()
	
	def add_node(self, label=''):
		return self.nodes.add(label)
	
	def add_edge_id(self, srcid, dstid, label=''):
		return self.edges.add(srcid, dstid, label)
	
	def add_edge_name(self, srcname, dstname, label=''):
		sources = self.nodes[srcname]
		if len(sources) > 1:
			dprint(lambda: 'Multiple sources matching name "{0}".'.format(srcname), -1)
			#raise KeyError('Multiple sources matching name "{0}".'.format(srcname))
		
		destinations = self.nodes[dstname]
		if len(destinations) > 1:
			dprint(lambda: 'Multiple destinations matching name "{0}".'.format(dstname), -1)
			#raise KeyError('Multiple destinations matching name "{0}".'.format(dstname))
		
		return self.add_edge_id(sources[0].id, destinations[0].id, label)
	
	def __str__(self):
		header =\
'''graph [
  version 2
  directed 1
'''
		footer =\
''']
'''
		return ''.join([header, str(self.nodes), str(self.edges), footer])

# nevermind the bollocks, here's the graph processing
dprint(lambda: 'set up')

outfilename = sys.argv[2]
graph = Graph()
reader = csv.reader(open(sys.argv[1], 'r'))
firstline = next(reader)
format = dict([(firstline[position], position) for position in range(len(firstline))])

lines = 0
for row in reader:
	get = lambda key: row[format[key]]
	if get('Short DB Type') == 'Foreign Key':
		src = get('Entity')
		dst = get('FK Entity')
		label = get('Name')
	elif get('Short DB Type') == 'Type Key':
		src = get('Entity')
		dst = get('Typelist')
		label = get('Name')
	else:
		continue
	
	dprint(lambda: 'new foreign key ({src})--{label}-->({dst})'.format(src=src, dst=dst, label=label))
	dprint(lambda: str(row), 2)
	
	excludes = [
		'BasedOnID',
		'BranchID',
		'CreateUserID',
		'FixedID',
		'UpdateUserID'
	]
	excludesuffixes = (
		'Denorm',
		'L10N'
	)
	
	if label in excludes or label.endswith(excludesuffixes) or src.endswith(excludesuffixes) or dst.endswith(excludesuffixes):
		dprint(lambda: 'excluded edge "{0}"'.format(label), 1)
		continue
	
	if src not in graph.nodes:
		srcid = graph.add_node(src)
		dprint(lambda: 'created node for "{0}"'.format(src))
	else:
		sources = graph.nodes[src]
		if len(sources) > 1:
			dprint(lambda: 'Found more than one source "{0}" when adding an edge.'.format(src), -1)
		srcid = sources[0].id
	
	if dst not in graph.nodes:
		dstid = graph.add_node(dst)
		dprint(lambda: 'created node for "{0}"'.format(dst))
	else:
		destinations = graph.nodes[dst]
		if len(destinations) > 1:
			dprint(lambda: 'Found more than one destination "{0}" when adding an edge.'.format(src), -1)
		dstid = destinations[0].id
	
	dprint(lambda: '\n'.join(map(lambda pair: "{id}\t{label}".format(id=pair[0], label=pair[1].label), graph.nodes.nodes.items())), 3)
	
	graph.add_edge_id(srcid, dstid, label)
	
	lines += 1
	if lines % 200 == 0:
		dprint(lambda: 'processed {0} rows'.format(lines), 0)

dprint(lambda: '\n'.join(map(lambda node: '{0}: {1}'.format(node.id, node.label), graph.nodes.nodes.values())), 1)
dprint(lambda: '\n'.join(map(lambda edge: '{0}: ({1})--{2}-->({3})'.format(edge.id, graph.nodes[edge.src].label, edge.label, graph.nodes[edge.dst].label), graph.edges.edges.values())), 1)

del(reader) # forget the belt, let's go straight to suspenders

open(outfilename, 'w').write(str(graph)) # boom

exit(0)
#
