import math

import math

def factor(num):
	factors = []
	f = 2
	f_cap = math.sqrt(num)
	while f <= f_cap:
		f_count = 0
		while num % f == 0:
			f_count = f_count + 1
			num = num / f
		factors.append((f, f_count))
		f = f + 1
	if num > f_cap:
		factors.append((num, 1))
	return filter(lambda (n, v): v > 0, factors)



def test_factor(n):
	for i in range(1, n+1):
		decomposed = factor(i)
		product = 1
		for (f, p) in decomposed:
			product = product * f**p
		d = {'num': i}
		if product != i:
			print 'product of factor(%(num)d) NOT EQUAL TO %(num)d' % d

import sys
if len(sys.argv) == 2:
	print(factor(int(sys.argv[1])))

