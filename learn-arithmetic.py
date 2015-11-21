
# better to define the successor relation explicitly and let order follow from that
successors = { '0':'1', '1':'2', '2':'3', '3':'4', '4':'5', '5':'6', '6':'7', '7':'8', '8':'9', '9':'0' }
# but it's certainly more verbose

def generate_successors(digits):
	global successors
	successors = {digits[i]:digits[i+1] for i in range(len(digits)-1)}
	successors[digits[-1]] = digits[0] # wrap around
#generate_successors('0123456789abcdef') # any sequence

#print(successors)

zero = '0' # gotta start somewhere
one = successors[zero] #cute

def successor(digit):
	if digit not in successors:
		raise ArgumentError
	result = successors[digit]
	return result, one if result == zero else zero

def add_digits(i, j):
	jj = zero
	carry = zero
	while jj != j:
		jj,dummy = successor(jj)
		v, c = successor(i)
		i = v
		carry = c if carry == zero else carry
	return i, carry

#print(add('8', '5'))

def build_additiontables():
	global sum_value
	global sum_carry
	sum_value = {}
	sum_carry = {}
	i = zero
	j = zero
	while True:
		while True:
			sum_value[(i,j)],sum_carry[(i,j)] = add_digits(i, j)
			j,dummy = successor(j)
			if j == zero:
				break
		i,dummy = successor(i)
		if i == zero:
			break
build_additiontables()


def add_digits(i, j): # redefine now that we have tables
	return sum_value[i, j], sum_carry[i, j]

#print(add('6', '7'))

def full_add(i, j, ci):
	s,c = add_digits(i, j)
	s,co = add_digits(s, ci)
	co,dummy = add_digits(c, co) # actually we'll never carry out more than 1 from a single-digit sum...
	return s, co

#print(full_add('8', '2', zero))
#print(full_add('8', '2', '1'))

def add(p1, p2):
	result = []
	carry = zero
	if len(p2) > len(p1): # hmm, '>' is a bit too much like knowing what a number is. Let's pretend ordinals are different.
		p1, p2 = p2, p1
	for place in range(len(p2)): # add pairwise
		result[len(result):], carry = full_add(p1[place], p2[place], carry)
	for place in range(len(p2), len(p1)): # continue carrying
		result[len(result):], carry = add_digits(p1[place], carry)
	if carry != zero: # one last digit
		result[len(result):] = carry
	return result

twentythree = ['3', '2']
nineninety = ['0', '9', '9']
#print(digits_add(twentythree, nineninety))

def prettyprint(digits, width=0):
	stigid = digits[:]
	stigid.reverse()
	print(' '*(width-len(stigid)) + ''.join(stigid))

def multiply_digits(d1, d2):
	count = zero
	value = zero
	carry = zero
	while count != d2:
		value, c = add_digits(value, d1)
		carry, dummy = add_digits(c, carry)
		#print('multiply_digits', count, d1, d2, value, carry)
		count, dummy = successor(count)
	return value, carry

def build_multiplicationtables():
	global product_value
	global product_carry
	product_value = {}
	product_carry = {}
	i = zero
	j = zero
	while True:
		while True:
			product_value[(i,j)], product_carry[(i, j)] = multiply_digits(i, j)
			j, dummy = successor(j)
			if j == zero:
				break
		i, dummy = successor(i)
		if i == zero:
			break
build_multiplicationtables()

def multiply_digits(d1, d2):
	return product_value[(d1, d2)], product_carry[(d1, d2)]

def demo(op, n1, n2, label=None):
	result = op(n1, n2)
	things = [n1, n2, result]
	width = max(map(len, things+[label]))
	if label != None:
		print(label)
	for thing in things:
		prettyprint(thing, width)

#demo(add, twentythree, nineninety, "addition")

def full_multiply(d1, d2, carry_in):
	value, carry = multiply_digits(d1, d2)
	value, c = add_digits(value, carry_in)
	carry, dummy = add_digits(c, carry)
	return value, carry

#print(full_multiply('8', '7', '5'))

def multiply(p1, p2):
	result = [zero]
	place = []
	for d2 in p2:
		stage = place[:] # remember to copy, otherwise strange things happen
		#print('place', place)
		carry = zero
		for d1 in p1:
			stage[len(stage):], carry = full_multiply(d1, d2, carry)
			#print('stage', d2, d1, stage, carry)
		if carry != zero:
			stage[len(stage):] = carry
		result = add(result, stage)
		#print('accumulate', result)
		place += [zero]
	return result

#print(multiply('8', '7'))
#print(add(multiply('8', '7'), '5'))

demo(multiply, twentythree, nineninety, 'multiplication')
#demo(multiply, ['3', '2', '1'], ['6', '5', '4'], 'LOLcats')
