#!/usr/bin/python3

import math
import sys

class Binop:
	def __init__(self, l, r):
		self.left = l
		self.right = r

class Sum(Binop):
	def __str__(self):
		return "{0} + {1}".format(self.left, self.right)
	def evaluate(self):
		return self.left.evaluate() + self.right.evaluate()

class Product(Binop):
	def __str__(self):
		return "{0}*{1}".format(
			("({0})" if self.left.__class__ == Sum else "{0}").format(self.left),
			("({0})" if self.right.__class__ == Sum else "{0}").format(self.right)
		)
	def evaluate(self):
		return self.left.evaluate() * self.right.evaluate()

class Exp(Binop):
	def __str__(self):
		#return "{0}^{1}".format(
		return "{0}<sup>{1}</sup>".format(
			self.left,
			("{0}" if self.right.__class__ == Literal or self.right.__class__ == Exp else "({0})").format(self.right)
		)
	def evaluate(self):
		return self.left.evaluate() ** self.right.evaluate()

class Literal:
	def __init__(self, v):
		self.v = v
	def __str__(self):
		return str(self.v)
	def evaluate(self):
		return self.v

class Unop:
	def __init__(self, u):
		self.arg = u

class Neg(Unop):
	def __str__(self):
		return "-{0}".format(self.arg)
	def evaluate(self):
		return self.arg.evaluate() * -1

def tower(base, n):
	if n < base:
		return Literal(n)
	if base <= 1:
		return 'no.'
	
	power = 0
	while base ** (power+1) <= n:
		power += 1
	unit = base ** power
	count = 0
	while unit * (count + 1) <= n:
		count += 1
	high = unit * count
	low = n - high
	
	theExp = Literal(1) if power == 0 else Literal(base) if power == 1 else Exp(Literal(base), tower(base, power))
	theProd = Literal(0) if count == 0 else theExp if count == 1 else Product(tower(base, count), theExp)
	theSum = Sum(theProd, tower(base, low)) if low > 0 else theProd
	return theSum

if len(sys.argv) == 3:
	base = int(sys.argv[1])
	n = int(sys.argv[2])
	print(tower(base, n))
else:
	while True:
		line = input().strip()
		if len(line) == 0:
			break
		base, n = [int(word) for word in line.split()]
		print(tower(base, n))
		sys.stdout.flush()
#

