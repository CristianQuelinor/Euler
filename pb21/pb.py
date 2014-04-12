import math

def d(n):
	sum = 1

	for i in range(2, n):
		if n % i == 0:
			sum += i

	return sum

sum = 0

for i in range(0, 10001):
	d_i = d(i)
	d_d_i = -1
	
	if d_i != i:
		d_d_i = d(d_i)

		if d_d_i == i:
			sum += i

print sum
