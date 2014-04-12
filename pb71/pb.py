def solution():
	result = 0
	(n_max, d_max, f_max) = (2, 5, 2. / 5.)

	for d in range(1000001, 2, -1):
		n = (3 * d - 1) / 7

		if n * d_max > n_max * d:			
				(n_max, d_max) = (n, d)

	return n_max

print solution()
