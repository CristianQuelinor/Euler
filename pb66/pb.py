import math

def is_square(n):
	s = math.sqrt(n)
	
	return s == int(s)

def solve_equation(D): # return minimal x solution of x ** 2 = D * y ** 2 + 1
	if is_square(D):
		return -1	

	y = 1
	x = D * (y ** 2) + 1

	while is_square(x) == False and x ** 2 - D * (y ** 2) != 1:
		print y
		y += 1
		x = D * (y ** 2) + 1

	return math.sqrt(x)

def solution():
	x_maximum = -1
	D_max = -1

	for D in range(2, 1001):
		x = solve_equation(D)

		if x > x_maximum:
			x_maximum = x
			D_max = D

	return D_max

print solution()
