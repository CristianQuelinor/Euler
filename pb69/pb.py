def solution():
	totients = primes = [0] * 1000001
	result = 0
	maximum = 0
	d_maximum = 0

	for d in range(2, 1000001):
		totients[d] = d

	for d in range(2, 1000001):
		if totients[d] == d:
			for j in range(d, 1000001, d):
		   		totients[j] = totients[j] * (d - 1) / d

		if maximum * totients[d] < d:
			d_maximum = d
			maximum = float(d) / float(totients[d])

	return d_maximum

print solution()
