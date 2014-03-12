import functools
import re

commentpattern = re.compile(r'\s*(?<!\\)#.*$')
whitespacepattern = re.compile(r'^\s*')
def getindent(line):
	return len(whitespacepattern.match(line).group())

stripcomments = lambda line: re.sub(commentpattern, '', line)

class Linerator:
	lines = []
	pos = 0
	
	def __init__(self, lines):
		self.lines = list(lines)
	
	def hasNext(self):
		return self.pos < len(self.lines)
	
	def peek(self):
		return self.lines[self.pos]
	
	def next(self):
		value = self.peek()
		self.pos += 1
		return value
	
def treead(lines):
	forest = []
	while lines.hasNext():
		current = lines.next()
		childs = []
		if lines.hasNext() and getindent(lines.peek()) > getindent(current):
			childs = treead(lines) # indent increases
		forest.append((current.strip().split('\t'), childs))
		if lines.hasNext() and getindent(current) > getindent(lines.peek()):
			break # indent decreases
	return forest

def sanitizefile(lines):
	return filter(
		lambda line: len(line) > 0, 
		map(
			lambda line: stripcomments(line.rstrip()),
			lines
		)
	)

def applysequence(arg, ops):
	return applysequence(ops[0](arg), ops[1:]) if ops else arg
