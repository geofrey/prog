
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

print(add('6', '7'))

def add(i, j): # let's make it prettier
	return ''.join([sum_carry[(i,j)], sum_value[(i,j)]])

print(add('6', '7'))
