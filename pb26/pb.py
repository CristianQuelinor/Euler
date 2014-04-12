def ordre(x, n):
	a = x

	for i in range(1, n):
		if a == 1:
			return i	
		else:
			a = (a * x % n)

max_period = 0
max_d = 0

for d in range(3, 1001, 2):
	if d % 5 != 0:
		period = ordre(10, d)
		
		if period > max_period:
			max_period = period
			max_d = d
	
print max_d
