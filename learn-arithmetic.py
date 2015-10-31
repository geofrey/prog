
successors = { '0':'1', '1':'2', '2':'3', '3':'4', '4':'5', '5':'6', '6':'7', '7':'8', '8':'9', '9':'0' }
zero = '0' # gotta start somewhere
one = successors[zero] #cute

def successor(digit):
	if digit not in successors:
		raise ArgumentError
	result = successors[digit]
	return result, one if result == zero else zero

def add(i, j):
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
			sum_value[(i,j)],sum_carry[(i,j)] = add(i, j)
			j,dummy = successor(j)
			if j == zero:
				break
		i,dummy = successor(i)
		if i == zero:
			break
build_additiontables()


def add(i, j): # redefine now that we have tables
	return sum_value[i, j], sum_carry[i, j]

#print(add('6', '7'))

def full_add(i, j, ci):
	s,c = add(i, j)
	s,co = add(s, ci)
	co,dummy = add(c, co) # actually we'll never carry out more than 1 from a single-digit sum...
	return s, co

#print(full_add('8', '2', zero))
#print(full_add('8', '2', '1'))

def digits_add(p1, p2):
	result = []
	carry = zero
	if len(p2) > len(p1): # hmm, '>' is a bit too much like knowing what a number is
		p1, p2 = p2, p1
	for place in range(len(p2)):
		result[len(result):], carry = full_add(p1[place], p2[place], carry)
	for place in range(len(p2), len(p1)):
		result[len(result):], carry = add(p1[place], carry)
	result[len(result):] = carry
	return result

twentythree = ['3', '2']
nineninety = ['0', '9', '9']
print(digits_add(twentythree, nineninety))

def prettyprint(digits):
	stigid = digits[:]
	stigid.reverse()
	print(''.join(stigid))

prettyprint(digits_add(nineninety, twentythree))
