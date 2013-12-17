#!/usr/bin/python3

# Newton's Method applied to find sqrt. I think.

# f(x) = x^2 - a
# f'(x) = 2x
# tangent line at guess: y = f'(g)*(x - g) + f(g)
# or... y = 2g*(x-g)+g^2-a

# tangent's next zero from guess: x = -f(g)/f'(g) + g
# or... x = -(g^2-a)/2g + g

precision = 3
global epsilon
epsilon = 1 * 10**-precision # rather small

def newton_sqrt(value, maxiter=50):
	oldroot = value
	root = value / 2 # nice initial guess
	iterations = 0
	while abs(root - oldroot) > epsilon:
		if iterations > maxiter:
			print('Exceeded {} iterations, something may be wrong here.'.format(maxiter))
			break
		iterations += 1
		oldroot = root
		root = -(root**2-value)/(2*root) + root
	return root

try:
	line = input()
	while line:
		value = float(line)
		print(newton_sqrt(value))
		line = input()
except EOFError:
	pass

exit(0)
