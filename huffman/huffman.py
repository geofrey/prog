# I'll Huffman, and I'll puff, man, and I'll blow your house down, man.

import functools
import operator

class Puffball:
	def __init__(self, code, symbol, frequency):
		self.code = code
		self.symbol = symbol
		self.frequency = frequency
	
	def __repr__(self):
		return '"{code}": {contents} ({frequency})'.format(code=self.code, contents=self.symbol, frequency=self.frequency)

def loadalphabet(filename):
	file = open(filename, 'r')
	freqtree = []
	for line in file.readlines():
		letter, freq = line.strip().split()
		#freqtree.append(([letter], float(freq)))
		freqtree.append(Puffball(None, letter, float(freq)))
	file.close()
	return freqtree

def symbolize(ball, symbols, prefix=[]):
	ball.code = prefix
	if len(ball.symbol) > 1:
		for i in range(len(ball.symbol)):
			symbolize(ball.symbol[i], symbols, prefix=prefix + [symbols[i]])

def huffmanize(alphabetfile, symbols):
	freqtree = loadalphabet(alphabetfile)
	letters = freqtree[:]
	
	if(len(symbols) > 2):
		dummies = len(symbols) - 1 - (len(freqtree)-1)%(len(symbols)-1)
		for i in range(dummies):
			freqtree.append(Puffball(None, [], 0))

	getweight = lambda entry: entry.frequency

	while len(freqtree) >= len(symbols):
		freqtree.sort(key=getweight)
		cluster = freqtree[:len(symbols)]
		clusterweight = sum(map(getweight, cluster))
		del(freqtree[:len(symbols)])
		freqtree.append(Puffball(None, cluster, clusterweight))
	freqtree = freqtree[0]

	symbolize(freqtree, symbols)

	huffman = map(lambda ball: (''.join(ball.code), ball.symbol) ,letters)
	huffman.sort(key=lambda item: item[1])
	print(freqtree)

	return huffman

codes = [
	['1', '2', '3', '4', '5'],
	list('abcdefghijklmnopqrstuvwxyz'),
	['0', '1'],
	['A', 'B', 'C'],
	['1', '2', '3', '4']
]

def process(symbols):
	for letter in huffmanize('english-freq.txt', symbols):
		print('{letter}: {code}'.format(letter=letter[1], code=letter[0]))

for code in codes:
	print(code)
	process(code)

# doesn't quite work right for complex objects. Trees of simple items flatten just fine.
def flatten(thing, descent=lambda thing:thing, criterion=lambda anything:True, transform=lambda thing:thing):
	try:
		for item in filter(criterion, descent(thing)):
			for flattened in flatten(item, descent=descent, criterion=criterion, transform=transform):
				yield flattened
	except:
		yield transform(thing)

#
